# Autókölcsönző Rendszer

Ez a projekt egy egyszerű autókölcsönző rendszert valósít meg, amelyben autókat lehet bérelni, lemondani a bérlést, és megtekinteni az aktuális bérlések listáját.

## Általános elvárások

- Pythonban készítsétek a vizsgafeladatot.
- A kész projektet töltsétek fel a saját GitHub repositorytokban. 
  - Figyeljetek rá hogy a repó láthatósága PUBLIC legyen!
- A feladatot beadni a Neptunban a "Kötelező project feladat" elnevezéső feladatban kell. 
  - Készíts egy NEPTUNKOD.docx fájlt, amibe másold bele az előbbi pontban írt github repository linkjét. Ezt a fájlt töltsd fel!
- **Eredeti határidő: 2026.05.24 23:59:59.**
- **Frissített határidő (közölt módosítás): 2026.12.06 23:59:59.**
- Elküldés előtt tegyétek meg a következőket:
  - Egy browser incognito ablakában nézzétek meg az elküldendő GitHub repositoryt (látható, fent van az utolsó commit is).
  - Clone-ozzátok ki a repositoryt PyCharm-ban, és nézzétek meg, hogy futtatható-e (így fogom én is tesztelni, el kell induljon a projekt, hogy értékelni tudjam).
- Elevator pitch videó készítése
  - Rövid 2 nagyon max 3 perces videó ahol bemutatjátok az elkészült project feladatot. 

## Fő osztályok

- **Auto (absztrakt osztály):** Definiálja az autó alapvető attribútumait (rendszám, típus, bérleti díj).
- **Személyauto:** A személyautók specifikus attribútumait tartalmazó osztály.
- **Teherauto:** A teherautók specifikus attribútumait tartalmazó osztály.
- **Autokolcsonzo:** Tartalmazza az autókat és saját attribútumot is, például a kölcsönző nevét.
- **Berles:** Az autóbérléshez szükséges osztály, amely egy autó bérlését egy napra tárolja.

## Funkciók

- **Autó bérlése:** Az autók bérelhetők egy napra, és a bérlés visszaadja az árat.
- **Bérlés lemondása:** A felhasználó lemondhatja a meglévő bérlését.
- **Bérlések listázása:** Az összes aktuális bérlés listázása.

## További elvárt funkciók
- Ahol csak lehet használj non-public attribútumokat, szükség esetén írj hozzá getter/setter-t.
- Használj hibakezelést.

## Adatvalidáció

- Ellenőrzi, hogy az autó elérhető-e bérlésre, és a bérlési dátum érvényes-e.
- Biztosítja, hogy csak létező bérléseket lehessen lemondani.

## Felhasználói interfész

- Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
  - Autó bérlése
  - Bérlés lemondása
  - Bérlések listázása

## Előkészítés

A rendszer indulásakor egy autókölcsönző áll rendelkezésre, amely 3 autót és 4 bérlést tartalmaz. Ezt az adatot a program indulásakor előre betöltjük a rendszerbe, így a felhasználó már használatra kész rendszert kap.
