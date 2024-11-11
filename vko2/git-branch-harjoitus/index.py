# importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger('aloitetaan')

x = int(input('luku 1: '))
y = int(input('luku 2: '))

print('summa on ' + summa(x, y))
print('erotus on ' + erotus(x, y))
print('tulo on ' + tulo(x, y))

logger('lopetetaan')

# tää loppuu nyt
