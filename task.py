import sys


def task1(filename, country, year):
    head = None
    first_line = True
    gold = 0
    silver = 0
    bronze = 0
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if first_line:
                head = data
                first_line = False
                continue
            medal = data[head.index("Medal")]
            if country == data[head.index("NOC")] and year == data[head.index("Year")]:
                if medal == "Gold":
                    gold += 1
                    continue
                elif medal == "Silver":
                    silver += 1
                    continue
                elif medal == "Bronze":
                    bronze += 1
                    continue


def main():
    args = sys.argv
    if args[1] == "-medals":
        filename = args[args.index("-filename") + 1]
        country = args[args.index("-country") + 1]
        year = args[args.index("-year") + 1]
        task1(filename, country, year)
