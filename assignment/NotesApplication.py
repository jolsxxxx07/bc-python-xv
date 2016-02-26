''' A notes application that creates,
reads, updates and deletes a note instance..'''
	
class NotesApplication(object):
	'''constructor where author and list is initialised'''
	def __init__(self,author,notes_list):

		self.author = author
		if(type(notes_list) is list):
			self.noteslist = notes_list
		else:
			self.noteslist = [notes_list]

	'''create function or add method to list'''
	def create(self,notes_content):
		if notes_content == "" or notes_content == None:
			return "Please Enter Value"
	
		self.noteslist.append(notes_content)
		return notes_content +" added"


	'''function to test author of list'''
	def getAuthor(self):
		return str(self.author)

	def __str__(self):
		size = str(len(self.noteslist))
		return str(self.author +" "+size)


	''' prist the notes with author and count'''
	def list(self):
		count = 0
		for i in self.noteslist:
			
			print("Note ID  %d. " % (count) )
			print(i)
			print("By Author "+self.author)
			count+=1 
		if count == 0:
			return str("Empty notes")
		else:
			return str("List has entries")


	'''gets a note at a given index'''
	def get(self,note_id):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if  note_id >= len(self.noteslist):
			return str(note_id) + " is less than list size"
		return str(self.noteslist[note_id])


	'''function to search through list,returns the text if found'''
	def search(self,search_text):
		textadd = "Showing resultsfor search \"[<"+search_text+">]\""
		textadd=""
		count = 0
		for search in self.noteslist:
			
			if search_text in search:
				textadd+=search +"\n"+"Note ID: %d \n By Author  %s"%(count,self.author)
				count+=1
		if count == 0:

			return str(search_text) +" not available in notes"
		return str(textadd)


	''' deletes an item at a given index'''
	def delete(self,note_id):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if note_id >= len(self.noteslist):
			return str(note_id) +" does not exist in list"
		del self.noteslist[note_id]
		return str(note_id) + " has been successfully deleted"




	''' to edit a previously saved note'''
	def edit(self,note_id,new_content):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if note_id >= len(self.noteslist):
			return str(note_id) +" does not exist in list"
		self.noteslist[note_id] = new_content
		return self.noteslist[note_id]







