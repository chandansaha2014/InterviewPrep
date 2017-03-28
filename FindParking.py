''''
Google Software Engineer
Find minimum steps/moves for parking
'''


def min_moves(parking, desired):
    cars = dict()
    free_spot = None
    for i in range(len(parking)):
        if parking[i] == -1:
            free_spot = i
        elif parking[i] is not desired[i]:
            cars[parking[i]] = (i, None)

    for i in range(len(parking)):
        if desired[i] in cars:
            cars[desired[i]] = (cars[desired[i]][0], i)


    swaps = dict()
    for car in cars:
        swaps[cars[car][1]] = cars[car][0]
    print("Swaps")
    print(swaps)

    num_swaps = 0
    while swaps:
        if free_spot in swaps:
            temp = free_spot
            free_spot = swaps[free_spot]
            del swaps[temp]
        else:
            first = list(swaps.items())[0]
            swaps[first[0]] = free_spot
            free_spot = first[1]
        #print(swaps)
        num_swaps += 1
    print("cars Dictionary")
    print(cars)
    return num_swaps


p = [1, 2, 3, -1, 4, 5]
print(p)
d = [5, -1, 2, 3, 1, 4]

print(min_moves(p, d))
