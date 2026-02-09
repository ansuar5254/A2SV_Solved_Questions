class FrequencyTracker:

    def __init__(self):
        self.valueCount = {}     
        self.frequencyMap = {}  

    def add(self, num: int) -> None:
        prevFreq = self.valueCount.get(num, 0)

        if prevFreq in self.frequencyMap:
            self.frequencyMap[prevFreq] -= 1
            if self.frequencyMap[prevFreq] == 0:
                del self.frequencyMap[prevFreq]

        self.valueCount[num] = prevFreq + 1
        newFreq = self.valueCount[num]
        self.frequencyMap[newFreq] = self.frequencyMap.get(newFreq, 0) + 1

    def deleteOne(self, num: int) -> None:
        if num not in self.valueCount:
            return

        oldFreq = self.valueCount[num]
        self.frequencyMap[oldFreq] -= 1
        if self.frequencyMap[oldFreq] == 0:
            del self.frequencyMap[oldFreq]

        self.valueCount[num] -= 1
        newFreq = self.valueCount[num]

        if newFreq > 0:
            self.frequencyMap[newFreq] = self.frequencyMap.get(newFreq, 0) + 1
        else:
            del self.valueCount[num]

    def hasFrequency(self, freq: int) -> bool:
        return freq in self.frequencyMap
