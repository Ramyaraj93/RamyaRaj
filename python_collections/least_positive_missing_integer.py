#lst=[-2,-1,0,1,2,4]
#lst=sorted(lst)
#print(lst)


def smallest_missing_positive_integer(A):
    A.sort()
    N = len(A)

    i = 0
    previous = 0
    while i < N:
        current = A[i]

        if current > 0:
            if current > previous + 1:  # breaks consecutiveness
                return previous + 1
            else:
                previous = current

        i += 1

    return max(previous + 1, current + 1)