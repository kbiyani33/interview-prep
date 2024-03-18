def print1toN(n:int):
    """
    In this base condition is that we have to print 1 for any input less than or equal to 1

    The induction is that if I am able to call for N, then I am able to call for N-1 as well.
    Because I want to print it in order from 1, I will first call it for N-1 which i am believing by induction that it'll print ->
    1, 2, 3, 4, 5, .....

    Say I want print(5)

    If 5 == 1 ?
        No
        So it'll call for 4
        is 4 == 1 ?
            call for 3
            if 3 == 1 ?
            No
            call for 2
                is 2 == 1 ?
                no
                call for 1
                    is 1 == 1 ?
                    Yes
                    print 1 then return
                print 2 then return
            print 3 then return
        print 4 then return
    print 5

    """
    if n <= 1:
        print(1, end= " ")
        return
    print1toN(n-1)
    print(n, end=" ")

def printNto1(n:int):

    """
    Say I want print(5)
    Is 5 == 1 ?
        No
        print 5
        call for 4
        is 4 == 1 ?
            no
            print 4
            call for 3
            is 3 == 1?
                no
                print 3
                call for 2
                is 2 == 1
                    no
                    print 2
                    call for 1
                    is 1 == 1
                        print(1)
                        return
                    return
                return
            return
        return
    """

    if n <= 1:
        print(1, end= " ")
        return
    
    print(n, end=" ")
    print1toN(n-1)

if __name__ == "__main__":
    N = int(input("enter the value of n : "))
    print1toN(n=N)
    print("\n")
    printNto1(n=N)
    print("\n")
