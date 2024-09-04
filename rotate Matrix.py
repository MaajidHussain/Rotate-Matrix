def rotateMatrix(matrix):
    n=len(matrix)
    
    print("Original Matrix: ")
    for row in matrix:
        print(row)
    print()
        
    print("Transposing the Matrix.")
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    print("Transposed Matrix: ")
    for row in matrix:
        print(row)
    print() 
    
    print("Reversing Rows.")
    for row in matrix:
        row.reverse()
        
    print("Reversed Matrix: ")
    for row in matrix:
        print(row)
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix(matrix)