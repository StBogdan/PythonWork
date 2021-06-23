if __name__ == "__main__":
    with open("inputs/day_13.in") as raw_input:
        input_lines = raw_input.read().split('\n')

    for i, line in enumerate(input_lines):
        if "mask" in line:
            input_lines[i] = ("mask", line.split('=')[1].strip())
        else:
            mem_alloc, value = line.split('=')
            mem_location = mem_alloc.split("[")[1][:-2]
            input_lines[i] = ("mem", int(mem_location), value.strip())

    print(input_lines)