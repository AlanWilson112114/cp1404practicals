import csv

DATA_FILE = 'wimbledon.csv'
COUNTRY_IDX = 1
NAME_IDX = 2


def main():
    name_to_wins, countries_won = extract_data(DATA_FILE)
    display_champions_data(name_to_wins)
    display_countries_data(countries_won)


def extract_data(file_path):
    name_to_wins = {}
    countries_won = []
    with open(file_path, "r", encoding="utf-8-sig") as data_file:
        csv_reader = csv.reader(data_file)
        next(csv_reader)
        for line in csv_reader:
            country = line[COUNTRY_IDX]
            name = line[NAME_IDX]
            if country not in countries_won:
                countries_won.append(country)
            if name in name_to_wins:
                name_to_wins[name] += 1
            else:
                name_to_wins[name] = 1
    return name_to_wins, countries_won


def display_champions_data(name_to_wins):
    print(f"Wimbledon Champions:")
    for name, wins in name_to_wins.items():
        print(f"{name} {wins}")


def display_countries_data(countries_won):
    countries_won.sort()
    print(f"\nThese {len(countries_won)} countries have won Wimbledon: ")
    print(', '.join(countries_won))


main()
