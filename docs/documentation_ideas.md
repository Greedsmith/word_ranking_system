# Aanbevolen Documentatie

Deze documenten zouden het project duidelijker en professioneler maken.

## 1. Technisch ontwerp

Beschrijf hoe het project is opgebouwd:

- welke modules er zijn
- welke functie elke module heeft
- hoe data door het systeem stroomt
- waarom de score op deze manier is opgebouwd

## 2. Score-uitleg

Maak een apart document waarin precies staat hoe de moeilijkheidsscore werkt.

Handige onderdelen:

- overzicht van alle scorefactoren
- gewicht per factor
- voorbeelden van woorden met berekening
- uitleg waarom sommige factoren belangrijk zijn voor laaggeletterde lezers

## 3. Gebruikershandleiding

Beschrijf stap voor stap hoe iemand het project gebruikt.

Bijvoorbeeld:

- waar `.txt`-bestanden moeten staan
- hoe je het script uitvoert
- waar de resultaten verschijnen
- hoe je CSV-bestanden opent in Excel
- hoe pagina's gescheiden kunnen worden met `=== pagina ===`

## 4. Interpretatiehandleiding

Leg uit hoe iemand de output moet lezen.

Belangrijke vragen:

- wat betekent een hoge woordscore?
- wanneer is een pagina moeilijk?
- hoe betrouwbaar is de A1-C2-inschatting?
- wat betekent het percentage moeilijke woorden?

## 5. Validatieplan

Omdat de score nu een heuristiek is, is het waardevol om te beschrijven hoe je die later kunt testen.

Ideeen:

- vergelijk uitkomsten met teksten die al een bekend taalniveau hebben
- laat taalexperts enkele woorden beoordelen
- vergelijk moeilijke woorden met feedback van laaggeletterde lezers
- pas gewichten aan op basis van echte voorbeelden

## 6. Uitbreidingsplan

Beschrijf welke functies later toegevoegd kunnen worden.

Mogelijke uitbreidingen:

- lijst met veelvoorkomende makkelijke woorden
- lijst met vaktaal of moeilijke leenwoorden
- uitleg per woord waarom het moeilijk is
- webinterface voor uploaden van teksten
- export naar Excel met kleuren
- automatische suggesties voor makkelijkere woorden

## 7. Testdocumentatie

Leg vast hoe je controleert dat het project blijft werken.

Voorbeelden:

- test of woorden goed worden herkend
- test of `sch` en `ch` goed scoren
- test of pagina's goed worden gesplitst
- test of lege inputmappen geen fout geven
- test of outputbestanden worden aangemaakt

