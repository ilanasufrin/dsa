"""
Given two words word1 and word2, find the minimum number of steps (deleting a letter) required to convert word1 to word2. 
Deleting a letter from word1 and word2 at the same time is counted as 1 step.

"""


def deletion_distance(word1,word2,memo):
    if (len(word1),len(word2)) in memo: #try to speed it up instead of using the actual words
        return memo[(len(word1),len(word2))]
    
    if len(word1) < 1:
        return len(word2)
    
    if len(word2) < 1:
        return len(word1)

    steps = float('inf')
    
    if word1[0] == word2[0]:
        steps = deletion_distance(word1[1:],word2[1:],memo)

    steps = min(steps, 1 + deletion_distance(word1, word2[1:], memo), 1 + deletion_distance(word1[1:], word2, memo), 1 + deletion_distance(word1[1:], word2[1:], memo))

    memo[(len(word1),len(word2))] = steps

    return steps


print(deletion_distance("apple","banana",{}))