"""
Reverse words in a sentence
We did this by 2 pointer approach too!! end to len(str) and start to len(str) - 1, decrement start...
if start is space, then store string from start+1 to end... and then do end = start
"""

sentence = input()

def reverseWordsInSentence(sentence):
    # split a string based on ' '
    sentence = sentence.split()

    # reverse a string by reversed and it returns a iterator, convert it into list
    sentence = list(reversed(sentence))


    # join this array based on space operator
    sentence = ' '.join(sentence)

    # return the sentence
    return sentence

print(reverseWordsInSentence(sentence))


