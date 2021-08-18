# scripts-query-chess-api

Set of user scripts making use of Lichess API

## Extract game duration info from Lichess using gettimesfromlichess.py


The game duration can be derived from the difference of the tags createdAt and lastMoveAt obtained by querying the Lichess game API (only 1 game at a time)

1. A personal API token is to be requested from Lichess: https://lichess.org/account/oauth/token

2. Lichess game IDs (for exemple lth9JO0D) to be collected and placed in a file (1 ID per line). They can be collecting by parsing the PGN that can be obtained from https://lichess.org/@/-user-/download for instance for collecting the play time of a specific -user-.

3. Initialize the output file `cp gettimesfromlichess_header.csv newtimeextract.csv` (optional)

4. Run the script with the token, input file and output file `./gettimesfromlichess.py -TOKEN- -INPUT_FILE- >> newtimeextract.csv`. The extraction will run on the Lichess API at a rate of around 1 game per second.
