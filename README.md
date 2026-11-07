# GitHub trending verzamelaar

Elke ochtend leest een GitHub Action de trending-pagina van GitHub, werkt de sterren
bij van alle repo's die ooit trending waren en slaat alles op in `data/`.
Een dagelijkse Claude-taak leest deze data, schrijft per repo een korte uitleg in
het Nederlands, kiest een categorie en beoordeelt of het iets is voor Firecat.AI of
Firecat.Media. Het resultaat staat in het dashboard.

## Wat staat waar

| Bestand | Inhoud |
| --- | --- |
| `data/trending/JJJJ-MM-DD.json` | De trending-lijst van die dag |
| `data/repos.json` | Alle repo's die ooit trending waren, met datums |
| `data/stars.json` | Sterrenverloop per repo |
| `data/readme/` | Begin van de README van elke repo |
| `data/status.json` | Samenvatting van de laatste run |
| `ENRICH.md` | Regels voor de Nederlandse uitleg en de Firecat-beoordeling |

## Handmatig draaien

Tabblad Actions, workflow "Trending verzamelen", knop "Run workflow".

## Als het misgaat

Vindt de Action minder dan 5 repo's, dan stopt hij met een rode run en bewaart hij de
pagina in `data/debug/`. Meestal betekent dat dat GitHub de opbouw van de pagina heeft
veranderd en `parse_trending` in `scripts/collect.py` aangepast moet worden.
