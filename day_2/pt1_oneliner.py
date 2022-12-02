# Magic math
print(sum([(((((3+(r[1]-r[0]))%3)+1)%3)*3+r[1])for r in[[z[0]-64,z[1]-87]for z in[[(ord(y))for y in x.split()]for x in open('i').read().split('\n')]]]))