import argparse

parser = argparse.ArgumentParser(description='parser')
parser.add_argument("--overall", nargs='+', required=False)
parser.add_argument("filename", type=str, help='')
args = parser.parse_args()
overall = args.overall
filename = args.filename


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


task3(filename,overall)
