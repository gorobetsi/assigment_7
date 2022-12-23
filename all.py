import argparse

parser = argparse.ArgumentParser(description='parser')
parser.add_argument("filename", type=str)
parser.add_argument("action", type=str)
parser.add_argument("--country", type=str)
parser.add_argument("--countries", nargs='+', required=False)
parser.add_argument("--year", type=str)
args = parser.parse_args()
filename = args.filename


def count_medals(medals):
    gold = 0
    silver = 0
    bronze = 0
    #sum_medals = 0
    for medal in medals:
        if medal == "Gold\n":
            gold += 1
        elif medal == "Silver\n":
            silver += 1
        elif medal == "Bronze\n":
            bronze += 1
    #sum_medals = gold + silver + bronze
    print("gold=", gold)
    print("silver=", silver)
    print("bronze=", bronze)


def result_for1(list):
    list_with_names = []
    time = 0
    for items in list:
        item1 = items.split("\t")
        if time > 9:
            break
        elif item1[14] != "NA\n":
            list_with_names.append([item1[1], item1[12], item1[14]])
            time = time + 1
    for name in list_with_names:
        print(name[0], "-", name[1], "-", name[2])


def task1(filename, country, year):
    head = None
    first_line = True
    all_line = []
    medals = []
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if first_line:
                head = data
                first_line = False
                continue

            if country == data[head.index("NOC")] and year == data[head.index("Year")]:
                all_line.append(line)
                medal1 = line.split("\t")[14]
                medals.append(medal1)
        if 0 < len(medals) < 10:
            print("This country has less then 10 medals in this year")
        elif not medals:
            print("Try again. This country does not exist or there was no olympics this year")
        names = result_for1(all_line)
        show_medals = count_medals(medals)

        return names

def for_output(file, result_after1):
    with open(file, "w") as file:
        file.write(str(result_after1))

    if args[4] == "-output":
        file_for_output = args[5]
        for_output(file_for_output, result)


def total(filename, year):
    head = None
    first_line = True
    countries = {}
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            country_name = data[6]
            if first_line:
                head = data
                first_line = False
                continue
            if str(year) == data[head.index("Year")] and data[14] != "NA":
                if str(country_name) not in countries:
                    countries[str(country_name)] = [0,0,0]
                if data[14] == "Gold":
                    countries[str(country_name)][0] += 1
                elif data[14] == "Silver":
                    countries[str(country_name)][1] += 1
                elif data[14] == "Bronze":
                    countries[str(country_name)][2] += 1
        sort_countries = sorted(countries.items(), key=lambda i: sum(i[1]), reverse=True)
        for n in sort_countries:
            print(n[0], ":", "Gold -", n[1][0], "Silver -", n[1][1], "Bronze -", n[1][2], "Total-", sum(n[1]))

def task3(filename,overall):
    first_line = True
    d = dict()
    for country in overall:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                year = data[9]
                if first_line:
                    first_line = False
                    continue
                if country == data[6] and (data[-1] != "NA"):
                    if country not in d:
                        d[country] = dict()
                    if year not in d[country]:
                        d[country][year] = 0
                    d[country][year] += 1
    for key, value in d.items():
        max_key = list(value.keys())[0]
        for k, val in value.items():
            if val > value[max_key]:
                max_key = k
        print(f"the max medals in year: {key, max_key, value[max_key]}")
    for key1, value1 in d.items():
        min_key = list(value1.keys())[0]
        for k1, val1 in value1.items():
            if val1 < value1[min_key]:
                min_key = k1
        print(f"the min medals in year: {key1, min_key, value1[min_key]}")

def interactive(filename):
    first_line = True
    d = dict()
    user_country = input("please enter NOC country which you choose(USA or FIN..):\n")
    print(user_country)
    with open(filename, "r") as file:
        best_year = 0
        Olymp = []
        worst_year = 0
        year1 = 2023
        best_result = 0
        worst_result = 100000
        Gold = 0
        Silver = 0
        Bronze = 0
        city1 = ""
        for line in file:
            data = line.strip().split("\t")
            if first_line:
                first_line = False
                continue
            year = data[9]
            medal = data[-1]
            city = data[11]
            if user_country == data[7] or user_country == data[6]:
                if year not in Olymp:
                    Olymp.append(year)
                if year not in d:
                    d[year] = 0
                if year1 > int(data[9]):
                    year1 = int(data[9])
                    city1 = city
                if medal == "NA\n" or medal != "NA":
                    d[year] += 1
                    if medal == "Gold":
                        Gold += 1
                    elif medal == "Silver":
                        Silver += 1
                    elif medal == "Bronze":
                        Bronze += 1
    for year in d:
        if d[year] > best_result:
            best_result = d.get(year)
            best_year = year
    for year in d:
        if d[year] < worst_result:
            worst_result = d.get(year)
            worst_year = year
    print(f"the best year - {best_year} - {best_result} medals")
    print(f"the worst year - {worst_year} - {worst_result} medals")
    print(f"average gold {Gold//len(Olymp)} ")
    print(f"average silver {Silver//len(Olymp)} ")
    print(f"average bronze {Bronze//len(Olymp)} ")
    print(city1)
    print(year1)

def main():
    if args.action == "medals":
        country = args.country
        year = args.year
        return task1(filename, country, year)
    elif args.action == "total":
        year = args.year
        return total(filename, year)
    elif args.action == "overall":
        overall = args.countries
        return task3(filename, overall)
    elif args.action == "interactive":
        return interactive(filename)

print (main())
