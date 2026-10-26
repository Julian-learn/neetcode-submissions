class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        x = self.permute(nums[1:])
        res = []
        for perms in x:
            for i in range(len(perms) + 1):
                copy = perms.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        return res

    '''
    notes on how this works: build different perms from deepest recursive call
    in deepest call return [[]] (base case) which is the x in the second deepest call.
    here the for loop executes the first time and x becomes [[last_number_of_nums]]
    this is then given to the earlier recursive call to then add second last number before
    and after last number until its filled and res is finally returned.
    Remember: Build solution from inside!
    '''
        