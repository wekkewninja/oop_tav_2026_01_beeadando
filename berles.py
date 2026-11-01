import datetime
from auto import Auto


class Bérlés:
    """Egy autó egynapi bérlését reprezentáló osztály."""

    def __init__(self, sorszam: int, auto: Auto, datum: datetime.date):
        self._auto = auto
        self._datum = datum
        self._azonosito = f"{sorszam}-{auto.get_rendszam()}-{datum}"

    # --- auto (read-only) ---
    def get_auto(self) -> Auto:
        return self._auto

    # --- datum (read-only) ---
    def get_datum(self) -> datetime.date:
        return self._datum

    # --- azonosito (read-only) ---
    def get_azonosito(self) -> str:
        return self._azonosito

    def __str__(self) -> str:
        return (
            f"Azonosító: {self._azonosito:<30} | "
            f"Típus: {self._auto.get_tipus():<12} | "
            f"Rendszám: {self._auto.get_rendszam():<10} | "
            f"Dátum: {self._datum}"
        )
