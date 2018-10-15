import numpy as np
from itertools import permutations

#clockwise from top left
sum_circles = np.array([14, 16, 21, 18])

given_value = 4

sub_puzzle_indices = [ [ [0,1], [0,1] ], 
                       [ [0,1], [1,2] ],
                       [ [1,2], [1,2] ],
                       [ [1,2], [0,1] ] ]


def check_sub_puzzle_sum(sub_puzzle, indx):

    total = np.sum(np.sum(sub_puzzle))

    if total == sum_circles[indx]:
        return True
    else:
        return False

def search_puzzle(sol):

    success = 0

    for k in range(4):

        sub_puzzle = sol[sub_puzzle_indices[k][0][0]:sub_puzzle_indices[k][0][1]+1, sub_puzzle_indices[k][1][0]:sub_puzzle_indices[k][1][1]+1]

        if check_sub_puzzle_sum(sub_puzzle, k):
            success += 1
        else:
            break

    if success == 4:
        return sol
    else:
        return None


#brute force search
def solver():

    sol = np.arange(1,10)

    perms = set()

    for perm in permutations(sol):
        if np.asarray(perm).reshape(3,3)[1,1] == given_value:
            perms.add(perm)

    print "Number of permutations \t", len(perms)

    raw_input( "Click enter to continue")

    for it, p in enumerate(perms):

        new_sol = np.asarray(p).reshape(3,3)

        curr = search_puzzle(new_sol)

        if  curr is None:

            print "Search \t", it, "failed"

            continue
        else:

            print "Solution found \n", curr

            break

        
solver()
    




