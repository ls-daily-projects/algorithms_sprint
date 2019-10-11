'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

from math import floor

# Time complexity O(n)
# Space complexity O(n)


def count_th(word, buffer=[], count=0):
    if len(word) < 1:
        return count

    if len(buffer) == 0:
        buffer.append(word[0])
        buffer.append(word[1])
        word = word[2:]
    else:
        buffer.pop(0)
        buffer.append(word[0])
        word = word[1:]

    if buffer[0] == "t" and buffer[1] == "h":
        count += 1

    return count_th(word, buffer, count)
