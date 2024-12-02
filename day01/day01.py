import sys

def get_diff_sum(tab1, tab2):
    return (sum([abs(tab1[i] - tab2[i]) for i in range(len(tab1))]))

def get_simi_score(tab1, tab2):
    set_tab1 = set(tab1)
    return (sum([tab2.count(number) * number for number in set_tab1]))

def extract_tabs(filename):
    file = open(filename)
    tab1 = []
    tab2 = []
    for line in file:
        (x, y) = line.split()
        tab1.append(int(x))
        tab2.append(int(y))
    return (tab1, tab2)


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        filename = "input"
    tab1, tab2 = extract_tabs(filename)
    tab1.sort()
    tab2.sort()
    print (f"The \"sum diff\" for {filename} is {get_diff_sum(tab1, tab2)}")
    print (f"The \"similarity score\" for {filename} is {get_simi_score(tab1, tab2)}")
