n = int(input("Enter the order of matrix: "))

Matrix_1 = [[int(input("Enter the number: ")) for i in range(0,n)] for j in range(0,n)]
Matrix_2 = [[int(input("Enter the number: ")) for i in range(0,n)] for j in range(0,n)]

Transpose = list(zip(*Matrix_2))

Multiplied_Matrix = []
for i in range(0,n):
    sum = []
    for j in range(0,n):
        total = 0
        for k in range(0,n):
            total += Matrix_1[i][k] * Transpose[j][k]
        sum.append(total)
    Multiplied_Matrix.append(sum)

print(Multiplied_Matrix)