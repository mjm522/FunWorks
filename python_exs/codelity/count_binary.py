

def solution(S):
    # write your code in Python 3.6
    S = int(S, 2)
    count = 0
    while S != 0:
        if S%2==0:
            S = S//2
        else:
            S = S-1
        count += 1
        
    return count

def solution2(S):
    return len(S)-1 + (len(S)-1)//2


def solution3(S):

    count = 0

    start_count = False

    for s in S:

        if s=='0':
            if start_count:
                count += 1
        else:
            start_count = True
            count += 2

    if start_count:
        return count-1
    else:
        return 0



def solution4(A):
    # write your code in Python 3.6
    
    if not A:
        return 0

    necks = dict(zip(range(len(A)), A))

    print(necks)

    start_a = 0
    next_i = necks[start_a]
    max_val = 0
    count = 1

    while bool(necks):

        if len(necks) == 1:
            break

        if start_a == next_i:
            del necks[start_a]
            start_a = next(iter(necks))
            next_i = necks[start_a]
            count = 1
            # continue

        elif necks[next_i] == start_a:
            count += 1
            if count > max_val:
                max_val = count
            del necks[start_a]
            del necks[next_i]
            if len(necks) == 0:
                break
            start_a = next(iter(necks)) 
            next_i = necks[start_a]
            count = 1
        else:
            count += 1
            tmp_next_i = next_i
            next_i = necks[next_i]
            del necks[tmp_next_i]
            
    return max_val

# print(solution('1111111111111111111111111111111111111'))
# print(solution2('1111111111111111111111111111111111111'))
# print(solution3('1111111111111111111111111111111111111'))

print(solution4([5, 4, 0, 3, 1, 2, 6]))
# print(solution4([1, 4, 3, 5, 6, 2, 0]))
# print(solution4([0, 1, 2, 3, 4, 5, 6]))
# print(solution4([0, 1, 2, 3, 4, 5, 6]))