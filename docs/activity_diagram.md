# Activity Diagram

Dit diagram laat zien wat er gebeurt wanneer je `python rank_words.py` uitvoert.

```mermaid
flowchart TD
    A([Start]) --> B{Bestaan input- en outputmappen?}
    B -- Ja --> B0[Voorbereiding klaar]
    B -- Nee --> C0[Maak ontbrekende mappen aan]
    C0 --> B0

    B0 --> C[Lees .txt-bestanden uit input_txt]
    C --> D[Haal woorden uit de teksten]
    D --> E[Tel hoe vaak elk uniek woord voorkomt]
    E --> F[Bereken woordkenmerken]
    F --> G[Bereken woordscore]
    G --> H[Sorteer woorden van moeilijk naar makkelijk]
    H --> I[Schrijf word_ranking.csv en word_ranking.txt]

    B0 --> J[Lees .txt-bestanden uit input_pages]
    J --> K{Zijn er pagina's gevonden?}
    K -- Ja --> L[Splits teksten in pagina's]
    L --> M[Analyseer elke pagina]
    M --> N[Bereken paginascore]
    N --> O[Sorteer pagina's van moeilijk naar makkelijk]
    O --> P[Schrijf page_ranking.csv en page_ranking.txt]
    K -- Nee --> P

    B0 --> Q[Gebruik teksten uit input_txt voor tekstscore]
    Q --> R[Bereken gemiddelde woordscore]
    R --> S[Bereken gemiddelde zinslengte]
    S --> T[Bereken percentage moeilijke woorden]
    T --> U[Bereken tekstscore]
    U --> W[Schrijf story_level.csv en story_level.txt]

    I --> X([Einde])
    P --> X
    W --> X
```
