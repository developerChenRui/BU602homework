#!/home/ec602/anaconda3/bin/python python3.6
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:47:56 2017

# Copyright 2017 ChenRui ruirui@bu.edu
"""
import sys
import numpy as np
import math

def compute_time(ball1,ball2):
    a=((ball1[3]-ball2[3])**2+(ball1[4]-ball2[4])**2)
    b=2*((ball1[1]-ball2[1])*(ball1[3]-ball2[3])+(ball1[2]-ball2[2])*(ball1[4]-ball2[4]))
    c=(ball1[1]-ball2[1])**2+(ball1[2]-ball2[2])**2 - 100
    if b**2-4*a*c<=0|(a==0)&(b==0):
        return -1
    else:
        if a==0:
            ans = (0-c)/b
        else:
            x1 = ((0-b) + (b**2-4*a*c)**0.5)/(2*a)
            x2 = ((0-b) - (b**2-4*a*c)**0.5)/(2*a)
            ans = x2 if ((x1>x2)&(x2>=0)) else x1
        return ans

					
def update_without_collision(data,time):
    for i in range(len(data)):
        data[i][1] = data[i][1]+data[i][3]*time
        data[i][2] = data[i][2]+data[i][4]*time
    
def update_with_collision(data,time,collision_ball):
    update_without_collision(data,time)
    
    for i in collision_ball:
        target_ball1 = collision_ball[i][0]
        target_ball2 = collision_ball[i][1]
        for j in data:
            if j[0]==target_ball1:
                ball1 = j
            if j[0]==target_ball2:
                ball2 = j
        if ball1[1]-ball2[1]==0:
            phi = math.pi/2
        else:
            phi = math.atan((ball1[2]-ball2[2])/(ball1[1]-ball2[1]))
        v1 = (ball1[3]**2+ball1[4]**2)**(0.5)
        v2 = (ball2[3]**2+ball2[4]**2)**(0.5)
        if v1==0:
            theta1 = 0
        else:
            theta1 = math.acos(ball1[3]/v1) #??????????????????
        if v2==0:
            theta2 = 0
        else:
            theta2 = math.acos(ball2[3]/v2) #???????????????????
#        v1 = (ball1[3]**2+ball1[4]**2)**(0.5)
#        v2 = (ball2[3]**2+ball2[4]**2)**(0.5)
            
        ball1[3]=v2*math.cos(theta2-phi)*math.cos(phi)+\
        v1*math.sin(theta1-phi)*math.cos(phi+math.pi/2)
        
        ball1[4]=v2*math.cos(theta2-phi)*math.sin(phi)+\
        v1*math.sin(theta1-phi)*math.sin(phi+math.pi/2)
        
        ball2[3]=v1*math.cos(theta1-phi)*math.cos(phi)+\
        v2*math.sin(theta2-phi)*math.cos(phi+math.pi/2)        
        
        ball2[4]=v1*math.cos(theta1-phi)*math.sin(phi)+\
        v2*math.sin(theta2-phi)*math.sin(phi+math.pi/2)                            
            
    
def current_time_state(data,time):
    ans={}
    collision_flag = 0
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if (compute_time(data[i],data[j])!=-1)&(compute_time(data[i],data[j])>1e-10):
                collision_flag=1
                ans[(data[i][0],data[j][0])] = compute_time(data[i],data[j])
				#ans[data[j][0]] = compute_time(data[i],data[j])
    if collision_flag==1:
        min_time = ans.get(min(ans,key=ans.get))
        if time < min_time:
            update_without_collision(data,time)
        else:
            collision_times=1
            collision_ball={}
            for i in ans:
                if ans[i]==min_time:
                    collision_ball[collision_times]=i
                    collision_times = collision_times+1
                
            update_with_collision(data,min_time,collision_ball)
            current_time_state(data,time-min_time)
    else:
        update_without_collision(data,time)	


def set_format(data):
    ans = ""
    num=0
    for i in data:
        num=num+1
        for j in range(0,5):
            ans = ans + str(i[j]) + ' '
        if num!= len(data):
            ans = ans + '\n'
    print(ans)

def main(argv):
#    print(argv[1])
    target_time = [0]*len(argv)
    for i in range(len(argv)):
        if (argv[i].isdigit()):
            target_time[i] = float(argv[i])
            sorted_time = sorted(target_time)
            data = []
        else:
         #   print(2)
            return 2
            
    i=0  
    for line in sys.stdin:
        data.append([])
        for j in range(5):
            line_list = line.split()
            data[i].append(line_list[j])
        i=i+1
    for i in range(len(data)):
        data[i][1]=float(data[i][1])
        data[i][2]=float(data[i][2])
        data[i][3]=float(data[i][3])
        data[i][4]=float(data[i][4])
# #   print(data)
    
        
 
    current_sum_time = 0
    for i in sorted_time:
        print(i)       
        current_time_state(data,i-current_sum_time)
        set_format(data)
 #       print(data)
        current_sum_time = i
        


    
if __name__=="__main__":
	main(sys.argv[1:])
