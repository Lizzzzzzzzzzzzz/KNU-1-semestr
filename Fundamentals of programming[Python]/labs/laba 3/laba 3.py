import math

accuracy = float(input("Введіть точність: "))
res = 0
memberToSave = 0

print("===========================================")
print("        x                  k                          member                          sum        ")
print("===========================================")

for x in range(1, 6):
    k = 0
    currentRes = 0
    while True:
        if (k * 3 + k * ((x + 1) ** 0.5)) == 0 and x == 1:
            print("        ", x, 8 * "  ", k, 20 * "  ", "-", 15 * "  ", round(res, 4))
        elif (k * 3 + k * ((x + 1) ** 0.5)) == 0:
            space2String = (15 - len(str(round(res, 4)))) * "  "

            if res < 0:
                space2String += " "

            print("        ", x, 8 * "  ", k, 20 * "  ", "-", space2String, round(res, 4))
        else:
            currentRes = (((-1) ** k) * (x ** k)) / (k * 3 + k * ((x + 1) ** 0.5))
            res += currentRes

            # Configuring table
            space1String = (20 - len(str(round(currentRes, 4)))) * "  "

            if currentRes < 0:
                space1String += " "

            space2String = (15 - len(str(round(res, 4)))) * "  "

            if res < 0:
                space2String += " "

            space3String = (9 - len(str(k))) * "  "

            print("        ", x, space3String, k, space1String, round(currentRes, 4), space2String, round(res, 4))
            if abs(currentRes - memberToSave) <= accuracy:
                print("overflow - break cycle with k")
                break
        k += 1
        memberToSave = currentRes

print("===========================================")
print("sum=", res)