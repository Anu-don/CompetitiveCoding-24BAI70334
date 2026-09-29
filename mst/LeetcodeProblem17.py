def solution(num):
    if num < 2:
        return []

    val = str(num)
    result=[]
    zoro = ["abc","def",'ghi','jkl','mno','pqrs','tuv','wxyz']

    for i in val:

        new = []
        luffy = zoro[int(i)-2]

        for j in luffy:

            if result == []:
                new.append(j)
            else:
                for p in result:
                    new.append(p+j)

        result = new

    return result

n = solution(22)
print(n)

print()
print("For 34 : ",solution(34))
print()

print("For 264 : ",solution(264))
print()