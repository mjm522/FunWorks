"""
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    int solution(int H[], int N);

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].


"""

def solution(A):

    count = 1
    start_slice = False
    start_slice_idx = 0
    end_slice_idx = 0
    min_val = min(A)
    A = [x-min_val for x in A]

    while sum(A) != 0:

        for i, k in enumerate(A):

            if k != 0 and not start_slice:
                start_slice = True
                start_slice_idx = i

            if (k==0 and start_slice) or start_slice_idx==len(A)-1:
                start_slice = False

                if start_slice_idx==len(A)-1:
                    end_slice_idx = len(A)
                else:
                    end_slice_idx = i

                if end_slice_idx < start_slice_idx:
                    break

                min_val = min(A[start_slice_idx:end_slice_idx])

                for j in range(start_slice_idx, end_slice_idx):
                    A[j] -= min_val

                count += 1
    return count


print(solution([8,8,5,7,9,8,7,4,8]))

