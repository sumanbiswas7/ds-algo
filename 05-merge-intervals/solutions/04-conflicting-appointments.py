def isConflicts(intervals):
    intervals.sort(key = lambda i:i[0])

    for i in  range(1, len(intervals)):
      currFirst = intervals[i][0]
      prevLast = intervals[i-1][1]

      if (currFirst < prevLast): return False

    return True