# Architecture Design: Autókölcsönző Rendszer

**Status:** Approved  
**Author:** TARS | Architect  
**Date:** 2026-04-19  
**Approved by:** Czétényi Kristóf I62GFT
**Approveal date:** 2026-04-20
**PRD Reference:** `docs/02-prd-autokolcsonzo-rendszer.md` (PRD-001)

---

## Overview

A single-process, in-memory Python CLI application structured around a five-class OOP hierarchy. There are no external dependencies — only the Python standard library (`abc`, `datetime`). The application runs from a single entry point (`main.py`) and follows a module-per-class file layout for clarity and maintainability. All state lives in a single `Autókölcsönző` instance created at startup with seed data pre-loaded. The CLI is a simple `while True` numbered menu loop with input validation at every step.

---

## Module / File Structure

```
autokolcsonzo/          ← project root (also the git repo root)
│
├── main.py             ← entry point: creates seed data, starts CLI loop
├── auto.py             ← Auto (abstract base class)
├── szemely_auto.py     ← Személyautó(Auto)
├── teher_auto.py       ← Teherautó(Auto)
├── berles.py           ← Bérlés (rental record)
├── autokolcsonzo.py    ← Autókölcsönző (rental company, business logic)
│
├── NEPTUNKOD.docx      ← contains the public GitHub repository URL
└── README.md           ← brief project description and run instructions
```

No packages/sub-folders are needed for a project of this scope. All modules are co-located at the root.

---

## Domain Model

### `Auto` — abstract base class (`auto.py`)

| Attribute | Type | Access | Description |
|---|---|---|---|
| `_rendszam` | `str` | getter / setter | Licence plate number |
| `_tipus` | `str` | getter only | Vehicle type label (set at construction) |
| `_berleti_dij` | `float` | getter / setter | Daily rental rate in HUF |

- Defined with `abc.ABC` and `abc.abstractmethod`.
- Abstract method: `__str__` — each subclass must implement a human-readable string representation.
- `_tipus` is set by the subclass constructor and is read-only from outside (no setter).

---

### `Személyautó(Auto)` — passenger car (`szemely_auto.py`)

| Attribute | Type | Access | Description |
|---|---|---|---|
| `_utas_szam` | `int` | getter / setter | Passenger capacity |
| `_valto` | `str` | getter / setter | Transmission: `"manuális"` or `"automata"` |
| `_csomagtarto_meret` | `int` | getter / setter | Boot size in litres |
| `_hatotav` | `int` | getter / setter | Range in km |

- Sets `_tipus = "Személyautó"` in `__init__`.
- Validates `_valto` on construction and in setter: must be `"manuális"` or `"automata"` (raises `ValueError` otherwise).

---

### `Teherautó(Auto)` — truck (`teher_auto.py`)

| Attribute | Type | Access | Description |
|---|---|---|---|
| `_utas_szam` | `int` | getter / setter | Cab passenger capacity |
| `_terhebiras` | `float` | getter / setter | Weight limit in kg |
| `_sebesseg_korlat` | `int` | getter / setter | Speed limit in km/h |
| `_hatotav` | `int` | getter / setter | Range in km |

- Sets `_tipus = "Teherautó"` in `__init__`.

---

### `Bérlés` — rental record (`berles.py`)

| Attribute | Type | Access | Description |
|---|---|---|---|
| `_auto` | `Auto` | getter only | The rented vehicle |
| `_datum` | `datetime.date` | getter only | Rental date (single day) |
| `_azonosito` | `str` | getter only | Unique identifier: `{seq}-{rendszam}-{datum}` |

- `_azonosito` is computed in `__init__` from a passed-in sequence number, the car's plate, and the date.
- The class holds no mutable state after construction — all attributes are set once and read-only.
- `__str__` returns a formatted single-line summary for display in the rental list.

**Identifier format example:** `3-ABC-123-2026-05-15`

---

### `Autókölcsönző` — rental company + business logic (`autokolcsonzo.py`)

| Attribute | Type | Access | Description |
|---|---|---|---|
| `_nev` | `str` | getter / setter | Company name |
| `_autok` | `list[Auto]` | getter (returns copy) | Fleet of cars |
| `_berlesek` | `list[Bérlés]` | getter (returns copy) | Active rentals |
| `_berles_szamlalo` | `int` | private | Auto-increment counter for rental IDs |

