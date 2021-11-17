#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 02:14:26 2021

@author: ian
"""
import re
data=[]
#读取数据集
file = open("/home/ian/perfectmom/李节~富林泛泰聚氨酯砂浆.txt",encoding='utf-8')
last_name=''
name=''
multiLine=''
flag=0
count=0
keyNoise=['的口令红包','邀请加入','申请加入','点击查看','撤回了','(无)','对方已成功接收']
for line in file:
    #去除空行
    line=line.strip().replace('\n','')
    if(len(line)==0):
        continue
    # #去噪
    # if(len(line)>4 and (line[:4]=='消息记录' or line[:4]=='消息分组' or line[:4]=='消息对象' or line[:4]=='===='  
    #   or line[:4]=='http' or line[:6]=='[QQ红包]' or line[:3]=='管理员')):
    #     continue
    # continueflag=False
    # for s in keyNoise:
    #     if(s in line):
    #         continueflag=True
    # if(continueflag):
    #     continue
    # #同一个聊天对象的多行连接起来
    if(line[:12]=='李节~富林泛泰聚氨酯砂浆' or line[:4]=='YiAn'):
        name=line.split(' ')[0]
        if(name==last_name):
            flag=1
        else:
            flag=0
            last_name=name
            #print(name)
        # continue
    if(line[:12]=='李节~富林泛泰聚氨酯砂浆' ):
        line=line[38:]
    elif(line[:4]=='YiAn'):
        line=line[30:]
    
    if(flag==1):
        multiLine+=(' '+line)
        continue
    else:
        temp=line
        line=multiLine.replace('\n','')
        multiLine=temp
        
    if(name=='YiAn'):#添加“我”标记
        multiLine='SON'+temp
    else:#添加“朋友”标记
        multiLine='MOM'+temp
    #去除@某人的消息
    obj=re.findall( r'(@\S*\s)',line)
    for s in obj:
        line=line.replace(s,'')
    #去除图片和表情
    line=line.replace('[图片]','')
    line=line.replace('[语音]','')
    line=line.replace('[表情]','')
    line=line.strip()
    #去除空行
    if(len(line)==3):
        continue
    data.append(line)
    count+=1
    if(count==30678):#我这里只提取前30678行
        break
print(count)
#写入数据
with open('/home/ian/perfectmom/data.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(data))
    
    

input_text=[]
target_text=[]
for i in range(len(data)-1):
    if(data[i][:3]=='MOM' and data[i+1][:3]=='SON'):
        input_text.append(data[i][3:].strip())
        target_text.append(data[i+1][3:].strip())
        
with open('son.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(target_text))
with open('mom.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(input_text))
