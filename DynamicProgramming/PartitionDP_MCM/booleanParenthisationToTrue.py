from typing import List
MODULO = 1000000007
def recursiveBooleanParenthesization(exp:str, i:int, j:int, isTrue:bool, dp:List[List[List[int]]]) -> int:
    if i>j:
        return 0
    
    if i==j and isTrue:
        return int(exp[i]=="T")
    
    if i==j and not isTrue:
        return int(exp[i]=="F")
    
    if dp[i][j][int(isTrue)] != -1:
        return dp[i][j][int(isTrue)]
    
    ans = 0
    for index in range(i+1, j, 2):
        operator = exp[index]
        leftTrueCount = recursiveBooleanParenthesization(exp, i, index-1, True, dp)
        leftFalseCount = recursiveBooleanParenthesization(exp, i, index-1, False, dp)
        rightTrueCount = recursiveBooleanParenthesization(exp, index+1, j, True, dp)
        rightFalseCount = recursiveBooleanParenthesization(exp, index+1, j, False, dp)
        if isTrue:
            if operator=="&":
                ans += (leftTrueCount*rightTrueCount)%MODULO
            elif operator=="|":
                ans += ((leftTrueCount*rightTrueCount)%MODULO + (leftTrueCount*rightFalseCount)%MODULO + (leftFalseCount*rightTrueCount)%MODULO)%MODULO # Since TT, TF and FT are possible ways to get a true eventually
            elif operator=="^":
                ans += ((leftFalseCount*rightTrueCount)%MODULO + (leftTrueCount*rightFalseCount)%MODULO)%MODULO
        else:
            if operator=="&":
                ans += ((leftFalseCount*rightFalseCount)%MODULO + (leftTrueCount*rightFalseCount)%MODULO + (leftFalseCount*rightTrueCount)%MODULO)%MODULO # Since FF, TF and FT are possible ways to get a false eventually
            elif operator=="|":
                ans += (leftFalseCount*rightFalseCount)%MODULO
            elif operator=="^":
                ans += ((leftFalseCount*rightFalseCount)%MODULO + (leftTrueCount*rightTrueCount)%MODULO)%MODULO
    ans%=MODULO
    print(dp)
    dp[i][j][int(isTrue)] = ans
    return ans

def tabulationBottomUp(exp: str) -> int:
    # create the dp array
    n = len(exp)
    dp = [[[-1]*2 for i in range(n)] for i in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n):
            for k in range(2):
                if i>j:
                    dp[i][j][k] = 0
                    continue
                if i==j and k==1:
                    dp[i][j][k] = int(exp[i]=="T")
                    continue
                if i==j and k==0:
                    dp[i][j][k] = int(exp[i]=="F")
                    continue
                isTrue = bool(k)
                ans = 0
                for index in range(i+1, j, 2):
                    operator = exp[index]
                    lT = dp[i][index-1][int(True)]
                    rT = dp[index+1][j][int(True)]

                    lF = dp[i][index-1][int(False)]
                    rF = dp[index+1][j][int(False)]

                    if isTrue:
                        # For and operator, there's only one way to get true i.e. both true
                        if operator=="&":
                            ans += (lT*rT)%MODULO
                        # For or, TT, TF and FT are different ways to get true
                        elif operator=="|":
                            ans += ((lT*rT)%MODULO + (lT*rF)%MODULO + (lF*rT)%MODULO)%MODULO
                        # For XOR, TF and FT are different ways to get true
                        elif operator=="^":
                            ans += ((lT*rF)%MODULO + (lF*rT)%MODULO)%MODULO
                    else:
                        # For and operator, there's 3 ways to get False i.e.  FF, TF, FT
                        if operator=="&":
                            ans += ((lF*rF)%MODULO + (lT*rF)%MODULO + (lF*rT)%MODULO)%MODULO
                        # For or, FF is the only way to get false
                        elif operator=="|":
                            ans += (lF*rF)%MODULO
                        # For XOR, TT and FF are different ways to get false
                        elif operator=="^":
                            ans += ((lT*rT)%MODULO + (lF*rF)%MODULO)%MODULO
                dp[i][j][k] = ans%MODULO
    print(dp)
    return dp[0][n-1][1]








def evaluateExp(exp: str) -> int:
    # Write your code here.
    # n = len(exp)
    # dp = [[[-1]*2 for i in range(n)] for i in range(n)]
    # print(dp)
    # ans = recursiveBooleanParenthesization(exp, 0, len(exp)-1, True, dp)
    # print(dp)
    # return ans
    ans = tabulationBottomUp(exp)
    print(ans)


if __name__=="__main__":
    print(evaluateExp("T^F|T^F&T&F"))
