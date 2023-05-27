# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Using Patience Sorting to get the length of the 
        longest increasing subsequence in O( n * log(n) )
        time        
        """        
        # does binary search on an array 
        # sorted in strict descending order
        def reverse_bisect(array, ind):
            l, r = 0, len(array)
            while l < r:
                mid = (l+r)//2
                if nums[ind] > nums[array[mid]]:
                    r = mid
                else:
                    l = mid + 1
            return l

        n = len(nums)

        # the array containing the piles of the cards 
        # using the term cards because it makes it easier
        # to understand
        pile_list = [[0]]

        # a card that can't be placed on pile 1
        # will find the first card of pile 1 that's 
        # smaller than it then point to it 
        pointers = [-1] * n
        
        for i in range(1, n):
            card = nums[i]
            card_index = i

            card_is_placed = False
            card_equal_to_previous_topmost = False

            for pile in pile_list:
                # if the current card is smaller than 
                # the top most card of the current pile 
                topmost_in_pile = nums[pile[-1]]

                if card < topmost_in_pile:
                    # if the current card is equal to the topmost
                    # card in the previous pile then we don't put it 
                    # on the current pile since it will point to the 
                    # topmost of the previous pile, which has the same 
                    # value and we want our increasing subsequence to be 
                    # strictly increasing 
                    if not card_equal_to_previous_topmost:
                        pile.append(card_index)
                    # we consider it placed either way, this way 
                    # we test to see if it's placed so we place it 
                    # in a new pile in case it isn't, and if it's 
                    # equal to the topmost of the prev pile we consider it 
                    # placed despite not actually placing it
                    card_is_placed = True
                    break
                elif nums[i] > nums[pile[-1]]:
                    # use binary search to find the first smaller card in the pile 
                    # so we point to it, if the next pile isn't good either we'll 
                    # do the same thing and will update the pointer then 
                    pointers[i] = reverse_bisect(pile, i)
                    # 
                    if pointers[i] >= len(pile):
                        pointers[i] = -1
                else:
                    # if the card is equal to the topmost in this pile, we 
                    # make card_equal_to_previous_topmost True so we know it in the 
                    # next iteration
                    card_equal_to_previous_topmost = True

            if not card_is_placed and not card_equal_to_previous_topmost:
                pile_list.append([i])
        
        # this dfs will follow the pointers from the last pile until they're -1
        # the length of the longest path from this to -1 is the length of the longest
        # increasing subsequence
        # 
        def dfs(index, pile_index):
            if pointers[index] == -1:
                return 1
            return dfs(pile_list[pile_index-1][pointers[index]], pile_index-1) + 1

        # pile_list[-1] is the last pile, the k is the different indexes in that pile
        # the pile index is -1 meaning we start at the last pile 
        return max([dfs(k, -1) for k in pile_list[-1]])
            
