# ﷽
import os
from pathlib import Path
import sys
input = lambda: sys.stdin.readline().strip()

def get_dict():
    f = open( Path(__file__).with_name('grades.txt'))
    d={}
    for i in f:
        i=i.replace(":"," ")
        i=i.replace("-"," ")
        id,name,grade,birth,gender=i.split()
        if not grade.isdigit():continue
        d[id]={
            'name':name,
            'grade':int(grade),
            'birth':int(birth),
            'gender':gender,
        }
    return d

def get_id_oldest(d):
    tmpid=float('inf')
    tmpgrade=float('inf')
    for id in d:
        if d[id]['birth']< tmpgrade:tmpid=id;tmpgrade=d[id]['birth']
    return tmpid

def average_score(d) :
    return sum([ d[id]['grade'] for id in d ])//len(d)

def gender_of_high_score(d) :
    tmpgrade=-float('inf')
    tmpid=float('inf')
    for id in d:
        if d[id]['grade']>tmpgrade:tmpgrade=d[id]['grade'];tmpid=id
    return d[tmpid]['gender']




dict=get_dict()
# print(dict.keys())
av=average_score(dict)
print("average_score : ",av)
id_oldest=get_id_oldest(dict)
print("id_oldest : ",id_oldest)
gender_hightst=gender_of_high_score(dict)
print("gender_hightst : ",gender_hightst)

