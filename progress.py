_dict = {}

with open('homework.txt',encoding='utf-8') as f:
    print(type(f))
    # print(dir(f))
    for line in f.readlines():
        word = line.split()
        _group = word[0]
        _name_list = [word[1], word[2]]
        _dict[_group] = _name_list

print(_dict)
test = id(_dict)
print(test)


