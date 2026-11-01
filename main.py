import datetime

from szemely_auto import Személyautó
from teher_auto import Teherautó
from autokolcsonzo import Autókölcsönző


# ---------------------------------------------------------------------------
# Seed adatok
# ---------------------------------------------------------------------------

def seed_adatok_betoltese() -> Autókölcsönző:
    """Létrehozza a kölcsönzőt az előre definiált autókkal és bérlésekkel."""
    kolcsonzo = Autókölcsönző("Czétényi Kristóf Gépjármű Kölcsönző Kft.")

    # 3 autó
    a1 = Személyautó("GDE-001", 15000, 5, "manuális", 400, 600, "Ford", "Mondeo")
    a2 = Személyautó("GDE-002", 18000, 5, "automata", 350, 700, "Toyota", "Camry")
    a3 = Teherautó("GDE-003", 35000, 2, 3500, 90, 800, 600, 210, 230)

    kolcsonzo.auto_hozzaadasa(a1)
    kolcsonzo.auto_hozzaadasa(a2)
    kolcsonzo.auto_hozzaadasa(a3)

    # 4 bérlés (hardcoded dátumok 2026-04-19 és 2026-06-19 között)
    kolcsonzo.berles_feltoltese(a1, datetime.date(2026, 5, 2))
    kolcsonzo.berles_feltoltese(a2, datetime.date(2026, 5, 10))
    kolcsonzo.berles_feltoltese(a3, datetime.date(2026, 5, 20))
    kolcsonzo.berles_feltoltese(a1, datetime.date(2026, 6, 1))

    return kolcsonzo


# ---------------------------------------------------------------------------
# CLI folyamatok
# ---------------------------------------------------------------------------

def menu_kiiras(nev: str) -> None:
    print(f"\n{'='*50}")
    print(f"  {nev}")
    print(f"{'='*50}")
    print("  1. Autó bérlése")
    print("  2. Bérlés lemondása")
    print("  3. Bérlések listázása")
    print("  0. Kilépés")
    print(f"{'='*50}")


def autok_kilistazasa(kolcsonzo: Autókölcsönző) -> None:
    autok = kolcsonzo.get_autok()
    print("\nElérhető autók:")
    for i, auto in enumerate(autok, start=1):
        print(f"  {i}. {auto.leiras(reszletes=False)}")


def berles_folyamat(kolcsonzo: Autókölcsönző) -> None:
    """Autó bérlésének folyamata. Hiba esetén újra kérdez, nem tér vissza a főmenübe."""
    while True:
        autok_kilistazasa(kolcsonzo)
        print("  d. Autó részleteinek megtekintése")
        print("  Enter. Visszalépés")

        valasztas = input("\nVálasztás (rendszám / d / Enter): ").strip().upper()

        if valasztas == "":
            return

        if valasztas == "D":
            autok = kolcsonzo.get_autok()
            rendszam_reszlet = input("Adja meg a megtekinteni kívánt autó rendszámát: ").strip().upper()
            talalt = next((a for a in autok if a.get_rendszam() == rendszam_reszlet), None)
            if talalt:
                print(f"\n  {talalt.leiras(reszletes=True)}")
            else:
                print(f"Hiba: Nem található autó ezzel a rendszámmal: '{rendszam_reszlet}'")
            continue

        # valasztas == rendszam
        rendszam = valasztas
        datum_str = input("Adja meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ").strip()
        try:
            datum = datetime.date.fromisoformat(datum_str)
        except ValueError:
            print("Hiba: Érvénytelen dátumformátum. Használja az ÉÉÉÉ-HH-NN formátumot.")
            continue

        try:
            ar = kolcsonzo.auto_berles(rendszam, datum)
            berlesek = kolcsonzo.get_berlesek()
            azonosito = berlesek[-1].get_azonosito()
            print(f"\nSikeres bérlés! Ár: {ar:,.0f} Ft. Azonosító: {azonosito}")
            return
        except ValueError as e:
            print(f"Hiba: {e}")


def lemondas_folyamat(kolcsonzo: Autókölcsönző) -> None:
    """Bérlés lemondásának folyamata. Hiba esetén újra kérdez, nem tér vissza a főmenübe."""
    berlesek = kolcsonzo.get_berlesek()
    if not berlesek:
        print("\nNincs aktív bérlés, amit le lehetne mondani.")
        return

    print("\nAktív bérlések:")
    for berles in berlesek:
        print(f"  {berles}")

    while True:
        azonosito = input("\nAdja meg a lemondandó bérlés azonosítóját (vagy Enter a visszalépéshez): ").strip()
        if azonosito == "":
            return
        try:
            kolcsonzo.berles_lemondas(azonosito)
            print("Bérlés sikeresen lemondva.")
            return
        except ValueError as e:
            print(f"Hiba: {e}")


def listazas_folyamat(kolcsonzo: Autókölcsönző) -> None:
    """Az aktív bérlések listázásának folyamata."""
    berlesek = kolcsonzo.berlesek_listazasa()
    if not berlesek:
        print("\nNincs aktív bérlés.")
    else:
        print(f"\nAktív bérlések ({len(berlesek)} db):")
        for berles in berlesek:
            print(f"  {berles}")


# ---------------------------------------------------------------------------
# Belépési pont
# ---------------------------------------------------------------------------

def main() -> None:
    kolcsonzo = seed_adatok_betoltese()

    while True:
        menu_kiiras(kolcsonzo.get_nev())
        valasztas = input("Választás: ").strip()

        if valasztas == "1":
            berles_folyamat(kolcsonzo)
        elif valasztas == "2":
            lemondas_folyamat(kolcsonzo)
        elif valasztas == "3":
            listazas_folyamat(kolcsonzo)
        elif valasztas == "0":
            print("\nViszontlátásra!")
            break
        else:
            print("Érvénytelen választás. Kérem adjon meg 0–3 közötti számot.")


if __name__ == "__main__":
    main()
