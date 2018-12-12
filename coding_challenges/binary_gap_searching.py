def solution(N):

    def get_binary(num):
        binary = []
        result = num

        if result == 0:
            return [0]
        if result == 1:
            return [1]

        while True:
            binary.append(result%2)
            result = result/2
            if (result==0) or (result==1):
                binary.append(result)
                break

        return binary[::-1]

    binary_rep = get_binary(N)

    start_count = False
    end_count = False
    count = 0

    print "Binary of %d is \t"%N, binary_rep

    for k in range(len(binary_rep)):

        if binary_rep[k] == 1 and not start_count and not end_count:
            start_count = True

        if binary_rep[k]==1 and start_count and count>0:
            end_count = True

        if start_count and binary_rep[k]==0 and not end_count:
            count += 1

    if not end_count:
        count = 0

    return count



def main():

    gap = solution(221)

    print "The number of binary gaps is \t", gap

if __name__ == '__main__':
    main()
