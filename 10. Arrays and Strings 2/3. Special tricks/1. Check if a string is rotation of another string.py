"""
Check if a string is rotation of another string...
This is the best trick!!!
Ex - if u are given string - abcde, and u want to find out if a string say - bcdea is formed by rotating abcde,
then u can do is -
Form a new string as appending original to itself .. say - abcdeabcde
Now if u search bcdea in abcdeabde, u will definitely get an answer!!!

"""

original = input()
goal = input()

def checkIfOrgCanRotateToGoal():
    if len(original) != len(goal):
        return False

        # double the original str - eg - abcde --> abcdeabcde
        # then check if cdeab is a subsrting of - abcdeabcde .. .this should return true

    newStr = original + original

    if goal in newStr:
        return True

    return False

print(checkIfOrgCanRotateToGoal())