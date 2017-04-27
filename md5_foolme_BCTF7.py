import sys
import os
import random
import time
import base64
import string
import hashlib
SALT_LEN = 10
HEX_LEN = 4

def base_str():
	return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
def random_string(length):
	string = [random.choice(base_str()) for i in range(length)]
	return ("".join(string))
	
def find_string(salt,submd5):
	md5=hashlib.md5()
	inp=random_string(20)
	value=inp+salt
	md5=hashlib.md5()
	md5.update(value.encode("utf-8"))
	md5value=md5.hexdigest()
	while md5value[:HEX_LEN]!=submd5:
		inp=random_string(20)
		value=inp+salt
		md5=hashlib.md5()
		md5.update(value.encode("utf-8"))
		md5value=md5.hexdigest()
		print(md5.hexdigest()[:HEX_LEN])
	print(inp)
	return inp
	

def main():
	'''
	salt=random_string(SALT_LEN)
	tmpvalue=random_string(20)+salt
	md5=hashlib.md5()
	md5.update(tmpvalue.encode("utf-8"))
	submd5=md5.hexdigest()[:4]
	'''
	print ("salt:")
	salt=sys.stdin.readline()[:-1]
	print("submd5:")
	submd5=sys.stdin.readline()[:-1]
	print ("[*]Proof of work:")
	print ("\tMD5(key+\"%s\")[:4]==%s"%(salt,submd5))
	print ("[+]Give me the key:")
	sys.stdout.flush()
	
	value=find_string(salt,submd5)+salt
	
	sys.stdout.flush()
	
	md5=hashlib.md5()
	md5.update(value.encode("utf-8"))
	md5value=md5.hexdigest()
	
	print(md5value[:HEX_LEN])
	print(submd5)
	
	if(md5value[:HEX_LEN]!=submd5):
		print ("[-]Access Failed")
		return
main()