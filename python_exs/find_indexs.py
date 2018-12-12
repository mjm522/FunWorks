"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target

you may assume that each input would have exactly one solution and you may not use the same element twice

eg: given nums=[2,7,11,15], target = 9

return [0, 1]

"""


def find_indxs(arr, tgt):

    arr_dict={}
    for i,k in enumerate(arr):
        arr_dict[k]=i

    for i,k in enumerate(arr):
        other = tgt-k

        if other in arr_dict.keys():
            return [i, arr_dict[other]]

    return "There is no indx found"

def main():

    test = [2,7,11,15]
    tgt=19

    print find_indxs(test, tgt)


if __name__ == '__main__':
    main()



