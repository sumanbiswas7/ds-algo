# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of 
# the non-overlapping intervals that cover all the intervals in the input.

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda i:i[0])
    output = [intervals[0]]
    
    for start , end in intervals[1:]:
        outputLastElement = output[-1][1]
        
        if start <= outputLastElement:
            output[-1][1] = max(outputLastElement,end)
        else:
            output.append([start,end])
    
    return output

intervals = [[1,3],[8,10],[2,6],[15,18]]
merge(intervals)

