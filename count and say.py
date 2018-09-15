

def generate(num):
    res=''
    temp=0
    tag=0
    for x in str(num):
        if x==temp:
            temp=x
            tag+=1
        else:
            res+=str(tag)+str(temp)
            temp=x
            tag=1
    res += str(tag) + str(temp)
    return res[2:]

def put(N):
    n=1
    tag=1
    while(tag<N):
        n=generate(n)
        tag+=1
    return str(n)

num=6
print(put(num))