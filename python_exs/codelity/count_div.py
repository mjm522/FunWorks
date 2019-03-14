"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

def solution(A,B,K):

    if A%K == 0:
        pass
    else:
        if K > A:
            A += (K-A)
        else:
            A += A%K

    if A <= B:
        count = 1
    else:
        return 0


    return count + (B-A)//K

    # while A <= B:

    #     A += K

    #     if A <= B:
    #         count += 1

    # return count


[[11,345,17], [6,11,2],[0, 2000000000, 1]]

print(solution(11,345,17))