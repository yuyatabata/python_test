S = str(input())
 
 
def solve(S):
    c=0
    for i in range(len(S)-1):
        if S[i]==S[i+1]:
            c+=1
    if c>0:
        print("Bad")
        return 'Bad'
    else:
        print("Good")
        return 'Good'

#python3 my_ans.py <input.txt