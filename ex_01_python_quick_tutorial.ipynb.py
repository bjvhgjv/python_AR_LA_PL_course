print("wacanda forever!")
print("."*30)
print("全军列阵")
print("i am you!")
print(3+3) 
print("减：",11-1)
print("乘：",4*31)
print("除：", 2/8)
print("整除：", 4//6)
print("余数：", 5%1)
print("幂：",4**4)
x=8.0
monadic_equation=5*x+5
print("monadic_equation=",monadic_equation)
print("monadic_equation=%.2f"%monadic_equation) 
print("monadic_equation={:.2f}".format(monadic_equation)) 
city_name="Xi'an"
coordinate_longitude=108.942292
coordiante_latitude=34.261013
print("The longitude of the Xi'an coordinate is {lon:.2f}, and the latitude is {lat}.".format(lon=coordinate_longitude,lat=coordiante_latitude))
x,y,b=3,6,9
func_2=5*x+6*y+b
print("func_2={}".format(x,y,b,func_2))
i_n=list(range(1,10,3)) 
print(list)
print("The list length={}".format(len(i_n)))
print("Maximum value={}".format(max(i_n)))
print("Minimum value={}".format(min(i_n)))
i_s=list(map(chr,range(100,150)))
print(i_s)
print("."*25)
print("[4:6]->{}".format(i_s[5:6]))
print("[-5:-2]->{}".format(i_s[-4:-1]))
print("[-6:]->{}".format(i_s[-6:]))
print("[:4]->{}".format(i_s[:1]))
print("[:]->{}".format(i_s[:]))
help(map) 
help(chr)
print(i_s)
print("[0:8:3]->{}".format(i_s[0:5:2]))
print("[::5]->{}".format(i_s[::1]))
print("[5:2:-8]->{}".format(i_s[8:4:-1]))
print("[15:2:-1]->{}".format(i_s[19:3:-2]))
print("[4::-1]->{}".format(i_s[7::-2]))
print("[:4:-1]->{}".format(i_s[:3:-2]))
print(i_s)
i_s[5]=99 
print("i_s[5]=99->{}".format(i_s))
i_none=i_s+[None]*6
print("i_s+[None]*6->{}".format(i_none))
i_none[13]=2015
print("i_none[13]=2015->{}".format(i_none))
i_none[-6:-3]=list(range(99,105,1)) 
print("i_none[-6:-3]=list(range(100,104,2))->{}".format(i_none))
i_none[1:1]=[0,0,0,12]
print("i_none[1:1]=[0,0,0,12]->{}".format(i_none))
del i_none[-2:] 
print("del i_none[-2:]->{}".format(i_none))
i_s_2=list(map(chr,range(100,105)))
print(i_s_2)
i_s_2.append(88)
print("i_s_2.append(88)->{}".format(i_s_2))
i_s_2.append(list(range(20,50,2)))
print("i_s_2.append(list(range(20,50,2)))->{}".format(i_s_2))
i_spechars=['*',')','*']
i_s_2.extend(i_spechars)
print("i_s_2.extend(i_spechars)->{}".format(i_s_2))
print("i_s_2.count('*')={}".format(i_s_2.count('*')))
print("i_s_2.index('e')={}".format(i_s_2.index('e')))
i_s_2.insert(2,[800,1200,100])
print("i_s_2.insert(2,[800,1200,100])->{}".format(i_s_2))
print("i_s_2.pop(7)_popup->{}".format(i_s_2.pop(7)))
print("i_s_2.pop(7)_retention->{}".format(i_s_2))
i_s_2.remove('*')
print("i_s_2.remove('*')_retention->{}".format(i_s_2))
list_n_2=[1,24,3,80,5,3]
list_n_2.sort()
print("list_n_2.sort()->{}".format(list_n_2))
tuple_1=3,6,9,
print("tuple_1=3,6,9,->{}".format(tuple_1))
print("3*(30*3,)->{}".format(3*(20*3,)))
print("tuple((3,6,9))->{}".format(tuple((5,8,9)))) #用()
print("tuple([3,6,9])->{}".format(tuple([5,8,9]))) #用[]
import random
items=[(0,[i for i in range(5)]),(1,[random.sample(list(range(80,120,5)),3)]),(2,'forever')] #[i for i in range(5)] 
print("items->{}".format(items))
dic=dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[1]->{}".format(dic[1]))
print("len(dic)->{}".format(len(dic)))
dic[3]=(random.random(),random.uniform(80,150))
print("dic[3]=(random.random(),random.uniform(80,150))->{}".format(dic))
del dic[1]
print("del dic[1]->{}".format(dic))
print("4 in dic->{}".format(3 in dic))
print("6 in dic->{}".format(5 in dic))
print("dic.keys()->{}".format(dic.keys())) 
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print("list(dic.keys())->{}".format(list(dic.keys())))
for a,d in enumerate(dic.items()): 
    print(a,d)
i_A=list(range(6,20,3))
i_B=list(range(100,150,15))
print("i_A={},i_B={}".format(i_A,i_B))
dic_2={0:i_A,1:i_B}
print("dic_2={}".format(dic_2))
print("_"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(1,9,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_cofo=dic_2
print("dic_cofo=dic_2.cofo()->{}".format(dic_cofo))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_cofo={}".format(dic_cofo))
dic_cofo[5].remove(5)
print("dic_cofo[5].remove(5)->{}".format(dic_cofo))
dic_cofo.setdefault(6,[77,99]) #返回值
print("dic_cofo.setdefault(6,[77,99])->{}".format(dic_cofo))
dic_2.pop(5) #移除
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,7,6,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
dic_2.update(dic_update) #更新
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
dic_2.popitem() #移除
print("dic_2.popitem()->{}".format(dic_2))
dic_3={}.fromkeys([0,1,2,3,4,'A']) #给定键
print("dic_3={}"+".fromkeys([2,3,4,5,6,'A'])->{}".format(dic_3)) #脱字符
i_s_3=list("Wanconda forever!")
print("i_s_3=list(\"Wanconda forever!\")->{}".format(i_s_3)) #"\" escape character
print("\"Wancondaw\"+\" forever!\"->{}".format("Wancondaw"+" forever!"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("len(\"Wancondaw forever!\")->{}".format(len("Wancondaw forever!")))
coordinates="120.132007,30.300508,9.7"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates))) #通常用eval()方法将字符串，转换为对应数值形式；
print("\"Wanconda forever!\".lower()->{}".format("Wanconda forever!".lower()))
print("\"Wanconda forever!\".upper()->{}".format("Wanconda forever!".upper()))
print("\"Wanconda forever!\"[6:]->{}".format("Wanconda forever!"[6:]))
print("\"    Wanconda forever!    \".strip()->{}".format("    Wanconda forever!    ".strip()))
print("\"Wanconda forever!\".replace(\"forever\",\"ironman\")->{}".format("Wanconda forever!".replace("forever","ironman")))
Wanconda_i=list("Wanconda forever!")
Wanconda_i.sort()
print("Wanconda_i.sort()>{}".format(Wanconda_i))
print("\"Wanconda forever!\".find(\"fo\")->{}".format("Wanconda forever!".find("fo")))
format_str="Wacanda,%s and %s!"
values=("Wacanda","iron")
new_str=format_str % values
print("new_str=format_str % values->{}".format(new_str))
format_str_2="Pi with three decimals:%.3f,and enter a value with percent sign:%.2f %%" 
from math import pi
new_str_2=format_str_2 % (pi,1.2345678)
print("new_str_2=format_str_2 % (pi,1.2345678)->{}".format(new_str_2))
format_str_3="%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3=format_str_3%(pi,pi,pi,"Wacanda forever!",5,"Wacanda forever!",52,52,pi)
print("{}".format(new_str_3))
from string import Template
s_template_1=Template("$x,glorious,$x!")
s_1=s_template_1.substitute(x="Wacanda")
print("s_1=s_template_1.substitute(x=\"Wacanda\")->{}".format(s_1))
s_template_2=Template("${x}rever is amazing!")
s_2=s_template_2.substitute(x="Wacanda")
print("s_2=s_template_2.substitute(x=\"Wacanda\")->{}".format(s_2))
s_template_3=Template("$x and $y are both amazing!")
substitute_dict=dict([('x','Wacanda'),('y','forever')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))
import re
pattern_1='Wacanda'
text=" Wacanda forever!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))
pattern_2='Wacanda forever'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))
print("re.findall('.acanda','Wacanda forever!')->{}".format(re.findall('.acanda','Wacanda forever!')))
print("re.findall('.acanda','Wacanda forever!')->{}".format(re.findall('.acanda','Wacanda forever!')))
print("re.findall('.acanda','Wacanda forever!')->{}".format(re.findall('.acanda','Wacanda forever!')))
print("re.findall('.acanda','Wacanda forever!')->{}".format(re.findall('.acanda','Wacanda forever!')))
print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')))
print("re.findall(r'w{2}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{1,3}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{1,3}\.cadesign\.cn','www.cadesign.cn')))
import re
print("re.findall('[fo]*rever!','Wacanda forever!')->{}".format(re.findall('[fo]*rever!','Wacanda forever!')))
print("re.findall('[fo]*rever!','Wacanda orever!')->{}".format(re.findall('[fo]*rever!','Wacanda orever!')))
print("re.findall('[fo]*rever!','Wacanda orever!')->{}".format(re.findall('[fo]*rever!','Wacanda orever!')))
print("re.findall('[fo]*rever!','Wacanda orever!')->{}".format(re.findall('[fo]*rever!','Wacanda rever!')))
import re
print("re.findall('captain|ironman','captain')->{}".format(re.findall('captain|ironman','captain')))
print("re.findall('captain|ironman','ironman')->{}".format(re.findall('captain|ironman','ironman')))
print("re.findall('captain|ironman','ironman and captain')->{}".format(re.findall('captain|ironman','ironman and captain')))
import re
print("re.findall('\d','number=8')->{}".format(re.findall('\d','number=8')))
print("re.findall('\D','number=6')->{}".format(re.findall('\D','number=6')))
print("re.findall('[^1-8]','number=10')->{}".format(re.findall('[^1-8]','number=10')))
import re
print("re.findall('[a-z]','forever')->{}".format(re.findall('[a-z]','forever-3.0')))
print("re.search('[a-z]+','forever')->{}".format(re.search('[a-z]+','forever')))
if re.search('[a-z]+','forever'):
    print("re.search('[a-z]+','forever')->found it!")
print("re.split(',','Wcanda,,,,,,forever!')->{}".format(re.split(',','Wcanda,,,,,,forever!')))
print("re.sub('forever','captain','Wcanda forever!')->{}".format(re.sub('forever','captain','Wcanda forever!')))
pattern_compile=re.compile('forever')
print("pattern_compile.findall('Wcanda,,,,,,forever!')->{}".format(pattern_compile.findall('Wcanda,,,,,,forever!')))
import re
if re.match('f','forever'):
    print("re.match('f','forever')->found it!")
print("\'forever\'.find(\'forever\')->{}".format('forever'.find('forever')))
print("\'forever\'.find(\'ever\')->{}".format('forever'.find('ever')))
print("\'forever\'.find(\'o\')->{}".format('forever'.find('o')))
print("\'f\' in \'forever\'->{}".format('f' in 'forever'))
print("\'Wacanda,,,,,,forever!\'.split(',')->{}".format( 'Wacanda,,,,,,forever!'.split(',')))
print("\'Wacanda forever!\'.replace(\'forever\',\'forever\')->{}".format( 'Wacanda forever!'.replace('forever','captain')))
match_1=re.match(r'www\.(.*)\..{3}','www.forever.org')
print("match_1.gourp(1)->{}".format(match_1.group(1)))
print("match_1.start(1)->{}".format(match_1.start(1)))
print("match_1.end(1)->{}".format(match_1.end(1)))
print("match_1.span(1)->{}".format(match_1.span(1)))
match_2=re.match(r'www\.(.*)\.(.{3})','www.forever.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))
i_1=list(range(5,16,3))
print("i_1={}".format(i_1))
print("for i in i_1:")
for i in i_1:
    print(i)
print("for m in range(len(i_1)):")
for i in range(len(i_1)):
    print("idx={},val={}".format(i,i_1[i]))
print("/"*10)   
dic_4=dict(a=5,b=3,c=3,d=1)
print("dic_4={}".format(dic_4))
print("+"*88)
print("for u in dic_4:")
for k in dic_4:
    print(k)
print("for l,n in dic_4.items():")
for l,n in dic_4.items():
    print("key={},val={}".format(k,l))
x=2
while x<=50:
    print("x={}".format(x))
    x+=18  
x=2
while x<=66:
    print("x={}".format(x))
    x+=4 
    if x>=50:break    
    import sys
print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))  
    i+=2
    if i>=50:break
