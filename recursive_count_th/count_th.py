'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# slice notation simplify:
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array


def count_th(word):

    # if the length of string is less than two, return 0
    if len(word) < 2:
        return 0

    # check for the string 'th', this will take two indices at the time
    elif word[0:2] == 'th':
        # start from the first index and move through the rest of the array recusively
        return 1 + count_th(word[1:])

    else:
        return count_th(word[1:])


word = 'none'
word1 = 'thecnology'

print(count_th(word))
print(count_th(word1))