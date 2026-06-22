import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        heap = []  # min-heap of (frequency, element)
        for key, freq in d.items():
            if len(heap) < k:                        # heap not full yet, just add
                heapq.heappush(heap, (freq, key))
            elif freq > heap[0][0]:                  # heap full, check if current freq beats the minimum
                heapq.heappop(heap)                  # remove the smallest
                heapq.heappush(heap, (freq, key))    # add the new one

        return [key for freq, key in heap]