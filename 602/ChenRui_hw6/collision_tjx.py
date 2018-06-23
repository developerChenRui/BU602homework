import sys
import math
import numpy as np
import copy

inputstr = sys.stdin.read()

def main():
    global s
    global time
    global time1
    s = inputstr.splitlines(True)
    time = sys.argv
    del time[0]
    if len(time) == 0:
        exit(2)
    for i in range(0, len(time)):
        try:
            time[i] = float(sys.argv[i])
        except:
            exit(2)
    for i in range(0, len(s)):
        s[i] = s[i].split()
        if len(s[i]) != 5:
            exit(1)
        for j in range(1, 5):
            try:
                s[i][j] = float(s[i][j])
            except:
                exit(1)
    time.append(0)
    time=sorted(time)
    for i in range(0,len(time)):
        if time[0]<0:
            del time[0]
    if len(time)==1:
        exit(2)
    time1=[0]*(len(time)-1)
    for i in range(0,len(time)-1):
        time1[i]=time[i+1]-time[i]
    output()

            
def distance(x1,y1,x2,y2):
    return math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))

def swap_v(i1,i2):
    v1= np.array([s[i1][3], s[i1][4]])
    v2= np.array([s[i2][3], s[i2][4]])
    x1= np.array([s[i1][1], s[i1][2]])
    x2= np.array([s[i2][1], s[i2][2]])
    vv1= v1-np.dot((v1-v2), (x1-x2))*(x1-x2)/100
    vv2= v2-np.dot((v2-v1), (x2-x1))*(x2-x1)/100
    s[i1][3] = vv1[0]
    s[i1][4] = vv1[1]
    s[i2][3] = vv2[0]
    s[i2][4] = vv2[1]

def solve(a,b,c):
    if a!=0 and (b*b-4*a*c)>=0:
        x=np.roots([a,b,c])
        x1=float(x[0])
        x2=float(x[1])
        if x1>x2:
            if x1>0 and x2>0:
                return x2
            elif x1<0 and x2>0:
                return x2
            elif x1>0 and x2<0:
                return x1
            elif x1<0 and x2<0:
                return 0
        elif x1<x2:
            if x1>0 and x2>0:
                return x1
            elif x1<0 and x2>0:
                return x2
            elif x1>0 and x2<0:
                return x1
            elif x1<0 and x2<0:
                return 0
        else:
            if x1>=0:
                return x1
            else:
                return 0
    else: 
        if a==0 and b!=0:
            if (-c/b)>0:
                return (-c/b)
            else:
                return 0
        else:
            return 0


def collidetime(x1,y1,vx1,vy1,x2,y2,vx2,vy2):
    if distance(x1,y1,x2,y2)<10:
        return 0
    else:
        a=(vx1-vx2)*(vx1-vx2)+(vy1-vy2)*(vy1-vy2)
        b=2*(x1*vx1+x2*vx2+y1*vy1+y2*vy2-x1*vx2-x2*vx1-y1*vy2-y2*vy1)
        c=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)-100 
        return solve(a,b,c)
    
def collisioncase(time_index):
    t1=[]
    i1=[]
    j1=[]
    for i in range(0,len(s)-1):
        for j in range (i+1,len(s)):
            t0=collidetime(s[i][1],s[i][2],s[i][3],s[i][4],s[j][1],s[j][2],s[j][3],s[j][4])
            if type(t0)==float and t0>=0:
                t1.append(t0)
                i1.append(i)
                j1.append(j)
    if t1:
        tmin=min(t1)
        index=t1.index(tmin)
        i2=i1[index]
        j2=j1[index]
    else:
        tmin=0

    if tmin>=time1[time_index] or tmin==0:
        for i in range(0,len(s)):
            s[i][1]+=s[i][3]*time1[time_index]
            s[i][2]+=s[i][4]*time1[time_index]        
        printout(s)
    else:
        for i in range(0,len(s)):
            s[i][1]+=s[i][3]*tmin
            s[i][2]+=s[i][4]*tmin       
        swap_v(i2,j2)
        time1[time_index]-=tmin
        return(collisioncase(time_index))
        
def printout(list1):
    str1=copy.deepcopy(list1)
    for i in range(0,len(list1)):
        if i!=(len(list1)-1):
            str1[i].append('\n')
        else:
            str1[i].append('')
        for j in range(1,6):
            str1[i][j]=str(str1[i][j])
        str1[i]=" ".join(str1[i])
    str1="".join(str1)
    print(str1)

def output():
    for i in range(0,len(time1)):
        print(time[i+1])
        collisioncase(i)

if __name__ == '__main__':
    main()
