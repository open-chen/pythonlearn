
'''def demo(list):
    list2=[]
    for i in list[:]:
        if i['department_id'] not in list2:
            i["value"]=[i["value"]]
            list2.append(i['department_id'])
        else:
            for j in list:
                if j['department_id']==i['department_id']:
                    j["value"].append(i["value"])
                    list.remove(i)
                    break
    return list'''
'''def demo(list):
    dict = {}
    for i in list:
        if i['department_id'] not in dict:
            dict[i["department_id"]] = [i["value"]]
        else:
            dict[i["department_id"]].append(i["value"])
    new=[]
    for k,v in dict.items():
        new.append({"department_id": k,"value": v})
    print(new)'''

'''def demo(list):
    dict = {}
    for i in list[:]:
        if i['department_id'] not in dict:
            dict[i["department_id"]] = list.index(i)
            i["value"] = [i["value"]]
        else:
            list[dict[i["department_id"]]]["value"].append(i["value"])
            list.remove(i)
    return list'''

'''def demo(list):
    dict = {}
    n=0
    for i in list[:]:
        if i['department_id'] not in dict:
            dict[i["department_id"]] = n
            i["value"] = [i["value"]]
            n+=1
        else:
            list[dict[i["department_id"]]]["value"].append(i["value"])
            list.remove(i)
            n+=1
    return list'''

'''def demo(list):
    dict = {}
    n=0
    for i in list[:]:
        if i[sorted(i)[0]] not in dict:
            dict[i[sorted(i)[0]]] = n
            i[sorted(i)[1]] = [i[sorted(i)[1]]]
            n += 1
        else:
            list[dict[i[sorted(i)[0]]]][sorted(i)[1]].append(i[sorted(i)[1]])
            list.remove(i)
            n += 1
    return list'''

def demo(list):
    dict = {}
    n=0
    for i in list[:]:
        id=sorted(i)[0]
        val=sorted(i)[1]
        if i[id] not in dict:
            dict[i[id]] = n
            i[val] = [i[val]]
            n+=1
        else:
            list[dict[i[id]]][val].append(i[val])
            list.remove(i)
            n+=1
    return list

if __name__=="__main__":
    list1 = [
        {
            "department_id": 1,
            "value": "张三"
        },
        {
            "department_id": 2,
            "value": "李四"
        },
        {
            "department_id": 2,
            "value": "王五"
        },
        {
            "department_id": 2,
            "value": "张六"
        }
    ]
    list3=demo(list1)
    print(list3)
    # demo(list1)

    list2 = [
        {
            "department_id": 1,
            "value": ["张三", "李四"]
        },
        {
            "department_id": 2,
            "value": ["王五"]
        }
    ]