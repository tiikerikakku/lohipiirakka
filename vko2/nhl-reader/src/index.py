from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    q = PlayerReader(url)
    w = PlayerStats(q)
    e = w.top_scorers_by_nationality('FIN')

    print('players from finland\n')

    for player in e:
        print(player)

if __name__ == "__main__":
    main()
