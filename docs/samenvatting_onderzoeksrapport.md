# Samenvatting

Dit project onderzoekt hoe Nederlandse woorden en teksten automatisch kunnen worden gerangschikt op geschatte moeilijkheid voor laaggeletterde mensen. Het doel is om een praktisch hulpmiddel te ontwikkelen dat inzicht geeft in welke woorden, pagina's of volledige teksten lastig zijn om te lezen. Hiermee kan een schrijver, docent of onderzoeker sneller bepalen waar een tekst vereenvoudigd kan worden.

De moeilijkheid van woorden wordt berekend met een heuristisch scoresysteem. De score is gebaseerd op taalkenmerken, zoals woordlengte, het aantal tweeklanken, de aanwezigheid van `ch` of `sch`, het geschatte aantal lettergrepen, medeklinkerclusters en zeldzame letters zoals `q`, `x` en `y`. Elk kenmerk krijgt een bepaald gewicht. Een woord met meer moeilijke kenmerken krijgt daardoor een hogere score en wordt als moeilijker ingeschat.

Naast losse woorden kan het programma ook pagina's rangschikken. Hiervoor wordt een aparte invoermap gebruikt. Per pagina wordt gekeken naar, onder andere, de gemiddelde woordscore en het percentage moeilijke woorden. Daardoor kan zichtbaar worden welke pagina's binnen een tekst relatief lastig zijn.

Ook maakt het project een globale moeilijkheidsscore voor een volledige tekst. Deze score is gebaseerd op de gemiddelde woordscore, gemiddelde zinslengte en het percentage moeilijke woorden. De uitkomst is bedoeld als eerste indicatie van tekstmoeilijkheid en niet als officiele beoordeling.

Het project is opgebouwd in Python en verdeeld over meerdere herbruikbare modules. Hierdoor zijn onderdelen zoals woordherkenning, scoreberekening, pagina-analyse en rapportage apart aan te passen of uit te breiden. De resultaten worden opgeslagen als CSV- en tekstbestanden, zodat ze eenvoudig gelezen of verder geanalyseerd kunnen worden.

Een belangrijke beperking is dat het scoresysteem nog niet gevalideerd is met echte lezers of met bestaande leesbaarheidsdata. De huidige methode geeft daarom een onderbouwde schatting, maar geen definitief oordeel over leesbaarheid. Voor toekomstig onderzoek is het belangrijk om de uitkomsten te vergelijken met beoordelingen van taalexperts en laaggeletterde lezers.

Samenvattend biedt dit project een eerste technische basis voor het automatisch analyseren van tekstmoeilijkheid. Het maakt zichtbaar welke woorden en tekstonderdelen mogelijk lastig zijn en kan helpen bij het vereenvoudigen van teksten voor een laaggeletterd doelgroep.