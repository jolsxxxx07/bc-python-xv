import unittest
from NotesApplication import *

#20 test cases for class noteapplication
#i have 1 failure because i want to gain knowledge on why
#my tostring method is not called implicitly while testing
#its a bit broad on research... lazy programmers

class noteAppplicationTestcase(unittest.TestCase):
 
	def test_edit(self):
		test = NotesApplication("Jolaade",["A Starting note in the Application"])
		self.assertEqual(test.edit(0,"A Start Up Note"),"A Start Up Note")

	


	def test_empty_add(self):
		test = NotesApplication("Jolaade",[])
		self.assertEqual(test.create(""),"Please Enter Value")
    # double check for empty add parameter, please fix then when reviewing
	def test_noneValue_in_add(self):
		test = NotesApplication("",[])
		self.assertEqual(test.create(None),"Please Enter Value")

	def test_addedSuccessfully(self):
		test = NotesApplication("",[])
		self.assertEqual(test.create("Andela Bootcamp"),test.get(0)+" added")

	def test_getIndex(self):
		test = NotesApplication("Adewale",["I am a boy"])
		test.create("I am jolaade")
		test.create("I am babatunde")
		self.assertEqual(test.get(2),"I am babatunde")

	def test_getIndexFalseEntry(self):
		test = NotesApplication("Adewale",["I am a boy"])
		test.create("I am jolaade")
		test.create("I am babatunde")
		self.assertNotEqual(test.get(1),"I am babatunde")

	def test_edit_False_Entry(self):
		test = NotesApplication("Adewale ",["I am Jolaade"])
		test.create("Python is fun")
		self.assertEqual(test.edit(9,"Add me"),"9 does not exist in list")

	def test_edit_InvalidEntry(self):
		test = NotesApplication("Bootcamp IV ",["Chidi lectures well"])
		self.assertEqual(test.edit("hello","hi"),"hello is invalid")


	def test_delete_inValid(self):
		test = NotesApplication("Adewale",["jolaade"])
		self.assertEqual(test.delete("jolaade"),"jolaade is invalid")

	def test_delete_valid(self):
		test = NotesApplication("Adewale",["jolaade"])
		self.assertEqual(test.delete(0),"0 has been successfully deleted")

	def test_delete_indexOutOfRange_list(self):
		test = NotesApplication("Adewale",["jolaade"])
		self.assertEqual(test.delete(2),"2 does not exist in list")

	def test_delete_successfully(self):
		test = NotesApplication("Adewale",["jolaade"])
		self.assertEqual(test.delete(0),"0 has been successfully deleted")


	def test_search_successfully(self):
		test = NotesApplication("Adewale",["Babatunde"])
		test.create("adewale")
		test.create("wale")
		self.assertNotEqual(test.search("wale"),"wale not available in notes")

	def test_search_unsuccessfully(self):
		test = NotesApplication("Adewale",["Babatunde"])
		test.create("adewale")
		test.create("wale")
		self.assertNotEqual(test.search("jadesola"),"wale not available in notes")


	def test_invalid_getfromList(self):
		test = NotesApplication("Chidi",["Bootcamp"])
		test.create("Halos")
		self.assertEqual(test.get(3),"3 is less than list size")

    #test that data entered to search for list index is a valid input e.g an integer
	def test_invalid_getfromList(self):
		test = NotesApplication("Chidi",["Bootcamp"])
		test.create("Halos")
		self.assertEqual(test.get("babatu"),"babatu is invalid")

    #test that list is not empty after occupying it
	def test_list_occupied(self):
		test = NotesApplication("kenny",["adewale"])
		self.assertEqual(test.list(),"List has entries")


    #test is list is empty after two insertions and deletions
	def test_list_emptied(self):
		test = NotesApplication("Babatunde",["hello","who are you"])
		test.delete(0)
		test.delete(0)
		self.assertEqual(test.list(),"Empty notes")
    # test that author is valid
	def test_author_entry(self):
		test = NotesApplication("Babatunde",["hey"])
		self.assertEqual(test.getAuthor(),"Babatunde")
    
	def test_toString_valid(self):
		test = NotesApplication("Jolaade",[])
		test.create("Babatunde")
		test.create("James")
		test.create("Ola")
		test.create("Badmus")
		self.assertEqual(test,"Jolaade 4")
    #sample
	def test_toString_invalid(self):
		test = NotesApplication("Jolaade",[])
		test.create("Babatunde")
		test.delete(0)
		test.create("Ola")
		test.create("Badmus")
		self.assertNotEqual(test,"Jolaade 3")










if __name__ == '__main__':
    unittest.main()