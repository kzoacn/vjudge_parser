# -*- coding: utf-8 -*-  
import json
import sys

if len(sys.argv)!=3:
	print("Error! python3 vjudge_parser.py <in> <out>")
	sys.exit(0)

fin=open(sys.argv[1],"r")
fout=open(sys.argv[2],"w")

data=json.load(fin)
lst=[]
name=data['participants']
sub=data['submissions']

for l in sub:
	dic={}
	dic['user']=name[str(l[0])][0]
	dic['problem']=chr(ord('A')+l[1])
	dic['is_accepted']=(l[2]==1)
	dic['time']=l[3]
	lst.append(dic)

json.dump(lst,fout, ensure_ascii=False)
