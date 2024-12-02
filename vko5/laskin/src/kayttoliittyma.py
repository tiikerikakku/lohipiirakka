from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._cmd = {
            Komento.SUMMA: self._summa,
            Komento.EROTUS: self._erotus,
            Komento.NOLLAUS: self._nollaa,
            Komento.KUMOA: self._kumoa
        }

        self._before = 0

    # this doesn't quite follow the given example
    # but it works...
    # and I've got rid of the "horrifying" if-statements

    def _summa(self, arvo):
        self._before = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(arvo)

    def _erotus(self, arvo):
        self._before = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(arvo)

    def _nollaa(self, arvo):
        self._before = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def _kumoa(self, arvo):
        c = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.aseta_arvo(self._before)
        self._before = c

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        self._cmd[komento](arvo)

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
