def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    waitingTime = 0
    for executionTime in queries[:-1]:
        print(waitingTime, executionTime)
        waitingTime += executionTime
        totalWaitingTime += waitingTime

    return totalWaitingTime


if __name__ == "__main__":
    print(minimumWaitingTime([3, 2, 1, 2, 6]))
