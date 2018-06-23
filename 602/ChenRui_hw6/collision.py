#!/usr/bin/env python
#!/home/ec602/anaconda3/bin/python python3.6
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:47:56 2017

# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 lyz lyz95222@bu.edu
"""
import sys

def compute_time(ball1,ball2,distance):
    a=((ball1[3]-ball2[3])**2+(ball1[4]-ball2[4])**2)
    b=2*((ball1[1]-ball2[1])*(ball1[3]-ball2[3])+(ball1[2]-ball2[2])*(ball1[4]-ball2[4]))
#    if (a==0)&(b==0):
#        return -1
    c=(ball1[1]-ball2[1])**2+(ball1[2]-ball2[2])**2 - distance**2
    delta = b**2-4*a*c

    if delta<=0:
        return [(a*((0.00000000001)**2)+b*(0.00000000001)+c),-1]
    else:
        if a==0:
            ans = (0-c)/b
        else:             
            x1 = ((0-b) + (delta)**0.5)/(2*a)
            x2 = ((0-b) - (delta)**0.5)/(2*a)
            ans = x2 if ((x1>x2)&(x2>=0)) else x1
        return [(a*((0.00000000001)**2)+b*(0.00000000001)+c),ans]

					
def update_without_collision(data,time):
    for i in range(len(data)):
        data[i][1] = data[i][1]+data[i][3]*time
        data[i][2] = data[i][2]+data[i][4]*time
    
def update_with_collision(data,time,collision_ball):
    update_without_collision(data,time)
#    already_have=0
#    ball_mul ={}
#########################find mul collision balls###############################        

         
########################################################
    for i in collision_ball:


        target_ball1 = collision_ball[i][0]
        target_ball2 = collision_ball[i][1]

        for j in data:
            if (j[0]==target_ball1):
                ball1 = j
#                already_have = 1
            if j[0]==target_ball2:
                ball2 = j 

#        v1=np.array([ball1[3],ball1[4]])-(np.array([ball1[1],ball1[2]])-np.array([ball2[1],ball2[2]]))*(np.dot(np.array([ball1[3],ball1[4]])-np.array([ball2[3],ball2[4]]),(np.array([ball1[1],ball2[2]])-np.array([ball2[1],ball2[2]]))))/100
#        v2=np.array([ball2[3],ball2[4]])-(np.array([ball2[1],ball2[2]])-np.array([ball1[1],ball1[2]]))*(np.dot(np.array([ball2[3],ball2[4]])-np.array([ball1[3],ball1[4]]),(np.array([ball2[1],ball2[2]])-np.array([ball1[1],ball1[2]]))))/100
#        ball1[3]=v1[0]
#        ball1[4]=v1[1]
#        ball2[3]=v2[0]
#        ball2[4]=v2[1]        
                ##################################
        delta_x = ball1[1]-ball2[1]
        delta_y = ball1[2]-ball2[2]
        delta_vx = ball1[3]-ball2[3]
        delta_vy = ball1[4]-ball2[4]
        dot = (delta_x*delta_vx+delta_y*delta_vy)/100
        
#        temp_ball1_3[num]=ball1[3]-dot*delta_x
#        temp_ball1_4[num]=ball1[4]-dot*delta_y
#        temp_ball2_3[num]=ball2[3]+dot*delta_x
#        temp_ball2_4[num]=ball2[4]+dot*delta_y 
#        num=num+1
#        if (delta_x == 0):
#            tempv = ball1[4]
#            ball1[4]=ball2[4]
#            ball2[4]=tempv
#
#        elif (delta_y == 0):
#            tempv = ball1[3]
#            ball1[3]=ball2[3]
#            ball2[3]=tempv
#            
#        else:
#        if ball1[0] not in ball_mul:
 #       if (compute_time(ball1,ball2,9.99)>1e-15):
        ball1[3]=ball1[3]-dot*delta_x
        ball1[4]=ball1[4]-dot*delta_y
        ball2[3]=ball2[3]+dot*delta_x
        ball2[4]=ball2[4]+dot*delta_y
        
#        else:
#            ball_mul[ball1[0]][0]=ball1[3]-dot*delta_x + ball_mul[ball1[0]][0]
#            ball_mul[ball1[0]][1]=ball1[4]-dot*delta_y + ball_mul[ball1[0]][1]
            
#        if ball2[0] not in ball_mul:

#        else:
#            ball_mul[ball2[0]][0]=ball2[3]+dot*delta_x + ball_mul[ball1[0]][0]
#            ball_mul[ball2[0]][1]=ball2[4]+dot*delta_y + ball_mul[ball1[0]][1]
  
#    num=0
#    for i in collision_ball:        
#        target_ball1 = collision_ball[i][0]
#        target_ball2 = collision_ball[i][1]
#        for j in data:
#            if (already_have==0)&(j[0]==target_ball1):
#                ball1 = j
#                already_have = 1
#            elif j[0]==target_ball2:
#                ball2 = j
#        
#        ball1[3]=temp_ball1_3[num]
#        ball1[4]=temp_ball1_4[num]
#        ball2[3]=temp_ball2_3[num]
#        ball2[4]=temp_ball2_4[num]
#        num = num +1
                  
            
    
def current_time_state(data,time):
    ans={}
    collision_flag = 0
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            [flag_0,chech_time] = compute_time(data[i],data[j],10)
            if (chech_time!=-1)&(chech_time>9e-15)|((round(chech_time,2)==0)&(flag_0<=0)):
                collision_flag=1
                ans[(data[i][0],data[j][0])] = chech_time
				#ans[data[j][0]] = compute_time(data[i],data[j])
    if collision_flag==1:
        min_time = ans.get(min(ans,key=ans.get))
        if time <= min_time:
            update_without_collision(data,time)
        else:
            collision_times=1
            collision_ball={}
            for i in ans:
                if ans[i]<=(min_time+0.00000001):
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
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
def input_format_error(line):
    line_split = line.split()
#    print(line_split)
    if len(line_split)!=5:
#        print(1.1)
        return 1
    for i in range(1,len(line_split)):
#        print(type(line_split[i]))
        if is_number(line_split[i]):
            pass
        else:
            return 1
#        value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
#        result = value.match(line_split[i])
#        if result is None:
##            print(line_split[i])
##            print(is_number(line_split[i]))
#            if is_number(line_split[i]):
##                print(0)
#                return 0
#            else:
##                print(1.2)
#                return 1
#    print(0)
    return 0
#def float_num(x):
#	return float(x)



def main(argv):
#    print(argv)
#    return 1
    has_valid_number=0    
#    target_time = [0]*len(argv)
    target_time=[]
    for i in range(len(argv)):
        if (is_number(argv[i])):
            if float(argv[i])>0:
                has_valid_number = 1
                target_time.append(float(argv[i]))                      
#            print(2)
        else:
            sys.exit(2)
        
    if has_valid_number==0:
        sys.exit(2)
    sorted_time = sorted(target_time)
#    print(sorted_time)
    data = []      
    i=0  
    bad_input_flag=0
    try:
        while 1:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.split('\n')
            line=line[0]
#            line = line.split()
            if input_format_error(line)==1:
#                print('111111111111111111111')
#                sys.exit(1)
                bad_input_flag=1
                break
            else:
                data.append([])
                line_list = line.split()
                for j in range(5):
                    if j>0:
                        line_list[j]=float(line_list[j])
                    data[i].append(line_list[j])
                i=i+1
            
    except:
        pass
#    for i in range(len(file)-1):
#        line = file[i]
##    for line in sys.stdin:
##        print(line)
#        if input_format_error(line)==1:
#            return 1
#        else:
#            data.append([])
#            for j in range(5):
#                line_list = line.split()
#                data[i].append(line_list[j])
#            i=i+1
    if bad_input_flag:
 #       print('111111111111111')
        sys.exit(1)

#    for i in range(len(data)):
#        data[i][1]=float(data[i][1])
#        data[i][2]=float(data[i][2])
#        data[i][3]=float(data[i][3])
#        data[i][4]=float(data[i][4])
#    print(data)
#    
#        
# 
#    print('111111111111111')
    current_sum_time = 0
    for i in sorted_time:
        print(i)       
        current_time_state(data,i-current_sum_time)
        set_format(data)
 #       print(data)
        current_sum_time = i
    
        


    
if __name__=="__main__":
    main(sys.argv[1:])
    
