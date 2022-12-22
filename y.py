def task2(filename, year, total):
    if total:
        first_line = True
        countries = {}
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                country_name = data[6]
                if first_line:
                    first_line = False
                    continue
                if year == data[9] and data[14] != "NA" and data[6] != "Unified Team":
                    if str(country_name) not in countries:
                        countries[str(country_name)] = [0, 0, 0]
                    if data[14] == "Gold":
                        countries[str(country_name)][0] += 1
                    elif data[14] == "Silver":
                        countries[str(country_name)][1] += 1
                    elif data[14] == "Bronze":
                        countries[str(country_name)][2] += 1
            sort_countries = sorted(countries.items(), key=lambda x: sum(x[1]), reverse=True)
            for i in sort_countries:
                print(i[0], " ", i[1][0], "Gold", i[1][1], "Silver", i[1][2], "Bronze", " ", "Total", sum(i[1]))

print(task2("data_file.tsv", 1992, "total"))