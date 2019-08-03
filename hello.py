# # 可写函数说明
# def printinfo(arg1, *vartuple):
#     print("Output " + str(arg1))
#     if(len(vartuple) > 0):
#         print(vartuple[0])
#         print(vartuple[1])
#     return


# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)


expression = 10


def printinfo(str):
    return str


print(printinfo(100))
print(expression)
