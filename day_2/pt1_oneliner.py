# Magic math
print(sum([(((((3+(r[1]-r[0]))%3)+1)%3)*3+r[1])for r in[[z[0]-64,z[1]-87]for z in[[(ord(y))for y in x.split()]for x in open('i').read().split('\n')]]]))


# More messing around
# print(sum([(((((3+(r[1]-r[0]))%3)+1)%3)*3+r[1])for r in[[ord(z[0])-64,ord(z[1])-87] for z in[x.split()for x in open('i').read().split('\n')]]]))
# (x:=open('i').read().split(),print(sum([(((((3+(r[1]-r[0]))%3)+1)%3)*3+r[1]) for r in [[ord(z[0])-64,ord(z[1])-87] for z in zip(x[0::2],x[1::2])]])))