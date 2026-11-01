from abc import ABC, abstractmethod


class Auto(ABC):
    """Absztrakt alaposztály minden autótípushoz."""

    def __init__(self, rendszam: str, berleti_dij: float):
        self._rendszam = rendszam
        self._tipus: str = ""  # Subclass sets this in its __init__
        self._berleti_dij = berleti_dij

    # --- rendszam ---
    def get_rendszam(self) -> str:
        return self._rendszam

    def set_rendszam(self, rendszam: str) -> None:
        if not rendszam or not isinstance(rendszam, str):
            raise ValueError("A rendszám nem lehet üres.")
        self._rendszam = rendszam

    # --- tipus (read-only) ---
    def get_tipus(self) -> str:
        return self._tipus

    # --- berleti_dij ---
    def get_berleti_dij(self) -> float:
        return self._berleti_dij

    def set_berleti_dij(self, berleti_dij: float) -> None:
        if berleti_dij <= 0:
            raise ValueError("A bérleti díj pozitív szám kell legyen.")
        self._berleti_dij = berleti_dij

    @abstractmethod
    def leiras(self, reszletes: bool = True) -> str:
        """Szöveges reprezentáció. reszletes=False: csak rendszám + díj."""
        pass

    def __str__(self) -> str:
        return self.leiras(reszletes=True)
