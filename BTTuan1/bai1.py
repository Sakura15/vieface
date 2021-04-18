s = input()
s = s.strip()
a = s.split(' ')
kq = ''
for i in range(len(a)-1):
    tmp = a[i].upper()
    if len(tmp):
        kq += tmp[0]
kq = kq + '.'
tmp = a[len(a)-1]
tmp = tmp.lower()
kq += tmp[0].upper() + tmp[1:len(tmp)]
print(kq)