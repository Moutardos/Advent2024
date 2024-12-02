import sys

def is_safe(line):
    tab = line.split()
    tab_step = [int(tab[i]) - int(tab[i + 1]) for i in range(len(tab) - 1)]
    print(tab_step)
    return (is_sorted(tab_step) and check_step(tab_step, 1, 3))

def is_sorted(tab_step):
    return (
        all(
            step < 0 for step in tab_step
        ) or all(
            step > 0 for step in tab_step
        )
    )

def check_step(tab_step, min, max):
    return (
        all(
            abs(step) >= min and abs(step) <= max for step in tab_step
        )
    )

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        filename = "input"
    with open(filename, mode="r", encoding="utf-8") as file:
        safe_sum = sum([is_safe(line) for line in file])
        print(f"There is {safe_sum} reports that are safe")

    