topography_fp='./data/elevation.txt'
a=open(topography_fp,'r')
elevation_dat=[]
while True:
    line=a.readline()
    elevation_dat.append(line)
    if not line:break
a.close()
print("elevation_dat[:10]={}".format(elevation_dat[:10]))
import pandas as pd
elevation_df=pd.read_csv(topography_fp, delimiter = ",",header=None) 
print(elevation_df)
i_a=[1,2,3,4]
i_b=['point_a','point_b','point_c','point_d']
zip_i=zip(i_a,i_b) #The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
print("zip_i=zip(i_a,i_b)->{}".format(zip_i))
print("dict(zip_i)->{}".format(dict(zip_i)))
zip_i=zip(i_a,i_b) 
for a,b in zip_i:
    print(a,b)
    zip_i=zip(i_a,i_b)
a,b=zip(*zip_i)
print("a={},b={}".format(a,b))
i_c=['point_a','point_b','point_c','point_d']
dic_4={}
for idx,value in enumerate(i_c):
    dic_4[idx]=value
print("dic_4={}".format(dic_4))
print("dict((i,v) for i,v in enumerate(i_c))->{}".format(dict((i,v) for i,v in enumerate(i_c)))) #list comprehension
for i,(a,b) in enumerate(zip(i_a,i_b)):
 print('%d:%s,%s'%(i,a,b))
