P, Q, R = map(int, input().split())
 
def solve(P,Q,R):
    l =[P+Q,Q+R,P+R]
    print(min(l))
    return min(l)

#python3 my_ans.py <input.txt