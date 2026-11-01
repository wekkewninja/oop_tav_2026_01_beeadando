from auto import Auto


VALID_VALTO = ("manuális", "automata")


class Személyautó(Auto):
    """Személyautót reprezentáló osztály."""

    def __init__(
        self,
        rendszam: str,
        berleti_dij: float,
        utas_szam: int,
        valto: str,
        csomagtarto_meret: int,
        hatotav: int,
        gyarto: str,
        modell: str,
    ):
        super().__init__(rendszam, berleti_dij)
        self._tipus = "Személyautó"
        self._utas_szam = utas_szam
        self._set_valto_validated(valto)
        self._csomagtarto_meret = csomagtarto_meret
        self._hatotav = hatotav
        self._gyarto = gyarto
        self._modell = modell

    # --- utas_szam ---
    def get_utas_szam(self) -> int:
        return self._utas_szam

    def set_utas_szam(self, utas_szam: int) -> None:
        if utas_szam < 1:
            raise ValueError("Az utasszám legalább 1 kell legyen.")
        self._utas_szam = utas_szam

    # --- valto ---
    def _set_valto_validated(self, valto: str) -> None:
        if valto not in VALID_VALTO:
            raise ValueError(f"Érvénytelen váltótípus: '{valto}'. Elfogadott: {VALID_VALTO}")
        self._valto = valto

    def get_valto(self) -> str:
        return self._valto

    def set_valto(self, valto: str) -> None:
        self._set_valto_validated(valto)

    # --- csomagtarto_meret ---
    def get_csomagtarto_meret(self) -> int:
        return self._csomagtarto_meret

    def set_csomagtarto_meret(self, meret: int) -> None:
        if meret < 0:
            raise ValueError("A csomagtartó mérete nem lehet negatív.")
        self._csomagtarto_meret = meret

    # --- hatotav ---
    def get_hatotav(self) -> int:
        return self._hatotav

    def set_hatotav(self, hatotav: int) -> None:
        if hatotav <= 0:
            raise ValueError("A hatótáv pozitív szám kell legyen.")
        self._hatotav = hatotav

    # --- gyarto ---
    def get_gyarto(self) -> str:
        return self._gyarto

    def set_gyarto(self, gyarto: str) -> None:
        if not gyarto or not isinstance(gyarto, str):
            raise ValueError("A gyártó neve nem lehet üres.")
        self._gyarto = gyarto

    # --- modell ---
    def get_modell(self) -> str:
        return self._modell

    def set_modell(self, modell: str) -> None:
        if not modell or not isinstance(modell, str):
            raise ValueError("A modell neve nem lehet üres.")
        self._modell = modell

    def leiras(self, reszletes: bool = True) -> str:
        if not reszletes:
            return f"[Személyautó] {self._rendszam} | {self._berleti_dij:,.0f} Ft/nap"
        return (
            f"[Személyautó] {self._rendszam} | "
            f"{self._gyarto} {self._modell} | "
            f"{self._berleti_dij:,.0f} Ft/nap | "
            f"{self._utas_szam} utas | "
            f"{self._valto} | "
            f"{self._csomagtarto_meret} L csomagtartó | "
            f"{self._hatotav} km hatótáv"
        )

    def __str__(self) -> str:
        return self.leiras(reszletes=True)
