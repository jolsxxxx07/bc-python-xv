class NotesApplication(object):
	# A notes application that creates,
#reads, updates and deletes a note instance..
	
	def __init__(self,author,notes_list):

		self.author = author
		if(type(notes_list) is list):
			self.noteslist = notes_list
		else:
			self.noteslist = [notes_list]

		

	def create(self,notes_content):
		if notes_content == "" or notes_content == None:
			return "Please Enter Value"
	
		self.noteslist.append(notes_content)
		return notes_content +" added"

	def getAuthor(self):
		return str(self.author)

	def __str__(self):
		size = str(len(self.noteslist))
		return str(self.author +" "+size)



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

	def get(self,note_id):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if  note_id >= len(self.noteslist):
			return str(note_id) + " is less than list size"
		return str(self.noteslist[note_id])

	def search(self,search_text):
		textadd = "Showing resultsfor search \"[<"+search_text+">]\""
		textadd=""
		count = 0
		for i in self.noteslist:
			
			if search_text in i:
				textadd+=i +"\n"+"Note ID: %d \n By Author  %s"%(count,self.author)
				count+=1
		if count == 0:

			return str(search_text) +" not available in notes"
		return str(textadd)

	def delete(self,note_id):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if note_id >= len(self.noteslist):
			return str(note_id) +" does not exist in list"
		del self.noteslist[note_id]
		return str(note_id) + " has been successfully deleted"

    
	def edit(self,note_id,new_content):
		try:
			note_id = int(note_id)
		except ValueError:
			return str(note_id) + " is invalid"
		if note_id >= len(self.noteslist):
			return str(note_id) +" does not exist in list"
		self.noteslist[note_id] = new_content
		return self.noteslist[note_id]



test = NotesApplication("Jolaade","Funke is a goat")
test.create("And a monkey")
print(test.get(0))
print(test.list())
test.edit(0,"I love me")
test.create("Hello boy")
test.create("Hey world")
test.create("Real world problem")
print()
print()
print(test.list())
print()
print()
print(test)



