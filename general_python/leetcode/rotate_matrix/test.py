class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        j = 0
        length = len(matrix)
        if length % 2 == 0:
            count = length //2
        else:
            count = length // 2 + 1
        for j in range(count):
            i = 0
            while i < length - 1 - j * 2:
                matrix[j][i + j], \
                matrix[i + j][-1 - j], \
                matrix[-1 - j][-1 - i - j], \
                matrix[-1 - i - j][j] = \
                    matrix[-1 - i - j][j], \
                    matrix[j][i + j], \
                    matrix[i + j][-1 - j], \
                    matrix[-1 - j][-1 - i - j]
                i += 1
