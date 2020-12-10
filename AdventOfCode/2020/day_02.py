
def test_password_old(target_ltr: str, low: int, high: int, password: str):
    return low <= password.count(target_ltr) <= high


def test_password_new(target_ltr: str, poz1: int, poz2: int, password: str):
    return (poz1 <= len(password) and poz2 <= len(password)) and \
           (password[poz1-1] == target_ltr) ^ (password[poz2-1] == target_ltr)


def procline(raw_line: str) -> list:
    nums_raw, ltr_raw, password_raw = raw_line.split(" ")
    low, high = tuple(map(int, nums_raw.split("-")))
    ltr = ltr_raw[0]
    password = password_raw.strip()

    return ltr, low, high, password


if __name__ == "__main__":
    with open("inputs/day_02.in") as raw_input:
        input_lines = list(map(procline, raw_input.read().split('\n')))

    valid_new, valid_old = 0, 0
    for line in input_lines:
        valid_new += test_password_new(*line)
        valid_old += test_password_old(*line)
        print(f"Is line {str(line):40} valid ? {test_password_new(*line)}")

    print(f"Found valid: {valid_old}, new rule: {valid_new}")
