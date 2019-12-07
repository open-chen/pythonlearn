import requests
import random
import re
def demo_string():
    stra="hello worlD"
    print(stra)
    print(stra.capitalize())
    print(stra.replace("worlD","tihuan"))
    print("\n\rhello \\r\n".lstrip())
    print("\n\rhello \\r\n".rstrip())
    print(stra.startswith("h"))
    print(stra.endswith("d"))
    print(len(stra))
    print("-".join(["a","b"]))
    print(stra.split(" "))

def demo_operation():
    print(1+2,5/2,5*2,5%2,++2)
    print(True,not True)
    print(3,1<2,5>2)
    print(4,2<<3,2<<4)
    print(5,5|3,5&3,5^3)
    x=2
    y=3.3
    print(x,y,type(x),type(y))

def demo_buildinfunction():
    print(max(2,1,4,5),min(2,1,4,5))
    print(len("sssssss"),len([2,1,4,5]))
    print(abs(-2))#绝对值
    print(range(1,10,3))
    print(dir(list))
    x=2
    print(eval("x+3"))
    print(chr(37),ord("a"))

def demo_controlflow():
    score=65
    if score > 99:
        print("A")
    elif score > 60:
        print("B")
    else:print("C")
    while score<100:
        print(score)
        score+=10
    score=65
    #continue break pass
    for i in range(0,10,2):
        if i==0:
            pass
        if i<5:
            continue
        print(i)
        if i==7:break

def demo_list():
    lista=[1,2,3]
    print(lista)
    listb=["1","a","0.222"]
    print(listb)
    lista.extend(listb)
    print(lista)
    print(len(lista))
    print("a" in listb)
    lista=lista+listb
    print(lista)
    listb.insert(0,"www")
    print(listb)
    listb.pop(1)
    print(listb)
    listb.reverse()
    print(listb)
    print(listb[0])
    listb.sort()
    print(listb)
    listb.insert(0,"x")
    print(listb * 2)
    print([0] * 15)
    lista.append(listb)
    print(lista)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def demo_dict():
    dicta = {1:1,2:4,3:9,"+":add,"-":sub}
    print(dicta,type(dicta))
    print(dicta.keys(),dicta.values())
    for key,value in dicta.items():
        print(key,value)
    print(dicta["+"](1,2))
    print(dicta.get("-")(45,98))
    dicta["*"]="x"
    print(dicta)
    dicta.pop(1)
    print(dicta)
    del dicta[2]
    print(dicta)

def demo_set():
    seta=set([1,2,3])
    print(seta)
    setb=set((2,3,4))
    #seta.add(4)
    print(seta,setb)
    print(seta.intersection(setb),seta & setb)
    print(seta|setb,seta.union(setb))
    print(seta-setb)
    print(len(seta))
class User:
    type="USER"
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def __repr__(self):
        return  "im"+self.name+" "+str(self.uid)

class Admin(User):
    type = "ADMIN"
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group=group
    def __repr__(self):
        return "im"+self.name+" "+str(self.uid)+self.group
def demo_exception():
    try:
        print(2/1)
        print(2/0)
        raise Exception("Raise Error","NowCoder")
    except Exception as e:
        print("error",e)
    finally:
        print("clean up")

def demo_random():
    # random.seed(1)
    print(random.random()*100)
    print(random.randint(0,100))
    print(random.choice(range(0,100,10)))
    print(random.sample(range(0,100),4))
    a=[1,2,7,3,4,5]
    print(random.shuffle(a))
def demo_re():
    str="abc123def12gh15"
    p1=re.compile('[\d]+')
    p2 = re.compile('[\d]')
    print(p1.findall(str))
    print(p2.findall(str))

    str='a@163.com:b@gmail.com;c@qq.com'
    p3=re.compile('[\w]+@[163|qq]+\.com')
    print(p3.findall(str))

if __name__=='__main__':
    demo_re()
    # demo_random()
    # demo_exception()
    '''user1=User("name1",1)
    print(user1)
    admin1=Admin("a1",11,"101")
    print(admin1)'''
    #print("hello world!")
    # comment
    # demo_string()
    #demo_operation()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    #demo_set()

