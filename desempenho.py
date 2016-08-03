

import pandas as pd, database as db
import sqlite3

conn = sqlite3.connect("cartola_fc")
df = pd.read_sql_query('SELECT * FROM players',conn)
print df
conn.close()

#id = 1 -> goleiro. 2 = lateral . 3 = zagueiro. 4 = meia. 5 = atacante. 6 = tecnico MEDIANUM=PONTUACAOMEDIA
# Status : 3 = Suspenso. 6 = nenhum. 7 = provavel. 5 = contundido. 2 = duvida

