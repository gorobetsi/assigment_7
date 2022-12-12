import sys

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
        file.write(result_after1)

#c = task1("data_file.tsv", "USA","1936")

#print(c)


#args = sys.argv
# if args[2] == "-medals":
#     filename = args[args.index("-filename") + 1]
#     country = args[args.index("-country") + 1]
#     year = args[args.index("-year") + 1]
#     result = task1(filename, country, year)
#     print(result)
#     if args[4] == "-output":
#         file_for_output = args[5]
#         for_output(file_for_output, result)

args = sys.argv
if args[2] == "-medals":
    filename = args[1]
    country = args[3]
    year = args[4]
    result = task1(filename, country, year)
    print(result)

