
def q_sort(arr, lo, hi):

    def swap(e1, e2):
        tmp = arr[e1]
        arr[e1] = arr[e2]
        arr[e2] = tmp

    def partision(t_lo, t_hi):
        pivot = arr[t_hi]
        i = t_lo

        for j in range(t_lo, t_hi-1):
            if arr[j] < pivot:
                if i != j:
                    swap(i, j)
                i += 1
        swap(i, t_hi)
        
        return i

    if lo < hi:
        p = partision(lo, hi)
        q_sort(arr, lo, p-1)
        q_sort(arr, p+1, hi)

    return arr




def main():

    test = [5,2,2,1,8,3,2,9,2]
    print q_sort(test, 0, len(test)-1)

if __name__ == '__main__':
    main()