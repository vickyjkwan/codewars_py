# Write a function called LCS that accepts two sequences and returns the longest
# subsequence common to the passed in sequences.
#
# Subsequence
#
# A subsequence is different from a substring. The terms of a subsequence need not be
# consecutive terms of the original sequence.
#
# Example subsequence
#
# Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".
#
# LCS examples
#
# lcs( "abcdef" , "abc" ) => returns "abc"
# lcs( "abcdef" , "acf" ) => returns "acf"
# lcs( "132535365" , "123456789" ) => returns "12356"
# Notes
#
# Both arguments will be strings
# Return value must be a string
# Return an empty string if there exists no common subsequence
# Both arguments will have one or more characters (in JavaScript)
# All tests will only have a single longest common subsequence. Don't worry about
# cases such as LCS( "1234", "3412" ), which would have two possible longest common
# subsequences: "12" and "34".
#
# Tips
#
# Wikipedia has an explanation of the two properties that can be used to solve the problem.
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

from itertools import combinations

def lcs(x,y):
    pass

def subseq(s):
    for n in range(1, len(s)+1):
        
