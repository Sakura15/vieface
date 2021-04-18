import numpy as np
st = input()
a = st.split()
m = int(a[0])
n = int(a[1])
arr = np.zeros((m,n))
for i in range(m):
    lst = input().split()
    arr[i] = list(map(lambda x: int(x) if x.isdigit() else 0, lst))
st = input()
a = st.split()
p = int(a[0])
q = int(a[1])
arr1 = np.zeros((p,q))
for i in range(p):
    lst = input().split()
    arr1[i] = list(map(lambda x: int(x) if x.isdigit() else 0, lst))
def mul():
    if n != p:
        return None
    else: return arr.dot(arr1)
print(mul())