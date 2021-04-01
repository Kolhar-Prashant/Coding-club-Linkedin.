def rotate(row_num):
    for _ in range(k):
        temp = mat[row_num][1::]
        temp.append(mat[row_num][0])
        mat[row_num]=temp
        
mat= [[1,2,3],[4,5,6],[7,8,9]]
k=2
for row_num in range(len(mat)):
    rotate(row_num)
for row in mat:
    print(row)
