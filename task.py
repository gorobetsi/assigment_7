import sys


def count_medals(medals):
    gold = 0
    silver = 0
    bronze = 0
    sum_medals = 0
    for medal in medals:
        if medal == "Gold":
            gold += 1
        elif medal == "Silver":
            silver += 1
        elif medal == "Bronze":
            bronze += 1
    sum_medals = gold + silver + bronze
    return sum_medals


def filename(medals):
    filenames = []
    for medal in medals:
        if medal == "Gold":
            filenames = filenames.append(Name)






def task1(country, year):
    head = None
    first_line = True
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if first_line:
                head = data
                first_line = False
                continue

            if country == data[head.index("NOC")] and year == data[head.index("Year")]:
                pass


def main():
    args = sys.argv
    if args[1] == "-medals":
        filename = args[args.index("-filename") + 1]
        country = args[args.index("-country") + 1]
        year = args[args.index("-year") + 1]
        task1(filename, country, year)
