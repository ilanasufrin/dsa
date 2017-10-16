"""
Given 2 sequences, find the length of the longest subsequence present in both of them.
NOT consecutive. order is important. NOT substring. first brute force it by calculating all permutations that maintains the correct order. Analyze it.
Then do it with recursion/DP.
Cache will help. 
max length of each sequence is 1 billion. Which means you need a good runtime, not EVERY permutation. 


Inputs:
- seq1, string
- seq2, string
Output:
- integer
"""
class LCS:
    def lcs_no_dp(self, seq1, seq2):
        
        if len(seq1) < 1:
            return 0

        if len(seq2) < 1:
            return 0

        if seq1[0] == seq2[0]:
            return 1 + self.lcs_no_dp(seq1[1:], seq2[1:])

        else:
            return max(self.lcs_no_dp(seq1[1:], seq2), self.lcs_no_dp(seq1, seq2[1:]))

    def lcs_memo(self, seq1, seq2, cache):
        if cache is None:
            cache = {}

        #Read from the cache
        #We are going to cache based on length of the strings
        if len(seq1) in cache and len(seq2) in cache[len(seq1)]:
            return cache[len(seq1)][len(seq2)]

        # print('comparing ' + seq1 + ' and ' + seq2)

        # base cases
        if len(seq1) < 1:
            return 0

        if len(seq2) < 1:
            return 0

        #backtracking
        lcs = 0

        lcs = self.lcs_memo(seq1[1:], seq2[1:], cache)
        if seq1[0] == seq2[0]:
            lcs += 1 

        #Is it better to keep the old lcs, or remove one letter from either of the words?
        lcs = max(lcs, self.lcs_memo(seq1[1:], seq2, cache), self.lcs_memo(seq1, seq2[1:], cache))

        # print('lcs now is ' + str(lcs))

        #write to the cache
        if len(seq1) not in cache:
            cache[len(seq1)] = {}
        cache[len(seq1)][len(seq2)] = lcs

        return lcs


if __name__ == '__main__':
    lcs = LCS()
    answer = lcs.lcs_memo("AGGTAB", "GXTXAYB", {}) # expecting 4
    print(answer)