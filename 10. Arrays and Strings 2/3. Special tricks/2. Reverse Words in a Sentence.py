"""
Reverse words in a sentence
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


