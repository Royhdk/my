# a被除数数组，b除数数组，c每次的临时被除数，d商
import os

a = []
b = []
c = []
d = []


def shuru():
    # x被除数
    global x
    x = input('请输入被除数：')
    # y除数
    global y
    y = input('请输入除数：')
    for i in x:
        if i!='0' and i!='1':
            print('输入有误，请重新输入！！！')
            shuru()
            break
    for i in y:
        if i!='0' and i!='1':
            print('输入有误，请重新输入！！！')
            shuru()
            break
def quling(x):
    x = int(x)
    return str(x)

def jisuan():
    global a,b,c,d
    if c[0]=='1':
        d.append('1')
        for i in range(len(b)-1):
            if c[i+1]==b[i+1]:
                c[i] = '0'
            else:
                c[i]='1'
    else:
        d.append('0')
        for i in range(len(b)-1):
            c[i]=c[i+1]
    if len(a)==0:
        return
    del(c[len(b)-1])
    c.append(a[0])
    del(a[0])
shuru()
x = quling(x)
y = quling(y)

for i in x:
    a.append(i)
for i in y:
    b.append(i)

# 被除数添零
for i in range(len(y) - 1):
    a.append('0')


for i in range(len(b)):
    c.append(a[0])
    del(a[0])
jisuan()
for j in range(len(a)+1):
    jisuan()
del(c[len(b)-1])
print('商为：',d)
print('余数为：',c)
os.system('pause')
