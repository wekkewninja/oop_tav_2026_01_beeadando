import datetime
from auto import Auto
from berles import Bérlés


class Autókölcsönző:
    """Autókölcsönző céget és a bérlési üzleti logikát reprezentáló osztály."""

    def __init__(self, nev: str):
        self._nev = nev
        self._autok: list[Auto] = []
        self._berlesek: list[Bérlés] = []
        self._berles_szamlalo: int = 0

    # --- nev ---
    def get_nev(self) -> str:
        return self._nev

    def set_nev(self, nev: str) -> None:
        if not nev or not isinstance(nev, str):
            raise ValueError("A kölcsönző neve nem lehet üres.")
        self._nev = nev

    # --- autok (returns copy) ---
    def get_autok(self) -> list[Auto]:
        return list(self._autok)

    def auto_hozzaadasa(self, auto: Auto) -> None:
        """Autót ad a flottához (belső használatra, seed betöltésnél)."""
        self._autok.append(auto)

    # --- berlesek (returns copy) ---
    def get_berlesek(self) -> list[Bérlés]:
        return list(self._berlesek)

    # --- üzleti logika ---

    def auto_berles(self, rendszam: str, datum: datetime.date) -> float:
        """
        Bérel egy autót a megadott napra.
        Visszaadja a napi bérleti díjat.
        ValueError-t dob, ha az autó nem elérhető vagy a dátum érvénytelen.
        """
        if datum < datetime.date.today():
            raise ValueError("A bérlési dátum nem lehet múltbeli.")

        auto = self._auto_keresese(rendszam)

        for berles in self._berlesek:
            if berles.get_auto().get_rendszam() == rendszam and berles.get_datum() == datum:
                raise ValueError(
                    f"Az {rendszam} rendszámú autó {datum}-ra már foglalt."
                )

        self._berles_szamlalo += 1
        uj_berles = Bérlés(self._berles_szamlalo, auto, datum)
        self._berlesek.append(uj_berles)
        return auto.get_berleti_dij()

    def berles_feltoltese(self, auto: Auto, datum: datetime.date) -> None:
        """
        Seed adatok betöltéséhez — bérlést hoz létre ellenőrzés nélkül
        (a seed dátumok a múltban is lehetnek, ezért az auto_beresles
        validációját megkerüljük).
        """
        self._berles_szamlalo += 1
        uj_berles = Bérlés(self._berles_szamlalo, auto, datum)
        self._berlesek.append(uj_berles)

    def berles_lemondas(self, azonosito: str) -> None:
        """
        Lemondja a megadott azonosítójú bérlést.
        ValueError-t dob, ha nem létezik ilyen bérlés.
        """
        for berles in self._berlesek:
            if berles.get_azonosito() == azonosito:
                self._berlesek.remove(berles)
                return
        raise ValueError(f"Nem található bérlés ezzel az azonosítóval: '{azonosito}'")

    def berlesek_listazasa(self) -> list[Bérlés]:
        """Visszaadja az aktív bérlések másolatát."""
        return list(self._berlesek)

    # --- privát segédmetódus ---

    def _auto_keresese(self, rendszam: str) -> Auto:
        """Rendszám alapján megkeresi az autót. ValueError, ha nem létezik."""
        for auto in self._autok:
            if auto.get_rendszam() == rendszam:
                return auto
        raise ValueError(f"Nem található autó ezzel a rendszámmal: '{rendszam}'")
