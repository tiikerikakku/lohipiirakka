# importit

from logger import logger
from summa import summa
from erotus import erotus

logger('aloitetaan')

x = int(input('luku 1: '))
y = int(input('luku 2: '))

print('summa on ' + summa(x, y))
print('erotus on ' + erotus(x, y))

logger('lopetetaan')

# tää loppuu nyt
