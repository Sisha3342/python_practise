open_file = open('input.txt', 'r', encoding='utf-8')
initial_info = open_file.readline().split()
neighbors_list = [set() for _ in range(int(initial_info[0]))]
for edge in open_file:
    vertexes = tuple(map(int, edge.split()))
    neighbors_list[vertexes[0] - 1].add(vertexes[1])
    neighbors_list[vertexes[1] - 1].add(vertexes[0])
for adjacent_list in neighbors_list:
    print(len(adjacent_list), *adjacent_list)
open_file.close()
