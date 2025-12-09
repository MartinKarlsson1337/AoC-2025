
if __name__ == '__main__':
    with open('day7/day7.txt') as f:
        input_puzzle = f.readlines()

    iter_lines = iter(input_puzzle)
    first_row = next(iter_lines)
    row_width = len(first_row)

    beams = [0] * row_width
    print(beams)
    beam_start_x = first_row.index('S')
    beams[beam_start_x] = 1

    split_count = 0

    for row in iter_lines:
        new_beams = [0] * row_width
        for col_index, beam in enumerate(beams):
            if beam == 0:
                continue

            c = row[col_index]

            if c == '^':
                split_count += 1
                new_beams[col_index - 1] += beam
                new_beams[col_index + 1] += beam
            else:
                new_beams[col_index] += beam

        beams = new_beams

    print("Part 1:", split_count)
    print("Part 2:", sum(beams))