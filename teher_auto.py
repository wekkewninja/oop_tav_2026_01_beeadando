from auto import Auto


class Teherautó(Auto):
    """Teherautót reprezentáló osztály."""

    def __init__(
        self,
        rendszam: str,
        berleti_dij: float,
        utas_szam: int,
        terhebiras: float,
        sebesseg_korlat: int,
        hatotav: int,
        rakodter_hossz: int,
        rakodter_magassag: int,
        rakodter_szelesseg: int,
    ):
        super().__init__(rendszam, berleti_dij)
        self._tipus = "Teherautó"
        self._utas_szam = utas_szam
        self._terhebiras = terhebiras
        self._sebesseg_korlat = sebesseg_korlat
        self._hatotav = hatotav
        self._rakodter_hossz = rakodter_hossz
        self._rakodter_magassag = rakodter_magassag
        self._rakodter_szelesseg = rakodter_szelesseg

    # --- utas_szam ---
    def get_utas_szam(self) -> int:
        return self._utas_szam

    def set_utas_szam(self, utas_szam: int) -> None:
        if utas_szam < 1:
            raise ValueError("Az utasszám legalább 1 kell legyen.")
        self._utas_szam = utas_szam

    # --- terhebiras ---
    def get_terhebiras(self) -> float:
        return self._terhebiras

    def set_terhebiras(self, terhebiras: float) -> None:
        if terhebiras <= 0:
            raise ValueError("A teherbírás pozitív szám kell legyen.")
        self._terhebiras = terhebiras

    # --- sebesseg_korlat ---
    def get_sebesseg_korlat(self) -> int:
        return self._sebesseg_korlat

    def set_sebesseg_korlat(self, sebesseg_korlat: int) -> None:
        if sebesseg_korlat <= 0:
            raise ValueError("A sebességkorlát pozitív szám kell legyen.")
        self._sebesseg_korlat = sebesseg_korlat

    # --- hatotav ---
    def get_hatotav(self) -> int:
        return self._hatotav

    def set_hatotav(self, hatotav: int) -> None:
        if hatotav <= 0:
            raise ValueError("A hatótáv pozitív szám kell legyen.")
        self._hatotav = hatotav

    # --- rakodter meretek ---
    def get_rakodter_hossz(self) -> int:
        return self._rakodter_hossz

    def set_rakodter_hossz(self, hossz: int) -> None:
        if hossz <= 0:
            raise ValueError("A rakodótér hossza pozitív szám kell legyen.")
        self._rakodter_hossz = hossz

    def get_rakodter_magassag(self) -> int:
        return self._rakodter_magassag

    def set_rakodter_magassag(self, magassag: int) -> None:
        if magassag <= 0:
            raise ValueError("A rakodótér magassága pozitív szám kell legyen.")
        self._rakodter_magassag = magassag

    def get_rakodter_szelesseg(self) -> int:
        return self._rakodter_szelesseg

    def set_rakodter_szelesseg(self, szelesseg: int) -> None:
        if szelesseg <= 0:
            raise ValueError("A rakodótér szélessége pozitív szám kell legyen.")
        self._rakodter_szelesseg = szelesseg

    def leiras(self, reszletes: bool = True) -> str:
        if not reszletes:
            return f"[Teherautó]   {self._rendszam} | {self._berleti_dij:,.0f} Ft/nap"
        return (
            f"[Teherautó]   {self._rendszam} | "
            f"{self._berleti_dij:,.0f} Ft/nap | "
            f"{self._utas_szam} utas | "
            f"{self._terhebiras:,.0f} kg teherbírás | "
            f"{self._sebesseg_korlat} km/h max | "
            f"{self._hatotav} km hatótáv | "
            f"rakodótér: {self._rakodter_hossz}×{self._rakodter_magassag}×{self._rakodter_szelesseg} cm"
        )

    def __str__(self) -> str:
        return self.leiras(reszletes=True)
