# PRD: Autókölcsönző Rendszer

**Status:** Approved  
**Author:** TARS | Analyst  
**Date:** 2026-04-19 
**Approved by:** Czétényi Kristóf I62GFT
**Approval date:** 2026-04-19 
**Feature ID:** PRD-001  
**Brief Reference:** `docs/01-fb-autokolcsonzo-rendszer.md` (FB-001)

---

## Summary

A self-contained Python application that implements a simple car rental system using object-oriented programming principles. Users interact via a numbered CLI menu to rent a car for a single day, cancel an existing rental, or list all active rentals. The application pre-loads seed data on startup and requires no third-party packages. It is a university graded assignment with an updated submission deadline of 2026-12-06.

---

## Problem Statement

A university OOP course requires a fully functional Python car rental application demonstrating abstraction, encapsulation, and inheritance. The instructor evaluates the submission by cloning the public GitHub repository and running the project in PyCharm — it must start and operate correctly from a fresh clone without any additional setup.

---

## Goals

- The system shall implement a clean OOP class hierarchy as specified by the assignment.
- The system shall enable the user to rent, cancel, and list car rentals through a CLI.
- The system shall validate all input and handle errors gracefully without crashing.
- The system shall pre-load operational seed data on startup.
- The system shall run with no dependencies beyond Python's standard library.

---

## Non-Goals

- No file-based or database persistence.
- No multi-day or date-range rental support.
- No user authentication or multi-user support.
- No web, API, or GUI interface.
- No payment processing.
- No fleet management beyond the 3 pre-loaded cars.

---

## Domain Concepts Involved

| Concept | Description |
|---|---|
| `Auto` | Abstract base class representing a rentable vehicle with plate number, type, and daily rate |
| `Személyautó` | Passenger car subclass with additional passenger/comfort attributes |
| `Teherautó` | Truck subclass with load and performance constraint attributes |
| `Autókölcsönző` | Rental company entity owning a fleet of cars |
| `Bérlés` | A rental record binding one car to one calendar date |

---

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-001 | The system shall define `Auto` as an abstract base class with non-public attributes: plate number (`_rendszam`), vehicle type (`_tipus`), and daily rental rate (`_berleti_dij`). |
| FR-002 | The system shall provide public getter and setter methods for every non-public attribute on `Auto` and its subclasses. |
| FR-003 | The system shall define `Személyautó` as a concrete subclass of `Auto` with the following additional non-public attributes: passenger count (`_utas_szam`), transmission type (`_valto`: `"manuális"` or `"automata"`), luggage compartment size in litres (`_csomagtarto_meret`), and range in km (`_hatotav`). |
| FR-004 | The system shall define `Teherautó` as a concrete subclass of `Auto` with the following additional non-public attributes: passenger count (`_utas_szam`), weight limit in kg (`_terhebiras`), speed limit in km/h (`_sebesseg_korlat`), and range in km (`_hatotav`). |
| FR-005 | The system shall define `Autókölcsönző` with a non-public company name attribute (`_nev`) and a non-public list of cars (`_autok`). |
| FR-006 | The system shall define `Bérlés` with a non-public reference to a car and a non-public rental date (`_datum`), where the date represents a single calendar day. Each `Bérlés` instance shall have a unique identifier composed of an auto-incremented integer, the car's plate number, and the rental date, formatted as `{id}-{rendszam}-{datum}` (e.g., `1-ABC-123-2026-05-01`). |
| FR-007 | The system shall allow renting an available car: given a valid car identifier and a valid future date, a new `Bérlés` is created, added to the active rental list, and the computed daily rental price is returned to the user. |
| FR-008 | The system shall reject a rental attempt when the chosen car is already rented for the requested date, and display an informative error message. |
| FR-009 | The system shall reject a rental attempt when the provided date is invalid (e.g., wrong format, past date), and display an informative error message. |
| FR-010 | The system shall allow cancelling an existing rental: given a valid rental identifier, the corresponding `Bérlés` is removed from the active rental list. |
| FR-011 | The system shall reject a cancellation attempt when no rental matching the given identifier exists, and display an informative error message. |
| FR-012 | The system shall display all active rentals when the user requests a listing, showing at minimum: rental identifier, car plate number, car type, and rental date. |
| FR-013 | The system shall display a meaningful message when the rental list is empty. |
| FR-014 | The system shall pre-load on startup: one `Autókölcsönző` instance containing exactly 3 cars (mix of `Személyautó` and `Teherautó`) and 4 `Bérlés` instances with hardcoded dates falling between 2026-04-19 and 2026-06-19, so the user receives a ready-to-use system. |
| FR-015 | The system shall provide a numbered CLI menu with at minimum the following options: (1) Rent a car, (2) Cancel a rental, (3) List rentals, (0) Exit. Navigation uses numeric input only. |
| FR-016 | The system shall terminate cleanly when the user selects the exit option. |

