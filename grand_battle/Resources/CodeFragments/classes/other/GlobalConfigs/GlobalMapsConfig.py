from random import randint as rd


class GlobalMapsConfig:
    def __init__(self):
        self.MAP_MATRIX = []
        self.MAP_SEGMENTS_nums = [rd(0, 12) for _ in range(3)]
        self.MAP_SEGMENTS = []

        MAP_MATRIX = []
        for i in range(18):
            MAP_MATRIX.append([])
            for j in range(120):
                if i == 0 or i == 17 or j == 0 or j == 119:
                    MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
                else:
                    MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')

        self.MAP_MATRIX = MAP_MATRIX

        MAP_SEGMENTS_loaded = []
        MAP_SEGMENTS = []
        for i in range(12):
            num = '0' * int(i < 9) + str(i + 1)
            map_segment = open('Other/endless-map-segments/endless_map_segment' + num + '.txt')
            MAP_SEGMENTS_loaded.append(map_segment.readlines())
            map_segment.close()

        for k in range(12):
            MAP_SEGMENTS.append([])
            for i in range(18):
                MAP_SEGMENTS[k].append([])
                for j in range(24):
                    MAP_SEGMENTS[k][i].append(MAP_SEGMENTS_loaded[k][i][j])

        self.MAP_SEGMENTS = MAP_SEGMENTS
