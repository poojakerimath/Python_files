def pascal_triangle(n):
    triangle =[]
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            print(f"row[{j}] = {triangle[i - 1][j - 1]} + {triangle[i - 1][j]} = {row[j]}")

        triangle.append(row)

    return triangle

n = int(input("enter the rows you want enter"))
result = pascal_triangle(n)
for row in result:
    print(row)