---

## Non-Functional Requirements

| ID | Requirement | Category |
|---|---|---|
| NFR-001 | The application must be implemented entirely in Python using only the standard library. No third-party packages are permitted. | Portability |
| NFR-002 | The application must start and run correctly from a fresh `git clone` in PyCharm without any `pip install` or manual environment setup. | Deployability |
| NFR-003 | No unhandled exception may propagate to the user. All error paths must be caught and result in a readable message, after which the menu is re-displayed. | Reliability |
| NFR-004 | The codebase must demonstrate: abstraction via an abstract base class (`Auto`), encapsulation via non-public attributes and accessors, and inheritance via `Személyautó` and `Teherautó`. | Code quality |
| NFR-005 | The GitHub repository must be set to public visibility at the time of submission. | Deliverability |
| NFR-006 | A `NEPTUNKOD.docx` file must exist at the repository root containing the public GitHub repository URL. The Neptun code is `I62GFT`. | Deliverability |

---

## Acceptance Criteria

| ID | Criterion | Linked FR |
|---|---|---|
| AC-001 | Given the application is started, when the main menu is displayed, then options 1, 2, 3, and 0 are shown. | FR-015 |
| AC-002 | Given 3 cars and 4 rentals are pre-loaded, when the user selects "List rentals" immediately after startup, then all 4 rentals are displayed with car plate, type, and date. | FR-012, FR-014 |
| AC-003 | Given a car is available on a date, when the user selects "Rent a car" and provides a valid plate/ID and a valid future date, then a new rental is created and the daily rental price is shown. | FR-007 |
| AC-004 | Given a car is already rented on a date, when the user attempts to rent the same car for the same date, then the rental is rejected with an informative message and no new rental is created. | FR-008 |
| AC-005 | Given the user enters an invalid date (wrong format or past), when attempting to rent, then the operation is rejected with an informative message. | FR-009 |
| AC-006 | Given an existing rental, when the user selects "Cancel a rental" and provides its identifier, then the rental is removed and no longer appears in the list. | FR-010 |
| AC-007 | Given a non-existent rental identifier, when the user attempts to cancel, then the operation is rejected with an informative message. | FR-011 |
| AC-008 | Given the application is cloned from the public GitHub repository into a new PyCharm project with no additional setup, when the main Python file is run, then the application starts and the menu is displayed without errors. | NFR-001, NFR-002 |
| AC-009 | Given any invalid input (non-numeric menu choice, malformed date, out-of-range selection), when entered by the user, then no unhandled exception occurs and the menu is re-displayed. | NFR-003 |
| AC-010 | Given `Auto` is defined, when inspected, then it is an abstract class that cannot be instantiated directly. | NFR-004 |
| AC-011 | Given a `Személyautó` instance, when accessed via getters, then all 7 attributes (3 base + 4 subclass) return correct values. | FR-002, FR-003 |
| AC-012 | Given a `Teherautó` instance, when accessed via getters, then all 7 attributes (3 base + 4 subclass) return correct values. | FR-002, FR-004 |
| AC-013 | Given `NEPTUNKOD.docx` exists at the repository root, when opened, then it contains the public GitHub repository URL. | NFR-006 |

---

## Open Questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | Should the seed data rental dates be set to future dates relative to execution time, or are fixed hardcoded dates acceptable? | Developer | **Closed** — Hardcoded dates between 2026-04-19 and 2026-06-19. |
| 2 | Should the rental identifier used in cancellation be an auto-incremented integer, or derived from car plate + date? | Architect | **Closed** — Format: `{auto-increment}-{rendszam}-{datum}` (e.g., `1-ABC-123-2026-05-01`). |
