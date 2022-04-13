directions = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

def solution(path):
    result = []

    prevTime = 0
    currDir = path[0]
    currDis = 0
    for p in path:
        if p == currDir:
            currDis += 1
        else:
            turnDir = 'right' if (directions[p] - directions[currDir] == 1 or directions[p] - directions[currDir] == -3) else 'left'
            if currDis > 5:
                result.append(f"Time {prevTime + currDis - 5}: Go straight {500}m and turn {turnDir}")
            else:
                result.append(f"Time {prevTime}: Go straight {currDis*100}m and turn {turnDir}")
            prevTime += currDis
            currDir = p
            currDis = 1

    return result


if __name__ == "__main__":
    print(solution("EEESEEEEEENNNN"))
    print(solution("SSSSSSWWWNNNNNN"))