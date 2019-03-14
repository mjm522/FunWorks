"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""
from itertools import combinations

# def solution(A):

#     PQ = combinations(range(len(A)),2)

#     def get_avg(p, q):

#         return sum(A[p:q+1])/(q-p+1)

#     min_val = 1e10
#     indx = 0

#     for pq in PQ:
#         avg = get_avg(pq[0], pq[1])
#         if  avg < min_val:
#             min_val = avg
#             indx = pq[0]
#         if avg == min_val:
#             if  pq[0] < indx:
#                 indx = pq[0]

#     return indx

def solution(A):

    sum_a = sum(A)

    min_val = 1e10
    indx = 0

    for p in range(len(A)):
        tmp_sum = sum_a-A[p]
        for q in range(len(A)-1, p+1, -1):
            tmp_sum -= A[q]
            avg = tmp_sum/(q-p+1)
            print(avg)
            if  avg < min_val:
                min_val = avg
                indx = p
            if avg == min_val:
                if  p < indx:
                    indx = p

    return indx


print(solution([4,2,2,5,1,5,8]))


