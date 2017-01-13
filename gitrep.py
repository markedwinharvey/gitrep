#!/usr/bin/env python
'''
Simple command-line repository creator for github
'''
import subprocess as sp
import os
import pickle
import sys

user_data_path = os.path.dirname(os.path.abspath(__file__))+'/user_data.p'

def exit():
	print 'exiting...'
	print
	sys.exit()


def enter_data(): 
	'''Enter new username and token, with option to save'''
	user_name = raw_input('Enter new user_name: ')
	token = raw_input('Enter token for this user_name: ')
		
	if ask_ynq('Save this data?') == 'y':
		user_data = {'user_name':user_name,'token':token}
		pickle.dump(user_data, open(user_data_path,'wb'))
	
	return user_name, token


def ask_ynq(msg):
	'''Request user feedback in the form: {y, n, q} based on msg prompt'''
	fb=''
	while fb not in list('ynq'):
		fb = raw_input('%s Type y, n, or q: ' %msg)
	if fb == 'q': exit()
	return fb


def main():
	
	if os.path.exists(user_data_path):						#found saved data
		user_data = pickle.load(open(user_data_path,'rb'))	#load data from file
		user_name = user_data['user_name']
		token = user_data['token']
		
		print 'User data saved as:'
		print '\tuser_name: ',user_name
		print '\ttoken:     ',token
		
		if ask_ynq('Use this data?') == 'n':
			user_name,token = enter_data()					#get new data from user
		
	else:													#data not found
		print 'File user_data.p not found.'					
		user_name,token = enter_data()						#request data

	repo_name = raw_input('Enter new repo name: ')
	repo_desc = raw_input('Enter description: ')
	
	if ask_ynq('Create this repo?') == 'y':
		repo_command = 'curl -u \"'+user_name+':'+token+'\" https://api.github.com/user/repos -d \'{\"name\":\"\''+repo_name+'\'\",\"description\":\"'+repo_desc+'\"}\''
		resp = sp.Popen([repo_command],stdout=sp.PIPE,shell=True).communicate()[0]
		
		print 'Github returned the following information:'
		print resp
	
	
if __name__ == '__main__':

	print
	print '#### gitrep.py: github repo creation in python ####'
	print
	
	main()