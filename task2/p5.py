from pathlib import Path


from p4 import get_dict
dict=get_dict()

f = open( Path(__file__).with_name('filtered.txt'),'w')
for i in dict:
    name=dict[i]['name']
    birth=dict[i]['birth']
    f.write(f'{i} {name} - {birth}  \n')