print("[x*x for x in range(1,25,8) if x%2==0]->{}".format([x*x for x in range(1,25,8) if x%2==0]))
print("[(x,y) for x in range(3)for y in range(2)]->{}".format([(x,y) for x in range(3)for y in range(2)]))
print("[(x,y) for x,y in zip(range(3),range(2))]->{}".format([(x,y) for x,y in zip(range(3),range(2))]))
nested_list=[[a for a in range(2,6,2)],2,3,[b for b in range(20,40,4)],[[c for c in range(200,1200,20)],3,9]]
print("[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]->{}".format(nested_list)) #嵌套列表推导式
flatten_i=lambda i: [m for n_i in i for m in flatten_i(n_i)] if type(i) is list else [i] 
print("flatten_i(nested_list)->{}".format(flatten_i(nested_list)))
x=5
if x<0:
    print('It is negative.')
elif x==0:
    print('Equal to zero.')
elif 0<x<20:
    print('Positive but smaller than 20')
else:
    print('Positive and larger than or equal to 20.')
x=y=[2,5,8]
z=[2,5,8]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x),id(y),id(z))) #Memory Location
del x[2]
print("x={},y={},z={} after del x[2]".format(x,y,z))
x=[2,5,8]
print("2 in x->{}".format(3 in x))
print("0 in x->{}".format(0 in x))
print("5 not in x->{}".format(3 not in x))
print("8 not in x->{}".format(0 not in x))
a,b,c=3,6,9
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b amazing!!!')
def simple_func(x,y):
    z=pow(x,2)+y
    return z

