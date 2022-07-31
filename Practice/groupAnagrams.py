import collections
arr = [x for x in input().split()]

def countAnagrams():

    # Create a dict first
    myDict = {} #collections.defaultdict(list)

    # for every string in arr, create a array len 26 for every occurrence of a, b c, ... jmust like anagrams
    for s in arr:

        count = [0] * 26

        for c in s:

            count[ord(c) - ord('a')] += 1

        count = tuple(count)
        if myDict.get(count) is None:
            myDict[count] = [s]
        else:
            myDict[count].append(s)

    print(list(myDict.values()))


countAnagrams()