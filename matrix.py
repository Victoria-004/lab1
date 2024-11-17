matrix = [
    [40, 72, 6, 92, 98],
    [18, -33, -48, 81, 26],
    [1, -4, 6, -2, 0],
    [36, 9, 0, 4, 1],
    [-55, 2, 66, 70, -3]
]

def sort(func):
    def sort_matrix(matrix):
        func(matrix)
        return matrix
    return sort_matrix

@sort
def bubble_sort(matrix):
    for column in range(len(matrix[0])):
        for i in range(len(matrix)):
            for j in range(0, len(matrix) - i - 1):
                if matrix[j][column] > matrix[j + 1][column]:
                    matrix[j][column], matrix[j + 1][column] = matrix[j + 1][column], matrix[j][column]
    return matrix

def calculate_fi(matrix):
    row_means = []
    for row in matrix:
        row_mean = sum(row) / len(row)
        row_means.append(row_mean)
    return row_means

def calculate_f(row_means):
    product = 1
    for mean in row_means:
        product *= mean
    return product

sorted_matrix = bubble_sort(matrix)

print("Відсортована матриця:")
for i in sorted_matrix:
    print(i)

row_means = calculate_fi(sorted_matrix)
print("Середні арифметичні значення елементів у кожному рядку:", row_means)

product_of_means = calculate_f(row_means)
print("Добуток середніх арифметичних значень:", product_of_means)































