from random import randint
import time


def main() -> None:

    
    n = int(input("Enter the size of the vector: "))

    vector = [randint(0, 100) for _ in range(n)]

    print("Unsorted vector: ", vector)

    start_time = time.time()
    v1 = Bubblesort(vector)
    time1 = time.time() - start_time

    start_time = time.time()
    v2 = Insertionsort(vector)
    time2 = time.time() - start_time

    start_time = time.time()
    v3 = Selectionsort(vector)
    time3 = time.time() - start_time

    print("Bubblesort: Time: ", time1)
    print("Insertionsort: Time: ", time2)
    print("Selectionsort: Time: ", time3)

    # print("Sorted vector: ", v1)

    return


def Bubblesort(vector: list) -> list:
    v = vector.copy() 
    for i in range(len(v)):
        # activate/deactivate lower bound:
        # is_sorted = True
        for j in range(len(v) - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                # activate/deactivate lower bound:
                # is_sorted = False
            #if is_sorted:
                #break
    return v


def Insertionsort(vector: list) -> list:
    v = vector.copy()
    for i in range(1, len(v)):
        key = v[i]
        j = i - 1
        while j >= 0 and v[j] > key:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = key
    return v


def Selectionsort(vector: list) -> list:
    v = vector.copy()
    for i in range(len(v)):
        min_index = i
        for j in range(i + 1, len(v)):
            if v[min_index] > v[j]:
                min_index = j
        v[i], v[min_index] = v[min_index], v[i]
    return v


if __name__ == "__main__":
    main()
