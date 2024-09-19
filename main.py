def main(filename):
    f = open(filename, 'r')
    lines = []
    for line in f:
        words = line.split(' ')
        while '' in words:
            words.remove('')
        lines.append(words)
    for i, line in enumerate(lines):
        if line[1] == '0.0':
            line[2:6] = lines[i + 1][2:6]
    linestrings = []
    for line in lines:
        linestring = ''.join(f"{word} " for word in line[:-1])
        linestring += f"{line[-1]}"
        linestrings.append(linestring)
    f.close()

    f = open('Rotations.rot', 'w')
    f.writelines(linestrings)
    print(f"Fixed rotation file!")


if __name__ == "__main__":
    main('Rotations.rot')
