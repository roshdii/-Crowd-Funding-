#! /usr/bin/env/ python3.6
## File : Crowd Funding Donating System 
## Author : Eslam Roshdi 
## Email : e.roshdii@gmail.com
## Date : 21 Nov 2019
## Info : e.g kick starter 
## Course : Intro to python
## Instructor : Abd Arahman Hamdy 

import os 
from menu_class import Menu

class User:
	# List of Users
	# add user , delete, edit, view 

	users = []
	no_of_users = 0

	def __init__(self,user_id=no_of_users+1,):
		pass  
		# check values & assign
		# add(self)

	def add(self):
		pass
		# append(self) to list 
		# recursive update 

	def edit(self):
		pass
		# display all info
		# edit whatever 
		# recursive update 

	def delete(self):
		pass
		# remove user obj from list 
		# recursice update 

	def view(self):
		pass
		# display current user info

	########### FILE ######################
	@classmethod
	def recursive_read_users(cls):
		pass 
		# read users file db 
		# convert to user obj 
		# append obj to users list 

	@classmethod
	def recursve_update_users(cls):
		pass
		# loop users list 
		# convert from obj to struct 
		# write to users file 

class Project:
	# List of Projects 
	# Start Project (with st.date / end.date) 
	# End Project (check donation 25% reached)

	projects = []
	no_of_projects = 0 

	def __init__(self,project_id=no_of_projects+1,user_id):
		pass
		# check_values & assign them 
		# start project 

	def start(self):
		pass
		# append(self) in list
		# recursive update project file

	def end(self):
		pass
		# check 25% off and time not passed
		# remove project from list
		# recursive update project file
	
	###### Out Sourceing Searching #######
	@classmethod
	def projects_of_user(cls,user_id):
		pass 
		# display all projects for specific user

	@classmethod
	def projects_of_time(cls,st_date,end_date):
		pass
		# display all projects(may inc. donats) within time search 

	@classmethod
	def all_projects(cls):
		pass
		# display all projects 

	########### FILE ######################
	@classmethod
	def recursive_read_projects(cls):
		pass 
		# read projects file db 
		# convert to project obj 
		# append obj to projects list 

	@classmethod
	def recursve_update_projects(cls):
		pass
		# loop projctss list 
		# convert from obj to struct 
		# write to projects file 


class Donation:
	# List of donations 
	# add a donate with the project id & user id donating 
	# remove a donate (at specfic project / from login user)
	
	dontas = []
	no_of_donats = 0 

	def __init__(self,donate_id=no_of_donats+1,user_id,project_id):
		pass 
		# check & assign values to current donation
		# add (self)

	def add(self):
		pass
		# append donate_obj to list 
		# recursive update donate file 

	def remove(Self):
		pass
		# remove donate with id from list 
		# recursive update donate file


	########## out sourceing search ####################
	@classmethod 
	def donats_of_user(cls,user_id):
		pass
		#search for all donats with user_id 
		#display donats and prespective projects

	@classmethod
	def donats_of_project(cls,project_id):
		pass
		#search for all donats with project_id 
		#display donats and prespective user 

	########### FILE ######################
	@classmethod
	def recursive_read_donats(cls):
		pass 
		# read donate file db 
		# convert to donate obj 
		# append obj to donats list 

	@classmethod
	def recursve_update_donats(cls):
		pass
		# loop donats list 
		# convert from obj to struct 
		# write to donate file 

def Signup:
	pass
	#1 Get Info from user(check if valid) 
	#2 Add USer (check return is ok)
	#3 Re #1 if not ok 
	#4 Back to main 

def Login:
	pass
	#1 check email/pass for user >> if true login_user is selected  
	#2 User menu : Account settings , Projects , Donations , Signout
	#3 Account Setting menu : Edit Info , Delete Account 
	#4 Project Menu : Add project(with data) , view projects(user/all/data) , edit project , Delete project , 
	#5 Donation Menu : project list (donate project / delete donate )
	#6 Sign Out 

def main:
	pass
	#1 main menu : Signup , login 
	#2 signup > go for signup 
	#3 login > go for login 
	#4 Exit


if __name__ == "__main__":
	main()


##############################################################
def check_dir(cls):
	try :
		l = os.listdir(db_dir_name)
		if len(l) > 0 :
			print("Done checking db/ no. of files = ",len(l))
	except FileNotFoundError:
		print("Error in accessing Database directory !!! Creating New db ")
		os.mkdir(db_dir_name)