print("simple_func(4,6)->{}".format(simple_func(4,6)))
print("simple_func(6,4)->{}".format(simple_func(6,4)))
print("simple_func(y=6,x=4)->{}".format(simple_func(y=6,x=4)))
def fibonacci(s,count): 
    fib_i=[0,1]
    fib_part=[]
    if s==0 or s==1:
        fib_part[:]=fib_i
        for i in range(count-2):
            fib_part.append(fib_part[-1]+fib_part[-2])
    else:
        while True:
            fib_i[:]=[fib_i[1],fib_i[0]+fib_i[1]]
            #print(fib_i)
            if fib_i[1]-s>=0:break
        fib_part[:]=fib_i
        if abs(fib_i[0]-s)>=abs(fib_i[1]-s):
            for i in range(count-1):
                fib_part.append(fib_part[-1]+fib_part[-2])
            fib_part.pop(0)
        else:
            for i in range(count-2):
                fib_part.append(fib_part[-1]+fib_part[-2])
    return fib_part

print("fibonacci(5,8)->{}".format(fibonacci(5,8)))
print("fibonacci(4,7)->{}".format(fibonacci(4,7)))
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(15))
class Bird:
    fly='Whirring'
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No.Thanks!')

class Apodidae(Bird): 
    def __init__(self):
        super(Apodidae,self).__init__()
        self.sound='Squawk!' #美 
    def sing(self):
        print(self.sound)
swift=Apodidae()
print("swift.fly->{}".format(swift.fly))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()
blackswift=Apodidae()
scarceswift=Apodidae()
print("blackswift.sing()->")
blackswift.sing()
print("scarceswift.sing()->")
scarceswift.sing()
print("blackswift.fly->{}".format(blackswift.fly))
blackswift.fly='hunting' #重新赋予实例的属性
print("blackswift.fly after redefining the blackswif's attribute->{}".format(blackswift.fly))
print("scarceswift.fly->{}".format(scarceswift.fly))
blackswift.sing()
help(Bird)
class Fibs():
    def __init__(self):
        self.a=1
        self.b=2
    def next(self):  #实现迭代器的next方法
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self): #实现迭代方法
        return self
