import sys

data_file = sys.argv[1]
year_set = set()    # set - used to store collections of data
with open(data_file, "r") as file:
    line = file.readline()
    while line != "":
        line = file.readline()
        split_line = line.split("\t")
        year = int(split_line[9])
        year_set.add(year)

year_list = sorted(year_set)
print(year_list)


parser = argparse.ArgumentParser(description='parser')
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--total", action="store_true", required=False)
parser.add_argument("--overall", nargs='+', required=False)
parser.add_argument("--filename", "--f", required=True)
parser.add_argument("--country", required=False)
parser.add_argument("--year", required=False)
parser.add_argument("--output", required=False)
parser.add_argument("--interactive", action="store_true", required=False)











# def total():
#     year = sys.argv[3]
#     for line in lines:
#         if year == line[9]:
#             print(line)
#
#
#
# def medals():
#     country = sys.argv[3]

# if mode == "-total":
#     total()
# else:
#     medals()







