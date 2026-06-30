class Solution:
    def segregate0and1(self, arr):
        # code here
        i = 0
        for j in range(len(arr)):
            if arr[i] == 0:
                i += 1
            else:
                if arr[j] == 0:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
                    i += 1
        return arr