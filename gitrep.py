#!/usr/bin/env python
'''
Simple command-line repository creator for github
'''
import subprocess
import os
import pickle
import sys

def exit():
	print 'exiting...'
	print
	sys.exit()

def enter_data(): 
	#Enter new username and token, with option to save
	user_name = raw_input('Enter new user_name: ')
	token = raw_input('Enter token for this user_name: ')
	save = ''
	while save not in list('ynq'):
		save = raw_input('Save this data? Enter y, n, or q: ')
	if save == 'q':
		exit()
	elif save == 'y':
		user_data = {'user_name':user_name,'token':token}
		pickle.dump(user_data,open('user_data.p','wb'))
	return user_name, token

def main():
	print
	print '#### gitrep.py: github repo creation in python ####'
	print
	
	if os.path.exists('user_data.p'):						#found saved data
		user_data = pickle.load(open('user_data.p','rb'))	#load data from file
		user_name = user_data['user_name']
		token = user_data['token']
		print 'User data saved as:'
		print '\tuser_name: ',user_name
		print '\ttoken:     ',token
		use_this = ''
		while use_this not in list('ynq'):
			use_this = raw_input('Use this data? Type y, n, or q: ')	#use saved data?
		if use_this == 'q':
			exit()
		elif use_this == 'n':
			user_name, token = enter_data()	#get new data from user
	else:
		print 'File user_data.p not found.'
		user_name,token = enter_data()

	repo_name = raw_input('Enter new repo name: ')
	repo_desc = raw_input('Enter description: ')
	repo_command = 'curl -u \"'+user_name+':'+token+'\" https://api.github.com/user/repos -d \'{\"name\":\"\''+repo_name+'\'\",\"description\":\"'+repo_desc+'\"}\''
	create_repo = ''
	while create_repo not in list('ynq'):
		create_repo = raw_input('Create this repo? Type y, n, or q: ')
	if create_repo == 'y':
		proc=subprocess.Popen([repo_command],stdout=subprocess.PIPE,shell=True)
		(response,err)=proc.communicate()
		print 'Github returned the following information:'
		print response	
	else:
		exit()
	
if __name__ == '__main__':
	main()