**Methods:**

| Method | Signature | Description |
|---|---|---|
| `auto_berles` | `(rendszam: str, datum: date) -> float` | Validates availability and date, creates `Bérlés`, appends to `_berlesek`, increments counter, returns daily rate. Raises `ValueError` on conflict or invalid input. |
| `berles_lemondas` | `(azonosito: str) -> None` | Finds and removes rental by identifier. Raises `ValueError` if not found. |
| `berlesek_listazasa` | `() -> list[Bérlés]` | Returns a copy of the active rental list. |
| `_auto_keresese` | `(rendszam: str) -> Auto` | Private helper — finds a car by plate number. Raises `ValueError` if not found. |

**Validation rules enforced inside `auto_berles`:**
1. `rendszam` must match an existing car in `_autok`.
2. `datum` must be a `datetime.date` instance ≥ today.
3. No existing `Bérlés` in `_berlesek` has the same car and same date.

---

## CLI Design (`main.py`)

```
create_seed_data() → Autókölcsönző
    │
    └─► while True:
            display_menu()
            choice = input()
            if choice == "1": rent_flow()
            elif choice == "2": cancel_flow()
            elif choice == "3": list_flow()
            elif choice == "0": exit
            else: "Érvénytelen választás."
```

**`rent_flow(kolcsonzo)`**
1. Display the fleet (plate + type + daily rate); `d` opens car details and Enter returns to the main menu.
2. Ask for a car plate number and date (`YYYY-MM-DD`).
3. Parse date with `datetime.date.fromisoformat()` — catches `ValueError`.
4. Call `kolcsonzo.auto_berles(rendszam, datum)` — catches `ValueError`, prints the error, and repeats the rental flow.
5. On success: print `"Sikeres bérlés! Ár: {ár} Ft. Azonosító: {azonosito}"` and return to the main menu.

**`cancel_flow(kolcsonzo)`**
1. Display all active rentals.
2. Ask for rental identifier input.
3. Call `kolcsonzo.berles_lemondas(azonosito)` — catches `ValueError`, prints error.
4. On success: print `"Bérlés sikeresen lemondva."`.

**`list_flow(kolcsonzo)`**
1. Call `kolcsonzo.berlesek_listazasa()`.
2. If empty: print `"Nincs aktív bérlés."`.
3. Otherwise: print each rental using `__str__`.

Rent and cancellation flows repeat after invalid input; success or Enter-to-return exits the flow to the main menu.

---

## Seed Data (defined in `main.py`)

| # | Type | Rendszám | Berleti díj | Extra attributes |
|---|---|---|---|---|
| 1 | `Személyautó` | `GDE-001` | 15 000 Ft/nap | 5 utas, manuális, 400 L, 600 km |
| 2 | `Személyautó` | `GDE-002` | 18 000 Ft/nap | 5 utas, automata, 350 L, 700 km |
| 3 | `Teherautó` | `GDE-003` | 35 000 Ft/nap | 2 utas, 3 500 kg, 90 km/h, 800 km |

| # | Rendszám | Dátum |
|---|---|---|
| 1 | `GDE-001` | 2026-05-02 |
| 2 | `GDE-002` | 2026-05-10 |
| 3 | `GDE-003` | 2026-05-20 |
| 4 | `GDE-001` | 2026-06-01 |

---

## Error Handling Strategy

Business rule violations are raised as `ValueError` with Hungarian-language messages inside the domain classes. The CLI catches expected `ValueError` exceptions, prints the message, and repeats the current rental or cancellation flow.

```python
# Pattern used throughout CLI flows:
try:
    result = kolcsonzo.some_operation(...)
except ValueError as e:
    print(f"Hiba: {e}")
```

---

## Extensibility Notes (for future use — not implemented now)

| Extension | Design target |
|---|---|
| Multi-day rentals | `Bérlés` would gain `_vege_datum`; `auto_berles` would check date range overlaps |
| Persistence | `Autókölcsönző` could be wrapped with a `save()`/`load()` using `json` (stdlib) |
| Additional car types | New subclass of `Auto` — no changes needed to `Autókölcsönző` or `Bérlés` |

---

## Open Questions

None — all design decisions resolved by the PRD and confirmed answers.
