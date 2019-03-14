
def q_sort(arr, lo, hi):

    def swap(e1, e2):
        tmp = arr[e1]
        arr[e1] = arr[e2]
        arr[e2] = tmp

    def partision(t_lo, t_hi):
        pivot = arr[t_hi]
        i = t_lo-1

        for j in range(t_lo, t_hi):
            if arr[j] <= pivot:
                # if i != j:
                i += 1
                swap(i, j)
                
        swap(i+1, t_hi)
        
        return i+1

    if lo < hi:
        p = partision(lo, hi)
        q_sort(arr, lo, p-1)
        q_sort(arr, p+1, hi)

    return arr




def main():

    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print q_sort(test, 0, len(test)-1)

if __name__ == '__main__':
    main()