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


def test1(farg,*args):
    print ("farg:",farg)
    for value in args:
        print ("args:",value)

def test2(farg,**args):
    print ("farg:",farg)
    for key in args:
        print ("key:%s  values:%s"%(key,args[key]))

test2()