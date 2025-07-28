"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

You should return a string in which:
Words are in reverse order
Only single spaces separate words
There are no leading or trailing spaces


"""
def reverse_words(s):
    s = s.split()
    reverse_form = s[::-1]
    return " ".join(reverse_form)

print(reverse_words("AI Engineer"))

