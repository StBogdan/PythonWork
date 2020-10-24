def determine_lucky_strings(text: str) -> int:
    # print(f"Looking at string {text}")
    pointer = 0
    kicks = 0
    total_lucky = 0
    while pointer < len(text): 
        if text[pointer: pointer + 4] == "KICK":
            kicks += 1
        elif text[pointer: pointer + 5] == "START":
            total_lucky += kicks
        pointer += 1
    return total_lucky


if __name__ == "__main__":
    n = int(input())
    res_list = []
    for i in range(n):
        input_str = input()
        res = determine_lucky_strings(input_str)
        res_list.append("Case #" + str(i+1) + ": " + str(res))
    print("\n".join(res_list))
