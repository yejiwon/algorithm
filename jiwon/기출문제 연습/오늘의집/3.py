def getFormatValue(formats, targetKey, key):
    value = formats[key] if key in formats else "{"+key+"}"
    if value.startswith("{"):   # 밸류가 템플릿이면
        nextKey = value[1:-1]
        if nextKey == targetKey:    # 무한 반복이면
            return "{"+targetKey+"}"
        if nextKey in formats:      # 밸류가 재귀이면
            return getFormatValue(formats, targetKey, nextKey)
    return value

def solution(tstring, variables):
    answer = []
    formats = { key: value for key, value in variables }

    for word in tstring.split(" "):
        value = word
        if word.startswith("{"):
            value = getFormatValue(formats, word[1:-1], word[1:-1])
            formats[word] = value
        answer.append(value)

    return ' '.join(answer)


if __name__ == "__main__":
    print(solution("this is {template} {template} is {state}", [["template", "string"], ["state", "{template}"]])) # 2
    print(solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{template}"]])) # 3
    print(solution("this is is {state}", [["template", "{state}"], ["state", "{templates}"]]))
    print(solution("{a} {b} {c} {d} {i}", [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]))
