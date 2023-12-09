from itertools import accumulate
import operator


if __name__ == '__main__':
    ray1 = [1.0, 2.0, 3.0, 4.0]
    ray2 = [2.0, 3.0, 4.0, 5.0]
    ray3 = [3.0, 4.0, 5.0, 6.0]
    rayray = [ray1, ray2, ray3]
    print("Acc", list(accumulate(ray1, operator.add)))
    print("Sum1", sum(ray1))
    print("Map2", list(map(operator.add, ray1, ray2)))
    print("Map3", list(map(operator.add, map(operator.add, ray1, ray2), ray3)))
    prev = []
    for ray in rayray:
        curr = ray
        if prev != []:
            curr = list(map(operator.add, prev, ray))
        prev = curr
    print("Loop", list(prev))
