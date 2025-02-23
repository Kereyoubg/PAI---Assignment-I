unsorted_array = [10, 22, 9, 33, 21, 50, 41, 60, 80]

def getLongestIncreasingSubsequence(arr):
    store = []
    for el in arr:
        internal_store = []
        for i in arr[arr.index(el):]:
            if (len(internal_store)) == 0:
                internal_store.append(i)
            else:
                if (i > internal_store[len(internal_store) -1]):
                    internal_store.append(i)
        if (len(internal_store) > len(store)):
            store = internal_store
    return store

largest_sequence = getLongestIncreasingSubsequence(unsorted_array)
print(largest_sequence)
print(len(largest_sequence))
