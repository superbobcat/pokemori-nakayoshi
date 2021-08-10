# points data:
# https://pocketcamp.fun/1684/
# Lv.10 : 20ポイント->21ポイント

point = [1, 4, 4, 5, 9, 11, 14, 16, 19, 21,
        24, 26, 29, 31, 34, 36, 39, 41, 44, 46,
        49, 51, 54, 56, 59, 61, 64, 66, 69, 71,
        74, 76, 79, 81, 84, 86, 89, 91, 94, 96,
        99, 101, 104, 106, 109]
def nakayoshi(targetLv, currentLv=1, nextPt=0):
    sum = 0
    if nextPt != 0:
        for i in range(currentLv+1, targetLv):
            sum = sum + point[i]
        sum = sum + nextPt
    else:
        for i in range(currentLv, targetLv):
            sum = sum + point[i]
    return sum

print(nakayoshi(15,13,12))
