# import sys

def total(filename, year):
    head = None
    first_line = True
    countries = {}
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split("\t")
            country_name = data[7]
            if first_line:
                head = data
                first_line = False
                continue
            if year == data[head.index("Year")] and data[14] != "NA\n":
                if str(country_name) not in countries:
                    countries[str(country_name)] = [0,0,0]
                if data[14] == "Gold\n":
                    countries[str(country_name)][0] += 1
                elif data[14] == "Silver\n":
                    countries[str(country_name)][1] += 1
                elif data[14] == "Bronze\n":
                    countries[str(country_name)][2] += 1
        print(countries)

print(total(data_file.tsv, 1972))
# args = sys.argv
# if args[2] == "-total":
#     filename = args[1]
#     year = args[3]
#     result = total(filename, year)
#     print(result)