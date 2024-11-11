from player_reader import PlayerReader
from player_stats import PlayerStats

from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

def main():
    # url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    # q = PlayerReader(url)
    # w = PlayerStats(q)
    # e = w.top_scorers_by_nationality('FIN')

    # print('players from finland\n')

    # for player in e:
    #     print(player)

    
    aa = '2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25'.split(', ')
    ab = ['AUS', 'AUT', 'BLR', 'CAN', 'CZE', 'DEN', 'FIN', 'FRA', 'GBR', 'GER', 'LAT', 'NED', 'NOR', 'POL', 'RUS', 'SLO', 'SUI', 'SVK', 'SWE', 'USA', 'UZB', 'q']


    b = Prompt.ask('Select season', choices=aa)

    q = f'https://studies.cs.helsinki.fi/nhlstats/{b}/players'
    w = PlayerReader(q)

    while True:
        c = Prompt.ask('Select nationality', choices=ab)

        if c == 'q':
            break

        e = PlayerStats(w)
        r = e.top_scorers_by_nationality(c)

        print()

        t = Table(title=f'top scorers of {c} for season {b}')

        t.add_column('name')
        t.add_column('team', style='purple')
        t.add_column('goals')
        t.add_column('assists')
        t.add_column('points', style='green')

        for x in r:
            t.add_row(x.name, x.d, str(x.b), str(x.c), str(x.bc))

        y = Console()
        y.print(t)

        print()

if __name__ == "__main__":
    main()
