class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for i in nums:
            frequencyDict[i] +=1
        sortedItems = sorted(frequencyDict.items(), key=lambda item: item[1], reverse = True)
        answer = []
        for num, count in sortedItems[:k]:
            answer.append(num)


        return answer
        