class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def _kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            if i >= len(b):
                break
            b[i] = a[i]
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception('Kapasiteetti ei ole int tai on negatiivinen')
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception('Kasvatuskoko ei ole int tai on negatiivinen')
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True

        return False

    def lisaa(self, lisattava):
        if not self.kuuluu(lisattava): # n ei kuulu listaan
            self.lukujono[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono): # ei mahdu enempää
                edellinen_lukujono = self._luo_lista(self.alkioiden_lkm)
                self._kopioi_lista(self.lukujono, edellinen_lukujono)

                self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self._kopioi_lista(edellinen_lukujono, self.lukujono)

            return True

        return False

    def poista(self, poistettava):
        for i in range(0, self.alkioiden_lkm):
            if poistettava == self.lukujono[i]:
                self.lukujono[i] = 0

                for j in range(i, self.alkioiden_lkm - 1): # siirretään vasemmalle
                    edellinen = self.lukujono[j]
                    self.lukujono[j] = self.lukujono[j + 1]
                    self.lukujono[j + 1] = edellinen

                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        self._kopioi_lista(self.lukujono, taulu)

        return taulu

    @staticmethod
    def yhdiste(a, b):
        intjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            intjoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            intjoukko.lisaa(b_taulu[i])

        return intjoukko

    @staticmethod
    def leikkaus(a, b):
        intjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    intjoukko.lisaa(b_taulu[j])

        return intjoukko

    @staticmethod
    def erotus(a, b):
        intjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            intjoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            intjoukko.poista(b_taulu[i])

        return intjoukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return '{}'
        else:
            tuotos = '{'
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += f'{str(self.lukujono[i])}, '
            tuotos += f'{str(self.lukujono[self.alkioiden_lkm - 1])}{"}"}'

            return tuotos
