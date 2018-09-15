st='hello as you'
l=len(st)
for x in range(-1,-2*l,-2):
    st+=st[x]

print(st[l:])
print(st[::-1])