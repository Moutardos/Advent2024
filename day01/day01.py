import sys

def extract_tabs(inputfile):
    tab_a = []
    tab_b = []
    with open(inputfile, mode="r", encoding="utf-8") as file:
        for line in file:
            (x, y) = line.split()
            tab_a.append(int(x))
            tab_b.append(int(y))
        file.close()
    return (tab_a, tab_b)

def part_one(inputfile, tab_a, tab_b):
    sum_diff =  sum(
                    abs(tab_a[i] - tab_b[i]) for i in range(len(tab_a))
                )
    print (f"The \"sum diff\" for {inputfile} is {sum_diff}")

def part_two(inputfile, tab_a, tab_b):
    set_a = set(tab_a)
    sim_score = sum(
                    tab_b.count(number) * number for number in set_a
                )
    print (f"The \"similarity score\" for {inputfile} is {sim_score}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input"
    tab1, tab2 = extract_tabs(filename)
    tab1.sort()
    tab2.sort()
    part_one(filename, tab1, tab2)
    part_two(filename, tab1, tab2)
