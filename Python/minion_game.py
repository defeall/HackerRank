def minion_game(s):
    kevin,stuart=0,0
    for i in range(len(s)):
        if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
            kevin=kevin+(len(s)-i)
        else:
            stuart=stuart+(len(s)-i)
    if(kevin>stuart):
        print("Kevin",kevin)
    elif(kevin==stuart):
        print("Draw")
    else:
        print("Stuart",stuart)
if __name__ == '__main__':
    s = input()
    minion_game(s)
