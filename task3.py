import argparse

parser = argparse.ArgumentParser(description='parser')
parser.add_argument("--overall", nargs='+', required=False)
parser.add_argument("filename", type=str, help='')
args = parser.parse_args()
overall = args.overall
filename = args.filename


def task3(filename,overall):
    first_line = True
    for country in overall:
        d = {}
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("\t")
                year = data[9]
                if first_line:
                    first_line = False
                    continue
                if country == data[6] and (data[-1] != "NA"):
                    if year not in d:
                        d[year] = 1
                    else:
                        d[year] += 1
        print(max(d, key=d.get), max(d.values()))

task3(filename,overall)
