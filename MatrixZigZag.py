'''
Company : Google
Link : https://www.careercup.com/question?id=5695158902325248
'''

def zigzag(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print('matrix {0}:' .format(matrix) )

    for row in range(0,rows):
        for col in range(0 , min(row + 1 ,cols)):
            print(matrix[row - col][col])

    for col in range(1, cols):
        for row in range(0, min(cols - col , rows)):
            print(matrix[rows - row - 1][col + row ])

    print()

zigzag([[1,2,3],[4,5,6],[7,8,9]])
zigzag([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
zigzag([[0,1],[2,3],[4,5]])
zigzag([[1],[2],[3]])
zigzag([[1, 2, 3]])

# direction = 1
# while col < len(matrix[0]):
#     while 0 <= row < len(matrix[0]):
#         print(matrix[row][col])
#         row += direction
#     row -= direction
#
#     direction = -1 * direction
#     col += 1
