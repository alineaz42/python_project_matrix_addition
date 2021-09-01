'''
Name: Ali Neaz
B.Sc(Hon's) in statistics at Islamic University,Kushtia,Bangladesh
'''
print("Hello wellcome to matrix calculation programm")

# taking inpute for the matrics


def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]th element:  "))
            row.append(inp)
        o.append(row)
    return o

# itereting every element and adding them into a new matrix


def sum(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output


# input of the order of the matrix {mxn}
m = int(input("Enter The value of m: "))
n = int(input("Enter The value of n: "))

# First matrix
print("Enter matrix A\n")
A = matrix(m, n)
# print(A)


# second matrix
print("Enter matrix B\n")
B = matrix(m, n)
# print(B)

# calling the sum function
addedMatrix = sum(A, B)
# printing the sum value
print(addedMatrix)
