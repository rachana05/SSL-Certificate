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
file_path='C:\Python34\<file_name>'
report=[]
for file in os.listdir(file_path):
	filename=os.path.join(file_path,file)
	with open(filename,'r',encoding='utf8') as f :
		for data in json_parse(f):
			result={}
			try:
				result['ip_address']=data["accepted_targets"][0]["server_info"]["ip_address"]
			except:
				result['ip_address']="N/A"
			try:
				result['hostname']=data["accepted_targets"][0]["server_info"]["hostname"]
			except:
				result['hostname']="N/A"
			try:
							result['highest_version']=data["accepted_targets"][0]["server_info"]["highest_ssl_version_supported"]
			except:
				result['highest_version']="N/A"
			try:				
				result['expiration']=data["accepted_targets"][0]["commands_results"]["certinfo"]["certificate_chain"][0]["notAfter"]
			except:
				result['expiration']="N/A"
			try:
				result['issuer']=data["accepted_targets"][0]["commands_results"]["certinfo"]["certificate_chain"][0]["issuer"]
			except:
				result['issuer']="N/A"
			try:			
				result['sslv2']=data["accepted_targets"][0]["commands_results"]["sslv2"]["accepted_cipher_list"]
			except:
				result['sslv2']="N/A"
			try:
				result['sslv3']=data["accepted_targets"][0]["commands_results"]["sslv3"]["accepted_cipher_list"]
			except:
				result['sslv3']="N/A"
			try:
				result['tlsv1']=data["accepted_targets"][0]["commands_results"]["tlsv1"]["accepted_cipher_list"]
			except:
				result['tlsv1']="N/A"
			try:
				result['tlsv1_1']=data["accepted_targets"][0]["commands_results"]["tlsv1_1"]["accepted_cipher_list"]
			except:
				result['tlsv1_1']="N/A"
			try:
				result['tlsv1_2']=data["accepted_targets"][0]["commands_results"]["tlsv1_2"]["accepted_cipher_list"]
			except:
				result['tlsv1_2']="N/A"
			try:
				result['tlsv1_3']=data["accepted_targets"][0]["commands_results"]["tlsv1_3"]["accepted_cipher_list"]
			except:
				result['tlsv1_3']="N/A"
			
			if result['sslv2']==[] : result['sslv2']="Not Supported"
			elif result['sslv2']=="N/A": result['sslv2']=="N/A"
			else:result['sslv2']="Supported"
			if result['sslv3']==[]: result['sslv3']="Not Supported"
			elif result['sslv3']=="N/A": result['sslv3']=="N/A"
			else: result['sslv3']="Supported"
			if result['tlsv1']==[]: result['tlsv1']="Not Supported"
			elif result['tlsv1']=="N/A": result['tlsv1']=="N/A"
			else: result['tlsv1']="Supported"
			if result['tlsv1_1']==[]: result['tlsv1_1']="Not Supported"
			elif result['tlsv1_1']=="N/A": result['tlsv1_1']=="N/A"
			else: result['tlsv1_1']="Supported"
			if result['tlsv1_2']==[]: result['tlsv1_2']="Not Supported"
			elif result['tlsv1_2']=="N/A": result['tlsv1_2']=="N/A"
			else: result['tlsv1_2']="Supported"
			if result['tlsv1_3']==[]: result['tlsv1_3']="Not Supported"
			elif result['tlsv1_3']=="N/A": result['tlsv1_3']=="N/A"
			else: result['tlsv1_3']="Supported"
	    		report.append(result)
	with open(r'<output_file>','w',newline='') as output:
		fields=['ip_address','hostname','highest_version','sslv2','sslv3','tlsv1','tlsv1_1','tlsv1_2','tlsv1_3','issuer','expiration']
		value=csv.DictWriter(output,fieldnames=fields)
		value.writeheader()
		value.writerows(report)
	
 
