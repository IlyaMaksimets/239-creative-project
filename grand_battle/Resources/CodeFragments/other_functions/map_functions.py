from random import randint as rd


def endless_map_update(MAP_SEGMENTS_NUMS, MAP_SEGMENTS):
    MAP_MATRIX = []
    for i in range(18):
        MAP_MATRIX.append([])

    for i in range(18):
        MAP_MATRIX[i].append('P')

    for n in range(11):
        MAP_MATRIX[0].append('P')
        MAP_MATRIX[17].append('P')
        for i in range(1, 17):
            MAP_MATRIX[i].append(['0'])

    for k in range(len(MAP_SEGMENTS_NUMS)):
        new_segment = MAP_SEGMENTS_NUMS[k]
        for i in range(18):
            for j in range(24):
                MAP_MATRIX[i].append(MAP_SEGMENTS[new_segment][i][j])

    MAP_SEGMENTS_NUMS.clear()
    MAP_SEGMENTS_NUMS = [rd(0, 11), rd(0, 11), rd(0, 11)]

    for i in range(1, 17):
        MAP_MATRIX[i].append('0')
        MAP_MATRIX[i].append('0')

    MAP_MATRIX[0].append('P')
    MAP_MATRIX[0].append('P')
    MAP_MATRIX[17].append('P')
    MAP_MATRIX[17].append('P')

    for i in range(18):
        MAP_MATRIX[i].append('P')

    return MAP_MATRIX, MAP_SEGMENTS_NUMS


def load_map(level):
    MAP_MATRIX = []
    Map = open('../Other/level-maps/level0' + level + 'map.txt')
    map_matrix = Map.readlines()
    for i in range(18):
        MAP_MATRIX.append([])
        for j in range(120):
            MAP_MATRIX[i].append(map_matrix[i][j])
    Map.close()

    return MAP_MATRIX
