import os
import json
import sys
import csv
import io
from json import JSONDecoder
from functools import partial
report=[]
count=0
def json_parse(fileobj, decoder=JSONDecoder(), buffersize=2048):
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
         buffer += chunk
         while buffer:
             try:
                 result, index = decoder.raw_decode(buffer)
                 yield result
                 buffer = buffer[index:]
             except ValueError:
                 # Not enough data to decode, read more
                 break
file_path='<file_path>'
report=[]

for file in os.listdir(file_path):
	filename=os.path.join(file_path,file)
	with open(filename,'r',encoding='utf8') as f :
		for data in json_parse(f):
			result={}
			result['<child1>']=data.get('<parent>').get('<child1>')
			result['<child2>']=data.get('<parent>').get('<child2>')
			report.append(result)
	with open(r'<file_path>','w',newline='') as output:
		fields=['<child1>','<child2>']
		value=csv.DictWriter(output,fieldnames=fields)
		value.writeheader()
		value.writerows(report)
	

				
			
			
			
			
	