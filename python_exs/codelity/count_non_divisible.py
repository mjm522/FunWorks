"""
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array 
that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

For the following elements:

        A[0] = 3, the non-divisors are: 2, 6,
        A[1] = 1, the non-divisors are: 3, 2, 3, 6,
        A[2] = 2, the non-divisors are: 3, 3, 6,
        A[3] = 3, the non-divisors are: 2, 6,
        A[4] = 6, there aren't any non-divisors.

Assume that the following declarations are given:

    struct Results {
      int * C;
      int L; // Length of the array
    };

Write a function:

    struct Results solution(int A[], int N);

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as a structure Results.

For example, given:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..50,000];
        each element of array A is an integer within the range [1..2 * N].


"""
import math
def solution(A):

    l = len(A)
    counts = [0]*l
    A_sort =  sorted(A)
    l_sort = len(A_sort)
    
    for k in range(l):

        for i,a in enumerate(A_sort):

            if (a==A[k]) or (A[k]%a==0):
                continue
            else:
                counts[k] += 1

            if a > 1+math.sqrt(A[k]):
                counts[k] += l_sort-i-1
                break

    return counts


# print(solution([3,1,2,3,6]))
# print(solution([3,3,2,3,6]))


