"""
For every string in the array, create a key, and check if that key exists in dict.
If it exists, then append to it this string
If not, then create a key and add this string to it

"""
s = input()
Dict = {}
def groupAnaGha():

    fullString = s.split(' ')
    for word in fullString:

        key = [0] * 26
        # create a key
        for letter in word:
            key[ord(letter) - ord('a')] += 1

        key = tuple(key)
        if Dict.get(key) is None:
            Dict[key] = [word]
        else:
            Dict[key].append(word)

    print(list(Dict.values()))

groupAnaGha()

