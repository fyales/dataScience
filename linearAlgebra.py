def vector_add(v,w):
    return [i + j for i,j in zip(v,w)]

def vector_subtract(v,w):
    return [i - j for i,j in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add,vectors)

print vector_add([1,2],[2,1])
print vector_subtract([1,2],[2,1])
print vector_sum([[3,4],[5,6],[7,8]])

# two row,three line
A = [[1,2,3 ],
    [4,5,6]]
print A

# three row,two line
B = [[1,2],
    [3,4],
    [5,6]]
print B

def shape(A):
    num_rows = len(A)
    num_lines = len(A[0]) if A else 0
    return num_rows,num_lines

print shape(A)
print shape(B)

