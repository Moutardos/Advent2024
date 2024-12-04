import sys

def extract_steps(line_tab):
    tab_step = [int(line_tab[i]) - int(line_tab[i + 1]) for i in range(len(line_tab) - 1)]
    return (tab_step)

def is_sorted(tab_step):
    return (
        all(
            step < 0 for step in tab_step
        ) or all(
            step > 0 for step in tab_step
        )
    )

def check_step(tab_step, min = 1, max = 3):
    return (
        all(
            abs(step) >= min and abs(step) <= max for step in tab_step
        )
    )

def is_safe(line_tab):
    tab_step = extract_steps(line_tab)
    return (is_sorted(tab_step) and check_step(tab_step))

def is_dampener_safe(line_tab):
    warning = 0
    while not is_safe(line_tab):
        warning += 1
        if warning > 1:
            return False
        original_tab = line_tab.copy()
        for i in range(len(original_tab)):
            line_tab = original_tab.copy()
            line_tab.pop(i)
            if is_safe(line_tab):
                return True
        return False
    return True

def part_one(report):
    safe_sum = sum([is_safe(line.split()) for line in report])
    print(f"There is {safe_sum} reports that are safe")

def part_two(report):
    safe_sum = sum([is_dampener_safe(line.split()) for line in report])
    print(f"There is {safe_sum} reports that are dampener safe")

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        filename = "input"
    with open(filename, mode="r", encoding="utf-8") as file:
        lines  = file.readlines()
        part_one(lines)
        part_two(lines)
