class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        sorted_item = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        results = []
        for pair in sorted_item[:k]:
            results.append(pair[0])
        return(results)
            

       