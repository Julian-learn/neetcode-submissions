class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #    map = {}
    #    for i in range(len(nums)):
    #        map[nums[i]] = 1 + map.get(nums[i],0)
    #    return sorted(map, key=lambda x: map[x], reverse = True)[:k]   
        map = {}
        count_map = [] 
        result = []
        for i in range(len(nums)):
            map[nums[i]] = 1 + map.get(nums[i],0) #intilialize hashmap {number : count}
        
        for _ in range(len(nums) + 1):
            count_map.append([])
        
        for key, value in map.items():
            count_map[value].append(key)
        
        for i in range(len(count_map)-1, 0, -1):
            for value in count_map[i]:
                result.append(value)
                if len(result) == k:
                    return result


        