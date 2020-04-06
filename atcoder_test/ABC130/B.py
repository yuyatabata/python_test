N, X = list(map(int, input().split()))
l = list(map(int, input().split()))
 
def solve(N,X,l):
    D=0
    i=0
    c=0
    while D <= X:
        try:
            c+=1
            # if i>len(l):
            #     break
            D+=l[i]
            i+=1
        except IndexError:
            break
    print(c)
    return c
#python3 my_ans.py <input.txt