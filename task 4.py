def interactive():
    first_line = True
    d = dict()
    user_country = input("please enter NOC country which you choose(USA or FIN..):\n")
    print(user_country)
    with open("data_file.tsv", "r") as file:
        best_year = 0
        Olymp=[]
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
                       # d[year] = dict()
                    d[year]=0 #gold, silver, bronze,total
                            # d[year]["Gold"] = 0
                        # d[year]["Silver"] = 0
                        # d[year]["Bronze"] = 0
                        # d[year]["total"] = 0
                if year1 > int(data[9]):
                    year1 = int(data[9])
                    city1 = city
                if medal != "NA\n" or medal != "NA":
                    d[year] += 1
                    if medal == "Gold":
                        Gold+= 1
                    elif medal == "Silver":
                        Silver+= 1
                    elif medal == "Bronze":
                        Bronze+= 1


   # result


    for year in d:
        if d[year] > best_result:
            best_result = d.get(year)
            best_year = year
    for year in d:
        if d[year] < worst_result:
            worst_result = d.get(year)
            worst_year = year

        # for year, results in d.items():
        #     if year1 > int(year):
        #         year1 = int(year)
        #         year1 = results[city]
        #         print(f"{year} - {results[city]}")
        # for medal, count in results.items():
        #     print(f"{medal} - {count}")
        #     if medal != "city":
        #         total_medals[medal] += count
        # if results["total"] > best_result:
        #     best_result = results["total"]
        #     best_year = year
        # if results["total"] < worst_result:
        #     worst_result = results["total"]
        #     worst_year = year
        # counter += 1
    print(f"the best year - {best_year} - {best_result} medals")
    print(f"the worst year - {worst_year} - {worst_result} medals")
    print(f"average gold {Gold//len(Olymp)} ")
    print(f"average silver {Silver//len(Olymp)} ")
    print(f"average bronze {Bronze//len(Olymp)} ")
    print(city1)
    print(year1)

interactive()
