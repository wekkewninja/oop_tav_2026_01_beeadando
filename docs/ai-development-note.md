# Fejlesztési megjegyzés — CASE + TARS

A projekt fejlesztése során egy saját tervezésű, ágens alapú AI rendszer — **CASE + TARS** — nyújtott támogatást. A rendszer a teljes fejlesztési életciklust lefedi:

- **CASE** *(Collective Agent-based Strategy and Elicitation)* — a követelmények összegyűjtéséért, szervezéséért és Feature Brief formájában való csomagolásáért felelős. A rendszer négy specializált ágensből áll: az **Intake Collector** heterogén forrásokból (szöveg, ötletek, feladatleírások, prezentációk, pdf-ek) normalizált követelménylistát állít össze; az **Organizer** deduplikálja, osztályozza és csoportokba rendezi a tételeket; a **Prioritizer** súlyozza és rangsorolja a csoportokat hat dimenzió mentén (üzleti érték, komplexitás, kockázat, függőségek, határidő, erőforrásigény); a **Package Creator** a jóváhagyott rangsorból Feature Brief dokumentumokat készít TARS számára. Egyetlen, jól definiált ötlet esetén a teljes pipeline megkerülhető a **Fast-Path** móddal, amely egyetlen lépésben generál Feature Brief-et.
- **TARS** *(Task-oriented Agent-based oRchestration System)* — a Feature Brief alapján végigvezeti a fejlesztést egy strukturált, 8 lépéses életcikluson. A rendszer specializált ágensekből áll, amelyek egymást követő fázisokban dolgoznak: az **Analyst** pontosítja a követelményeket és PRD-t készít, az **Architect** megtervezi a megoldás struktúráját, a **Developer** implementálja a kódot, a **QA** teszteli és átvizsgálja azt, a **Security Engineer** biztonsági szempontból értékeli, a **Documentation Writer** dokumentációt készít, a **DevOps** az üzembe helyezést felügyeli, a **Maintainer** pedig a tanulságokat rögzíti visszajelzésekből. Minden fázis kimenetét a felhasználó hagyja jóvá, mielőtt a következő elkezdődik.

Agentic módban működve a rendszer képes volt önállóan értelmezni a követelményeket, tervezni az architektúrát, implementálni a kódot, és dokumentációt generálni — mindezt emberi jóváhagyással a kritikus döntési pontokon.

---

## Felhasznált fázisok

| Fázis | Rendszer | Lépés | Emberi szerep | Használva |
|---|---|---|---|---|
| C1 | CASE | Intake — követelmények begyűjtése | Követelmények digitalizálása | ✗ |
| C2 | CASE | Organize — csoportosítás, prioritizálás előkészítése | — | ✗ |
| C3 | CASE | Prioritize — rangsorolás | — | ✗ |
| C4 | CASE | Package / **Fast-Path** — Feature Brief elkészítése | Jóváhagyás | ✓ |
| T1 | TARS | Követelményelemzés | Kérdések megválaszolása | ✓ |
| T2 | TARS | Termékkövetelmény-dokumentum (PRD) | Jóváhagyás | ✓ |
| T3 | TARS | Architektúra tervezés | Jóváhagyás | ✓ |
| T4 | TARS | Implementációs tervezés | Jóváhagyás | ✓ |
| T5 | TARS | Implementáció | Kód átvizsgálása | ✓ |
| T6 | TARS | Tesztelés | Eredmények áttekintése | ✓ |
| T7 | TARS | Kód- és biztonsági review | Átvizsgálás | ✓ |
| T8 | TARS | Dokumentáció | Jóváhagyás | ✓ |

> A CASE teljes pipeline (C1–C3) nem volt szükséges, mivel egyetlen, jól definiált ötletből indultunk. A **Fast-Path** (C4) közvetlenül Feature Brief-et generált és adta át TARS-nak.

---

Az AI rendszer kizárólag fejlesztési segédeszközként működött — minden kód, tervezési döntés és dokumentum emberi jóváhagyással készült és kerül beadásra.
