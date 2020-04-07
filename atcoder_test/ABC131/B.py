N,L = list(map(int, input().split()))

 
def solve(N,L):
    s_list=[]
    for i in range(1,N+1):
        s = L+i-1
        s_list.append(s)
    
    m=min(s_list,key=abs)
    ans=sum(s_list)-m
    print(ans)
    return ans
#python3 my_ans.py <input.txt