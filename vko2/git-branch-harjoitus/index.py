# importit

from logger import logger
from summa import summa
from erotus import erotus

logger('aloitetaan roska')

x = int(input('luku 1: '))
y = int(input('luku 2: '))

print(summa(x, y))
print(erotus(x, y))

logger('lopetetaan')

# tää loppuu nyt
