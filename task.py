import sys


def count_medals(medals, medals_line):
    gold = 0
    silver = 0
    bronze = 0
    if medal in medals:
        if medal == "Gold":
            gold += 1
        elif medal == "Silver":
            silver += 1
        elif medal == "Bronze":
            bronze += 1
        else:


def check_athletes(name)




def task1(filename, country, year):
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
