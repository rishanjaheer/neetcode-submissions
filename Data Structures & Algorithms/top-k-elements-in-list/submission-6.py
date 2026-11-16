import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap and map every number to its frequency
        #make an array with arrays inside it for k length
        #iterate through the hashmap and add to the inner array using the freq as an index
        #iterate from the end to the start looking for the k most frequent

        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for num, count in hashmap.items():
            freq[count].append(num)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        