if __name__ == "__main__":
    with open("input.txt") as input_file:
        vertex_degrees = [0 for _ in range(int(input_file.readline().split()[0]))]

        for line in input_file.readlines():
            splited = line.split()
            vertex_degrees[int(splited[0]) - 1] += 1
            vertex_degrees[int(splited[1]) - 1] += 1

    with open("output.txt", 'w') as output_file:
        print(*sorted(vertex_degrees, reverse=True), file=output_file)
