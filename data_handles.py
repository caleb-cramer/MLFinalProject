import csv

def main():
    f = open("input_data/weatherAUS.csv", "r")
    reader = csv.reader(f)
    data = list(reader)
    temp = set()
    for row in data:
        temp.add(row[1])
    temp.remove("Location")
    locations = list(temp)
    locations.sort()

    lists = []

    for location in locations:
        temp = []
        for row in data:
            if location == row[1]:
                temp.append(row)
        lists.append(temp)

    f.close()

    for location in locations:
        filename = "input_data/" + location + "parsedData"
        g = open(filename, "w")
        for jj in range(len(lists[locations.index(location)])):
            g.writelines(lists[locations.index(location)][jj])
            g.write("\n")
        g.close()



if __name__ == "__main__":
    main()