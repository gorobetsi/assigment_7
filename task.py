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
    return gold, silver, bronze, sum_medals

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
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            if first_line:
                head = data
                first_line = False
                continue

            if country == data[head.index("NOC")] and year == data[head.index("Year")]:
                all_line.append(line)
        b = result_for1(all_line)


    return b

c = task1("data_file.tsv", "USA","1936")

print(c)

def main():
    args = sys.argv
    if args[1] == "-medals":
        filename = args[args.index("-filename") + 1]
        country = args[args.index("-country") + 1]
        year = args[args.index("-year") + 1]
        task1(filename, country, year)
