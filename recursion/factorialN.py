def factorial(n : int) -> int :
    """
    My induction is that if I am calling for factorial(N)
    it'll be N * factorial(N-1)

    So, if i am able to get factorial(n-1) I can immediately get factorial(N)
    if I get input as 1 then i return 1 simple
    """
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == "__main__":
    N = int(input("enter the value of n : "))
    print(factorial(N))