f=Fibs()
fa=[]
fb=[]
for i in range(11):
    fa.append(f.next())
print("fa={}".format(fa))
for i in range(6):
    fb.append(f.next())
print("fb={}".format(fb))
ilst_d=list(range(2,15,3))
print("lst_d={}".format(ilst_d))
lst_iter=iter(list)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
next(lst_iter)
lst_e=[list(range(2,15,4)),[4,50,67,list(range(5)),58]]
print("lst_e={}".format(lst_e))
flatten_lst=[]
for v_1 in lst_e:
    try:
        for v_2 in v_1:
            try:
                for v_3 in v_2:
                    flatten_lst.append(v_3)
            except TypeError:
                flatten_lst.append(v_2)
    except TypeError:
        flatten_lst.append(v_1)
print("flatten_lst={}".format(flatten_lst))
def flatten(lst): #定义生成器（包含yield语句的函数）
    try: #使用语句try\except捕捉异常        
        for n_lst in lst:  #循环列表            
            for m in flatten(n_lst): #使用递归的方法循环子列表                
                yield m  #使用yield语句，每次产生多个值，当返回一个值时函数就会被冻结，当再次激活时，从停止的那点开始执行
    except TypeError:  #当函数被告知展开一个元素时，引发TypeError异常，生成器返回一个值
        yield lst #生成器返回引发异常的一个值        
print("list(flatten(lst_e))->{}".format(list(flatten(lst_e))))
flatten_lst=lambda lst:[m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst] #lambda 生成器方法
def infinite():
    n=1
    while True:
        yield 'num#'+str(n)
        n+=1
n=infinite()
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("[next(n) for i in range(6)]->{}".format([next(n) for i in range(6)]))
n=3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]->{}".format([[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]))
print("_"*50)
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))->{}".format(([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))))
gen=([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))
print("next(gen)->{}".format(next(gen)))
print("next(gen)->{}".format(next(gen)))
def f_convert_a(x):
    try:
        return float(x)
    except:
        return x
print("f_convert_a('1.2345')->{}".format(f_convert_a('1.2345')))    
print("f_convert_a('power')->{}".format(f_convert_a('power')))  
print("f_convert_a(2,5,8)->{}".format(f_convert_a((2,5,8))))  
def f_convert_b(x):
    try:
        return float(x)
    except ValueError:
        return x
print("f_convert_a('1.2345')->{}".format(f_convert_a('1.2345')))    
print("f_convert_a('power')->{}".format(f_convert_a('power')))  
print("f_convert_a(2,5,8)->{}".format(f_convert_a((2,5,8))))   
def f_convert_c(x):
    try:
        return float(x)
    except ValueError:
        return x
    except TypeError:
        print(x,'TypeError')
print("f_convert_c('3.1415')->{}".format(f_convert_c('3.1415')))    
print("f_convert_c('string')->{}".format(f_convert_c('string')))  
print("f_convert_c(3,6,7)->{}".format(f_convert_c((3,6,7))))         
def f_convert_d(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        print(x,'ValueError or TypeError')
print("f_convert_d('3.1415')->{}".format(f_convert_d('3.1415')))    
print("f_convert_d('string')->{}".format(f_convert_d('string')))  
print("f_convert_d(3,6,7)->{}".format(f_convert_d((3,6,7)))) 
def f_convert_e(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        return print(x,e)
print("f_convert_e('3.1415')->{}".format(f_convert_e('3.1415')))    
print("f_convert_e('string')->{}".format(f_convert_e('string')))  
print("f_convert_e(3,6,7)->{}".format(f_convert_e((3,6,7))))    
def f_convert_f(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        pass
print("f_convert_f('3.1415')->{}".format(f_convert_f('3.1415')))    
print("f_convert_f('string')->{}".format(f_convert_f('string')))  
print("f_convert_f(3,6,7)->{}".format(f_convert_f((3,6,7))))     
def f_open_a(fp): 
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close
        return data
tryException_content=f_open_a("./data/tryException.txt")   
print("tryException_content->{}".format(tryException_content))
f_open_a("./data/tryException_.txt")
def f_open_a(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close()
        return data
    finally:
        print('done!')
f_open_a("./data/tryException.txt")        
raise Exception #没有任何有关错误信息的普通异常
raise Exception('Computer says no!') #添加错误信息的异常
class some_custom_exception(Exception):pass #
raise some_custom_exception
x=20
assert x>0 #为真则不做任何事情














