# worst: O(N) because of last line ?
def searchNumOccurrence(V, k, start, end):
    if start > end:
        return 0
    mid = int((start + end) / 2)
    if V[mid] < k:
        return searchNumOccurrence(V, k, mid + 1, end)
    if V[mid] > k:
        return searchNumOccurrence(V, k, start, mid - 1)
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end)


vec = [1, 2, 3, 4, 5, 1, 2]
searchNumOccurrence(vec, 1, 0, len(vec))
