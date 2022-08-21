def intervalIntersection(firstList, secondList):
    first, second = 0, 0
    ans = []

    while first < len(firstList) and second < len(secondList):
        commonStart = max(firstList[first][0], secondList[second][0])
        commonEnd = min(firstList[first][1], secondList[second][1])

        if commonEnd >= commonStart:
            ans.append([commonStart, commonEnd])

        if firstList[first][1] > secondList[second][1]: second += 1
        else: first += 1

    return ans