# Woorden Moeilijkheid Rangschikken

Dit project rangschikt Nederlandse woorden, pagina's en volledige teksten op geschatte moeilijkheid.
Het is bedoeld als hulpmiddel om teksten beter te beoordelen voor laaggeletterde mensen.

## Wat het project maakt

Na het uitvoeren van het script staan deze bestanden in `output/`:

- `word_ranking.csv` en `word_ranking.txt`: unieke woorden uit `input_txt/`, gerangschikt van moeilijk naar makkelijk
- `page_ranking.csv` en `page_ranking.txt`: pagina's uit `input_pages/`, gerangschikt van moeilijk naar makkelijk
- `story_level.csv` en `story_level.txt`: inschatting van het Nederlandse taalniveau A1 tot C2 voor de teksten in `input_txt/`

## Mappen

- `input_txt/`: zet hier normale `.txt`-bestanden neer voor woordrangschikking en A1-C2-inschatting
- `input_pages/`: zet hier `.txt`-bestanden neer voor pagina-rangschikking
- `output/`: hier komen alle resultaten
- `woordenboek/`: herbruikbare Python-code, opgesplitst in kleinere modules

## Gebruik

Voer dit uit in de projectmap:

```bash
python rank_words.py
```

## Pagina's rangschikken

Voor pagina-rangschikking gebruikt de aparte map `input_pages/`.

Je kunt:

- een los `.txt`-bestand per pagina gebruiken
- meerdere pagina's in een `.txt`-bestand zetten en scheiden met `=== pagina ===`
- pagina's scheiden met een echt pagina-einde

Voorbeeld:

```text
Dit is pagina 1.

=== pagina ===

Dit is pagina 2.
```

## Woordscore

De huidige woordscore gebruikt deze regels:

```text
score = lengtepunten
      + (2 * aantal_tweeklanken)
      + 1.5 bij 'ch'
      + 2 bij 'sch'
      + extra punten bij 3 of meer lettergrepen
      + (2 * aantal medeklinkerclusters)
      + 1 bij q, x of y
```

`lengtepunten` is ongeveer de helft van de woordlengte. Lengte telt dus mee, maar minder zwaar dan in de eerste versie.

De gewichten staan in `woordenboek/config.py`.

## Taalniveau A1-C2

Het A1-C2-niveau is een schatting. Het project kijkt naar:

- gemiddelde woordscore
- gemiddelde zinslengte
- percentage moeilijke woorden

Daaruit maakt het script een `niveau_score`, die wordt omgezet naar:

- `A1`: zeer eenvoudig
- `A2`: eenvoudig
- `B1`: gemiddeld
- `B2`: redelijk moeilijk
- `C1`: moeilijk
- `C2`: zeer moeilijk

Deze inschatting is handig als eerste indicatie, maar het is geen officieel Europees Referentiekader-examen of gevalideerde taaltest.

## Code-opbouw

- `rank_words.py`: startscript
- `woordenboek/config.py`: mappen, tweeklanken en scoregewichten
- `woordenboek/text_utils.py`: tekstbestanden lezen, woorden vinden en pagina's splitsen
- `woordenboek/word_scoring.py`: woordkenmerken en woordscore
- `woordenboek/ranking.py`: rangschikking van woorden, pagina's en teksten
- `woordenboek/reports.py`: CSV- en tekstrapporten schrijven
