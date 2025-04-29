import pandas as pd
from Classes.Times import Time
from Classes.Rating import Rating
from Classes.Partida import Partida
from Classes.Parser import Parser

csv_partidas = pd.read_csv('partidas.csv')
csv_times = pd.read_csv('clubes.csv')
times: list[Time] = []

rating = Rating()
parser = Parser()
for i in csv_times.itertuples():
    times.append(Time(i.nome, i.rating))

row_lists = []
PARDITAS_TO_LOG = 10 # each 10 partidas it will save the resulto to log
c = PARDITAS_TO_LOG

for i in csv_partidas.itertuples():
    timeA = [t for t in times if i.timeA == t][0]
    timeB = [t for t in times if i.timeB == t][0]

    partida = Partida(timeA, timeB, parser.result(i.resultado), parser.goals(i.resultado))
    partida.atribute_new_rating()

    if c == 0:
        dict1 = {
            time.name: time.rating for time in times
        }

        row_lists.append(dict1)

        c = PARDITAS_TO_LOG
    
    c -= 1

print()
print()
print()

log = pd.DataFrame(row_lists)
print(log)

# for i in sorted(times, reverse=True):
#     print(i)