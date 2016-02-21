from __future__ import print_function
from colorama import init, Fore, Back, Style
# A simple command line interface that request input from uses to create,
#read, update and delete a note instance..
init()
class AdvancedNoteApplication(object):

	def __init__(self):
		


		print(Fore.GREEN+"Welcome to a new note session")
		print()
		print(Fore.BLUE)
		self.author = input("Please Enter Your Name: ")
		if self.author != "":
			print("Welcome "+self.author +" !")
			print()
			print()

			noteslists = input("Please Enter a note to be stored\n at the first element ")
			self.noteslist = [noteslists]
			if self.noteslist != "":

				print(Fore.GREEN+"Your note has been successfully added !")
			else :
				print(Fore.RED+"Plese, Try entering a note !")

		else :
			print(Fore.RED)
			print("Invalid Author name....")
			print(Fore.GREEN)
			recall = AdvancedNoteApplication()

		print("Please enter ( add_new-> ) to add to note ")
		print("Please enter (edit_new->  index )  to edit a note at the given index")
		print("Please enter (view_new-> ) to view all notes and authors")
		print("Please enter (get_new-> ) to get note")
		print("Pleas enter (search_new->) to search for text in notes")
		print("Please enter (delete_new-> ) to delete note")
		print("Please enter (_new-> ) to get back to the main menu")
		self.answerUserRequest()

	def answerUserRequest(self):
		print()
		print()
		print(Fore.GREEN)
		usercommand = input("Please Enter any of the methods \n or (_new) to see instructions )")
		if usercommand != "":
			if usercommand == "add_new->":
				self.create()
			if usercommand == "get_new->":
				self.get()
			if usercommand =="edit_new->":
				self.edit()
			if usercommand =="view_new->":
				self.list()
			if usercommand =="delete_new->":
				self.delete()
			if usercommand == "_new->":
				self.answerUserRequest()
			print(Fore.RED)
			print("Invalid command")
			print(Fore.GREEN)
			self.answerUserRequest()
	def create(self):
		print()
		print()
		print(Fore.BLUE)
		notes = input("Please Enter The note !!!")
		if notes == "_new->":
			self.answerUserRequest()
		if notes != "" or notes!= None:
			self.noteslist.append(notes)
			print(Fore.GREEN)
			print("Note successfully added ")
			self.answerUserRequest()
		else:
			self.create()

	def get(self):
		print()
		print()
		print(Fore.BLUE)
		try:
			note_id = input("Please Enter the Index for the note : ")
		except ValueError:
			print(Fore.RED)
			print (str(note_id) + " is invalid")
			self.get()

		if note_id == "_new->":
			self.answerUserRequest()
		if note_id >= len(self.noteslist):
			print(Fore.RED)
			print (str(note_id) + " is invalid")
			self.get()
		else:
			print(Fore.GREEN)
			print(str(self.noteslist[note_id]))
			self.answerUserRequest()

	def edit(self):
		print()
		print()
		print(Fore.BLUE)
		try:
		    note_id = int(input("Please Enter the Index for note to edit : "))
		except ValueError:
			print(Fore.RED)
			print("Enter a valid edit id")
			self.edit()

		if note_id == "_new->":
			self.answerUserRequest()
		if  note_id >= len(self.noteslist):
			print(Fore.RED)
			print(str(note_id) +" does not exist in list")
			self.edit()

		getNewContent = input("Please edit the previous value : ")
		if getNewContent == "_new->":
			self.answerUserRequest()
		if getNewContent =='' or getNewContent == None:
			print(Fore.RED)
			print(str(note_id) +" cannot be empty")
			self.edit()
		self.noteslist[note_id] = getNewContent
		print(Fore.GREEN)
		print(self.noteslist[note_id])
		self.answerUserRequest()

	def list(self):
		print(Fore.GREEN)
		count = 0
		for i in self.noteslist:
			
			print("Note ID  %d. " % (count) )
			print(i)
			print("By Author "+self.author)
			count+=1

		self.answerUserRequest()

	def delete(self):
		print()
		print()
		print(Fore.BLUE)
		try:
			note_id = int(input("Please enter node id index to delete : "))
		except ValueError:
			print(Fore.RED)
			print("Please enter a valid digit")
			self.delete()

		
		if note_id == "_new->":
			self.answerUserRequest()
		if note_id >= len(self.noteslist):

			print( str(note_id) +" does not exist in list")
			self.delete()
		del self.noteslist[note_id]
		print(str(note_id) + " has been successfully deleted")
		self.answerUserRequest()


	def search(self):
		search_text = input("Please enter your search text: ")
		if search_text == "_new->":
			self.answerUserRequest()

		textadd = "Showing resultsfor search \"[<"+search_text+">]\""
		textadd=""
		count = 0
		for i in self.noteslist:
			
			if search_text in i:
				textadd+=i +"\n"+"Note ID: %d \n By Author  %s"%(count,self.author)
				count+=1
		if count == 0:
			print(Fore.RED)
			print(str(search_text) +" not available")
			self.search()

		print( str(textadd))
		self.answerUserRequest()




test = AdvancedNoteApplication()
