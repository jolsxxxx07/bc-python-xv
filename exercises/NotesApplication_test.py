import unittest
from NotesApplication import *


'''20 test cases for class note Application '''

class noteAppplicationTestcase(unittest.TestCase):
    
    ''' testing edit works properly'''
    def test_edit(self):
    	test = NotesApplication("Jolaade",["A Starting note in the Application"])
    	self.assertEqual(test.edit(0,"A Start Up Note"),"A Start Up Note")

	

    ''' test that application does not accept an empty note'''
    def test_empty_add(self):
    	test = NotesApplication("Jolaade",[])
    	self.assertEqual(test.create(""),"Please Enter Value")
    

    '''further testing that none cannot be added to the notes'''
    def test_noneValue_in_add(self):
    	test = NotesApplication("",[])
    	self.assertEqual(test.create(None),"Please Enter Value")
    
    ''' test successful addition of a note'''
    def test_added_Successfully(self):
    	test = NotesApplication("",[])
    	self.assertEqual(test.create("Andela Bootcamp"),test.get(0)+" added")
    
    '''test get index works properly'''
    def test_getIndex(self):
    	test = NotesApplication("Adewale",["I am a boy"])
    	test.create("I am jolaade")
    	test.create("I am babatunde")
    	self.assertEqual(test.get(2),"I am babatunde")
    

    ''' further testing the element identification of get index'''

    def test_get_Index_False_Entry(self):
    	test = NotesApplication("Adewale",["I am a boy"])
    	test.create("I am jolaade")
    	test.create("I am babatunde")
    	self.assertNotEqual(test.get(1),"I am babatunde")
    

    ''' testing edit case for an element that does not exist'''
    def test_edit_False_Entry(self):
    	test = NotesApplication("Adewale ",["I am Jolaade"])
    	test.create("Python is fun")
    	self.assertEqual(test.edit(9,"Add me"),"9 does not exist in list")


    ''' i test passing a string as an index'''
    def test_edit_Invalid_Entry(self):
    	test = NotesApplication("Bootcamp IV ",["Chidi lectures well"])
    	self.assertEqual(test.edit("hello","hi"),"hello is invalid")

    ''' tsting deletetes response to a string used as argument'''
    def test_delete_inValid(self):
    	test = NotesApplication("Adewale",["jolaade"])
    	self.assertEqual(test.delete("jolaade"),"jolaade is invalid")

    '''testing a successful delete method'''
    def test_delete_valid(self):
    	test = NotesApplication("Adewale",["jolaade"])
    	self.assertEqual(test.delete(0),"0 has been successfully deleted")

    '''testing delete on an out of range index'''
    def test_delete_indexOutOfRange_list(self):
    	test = NotesApplication("Adewale",["jolaade"])
    	self.assertEqual(test.delete(2),"2 does not exist in list")
    

    '''test a successful delete '''

    def test_delete_successfully(self):
    	test = NotesApplication("Adewale",["jolaade"])
    	self.assertEqual(test.delete(0),"0 has been successfully deleted")

    ''' test a successfull search using not equal '''
    def test_search_successfully(self):
    	test = NotesApplication("Adewale",["Babatunde"])
    	test.create("adewale")
    	test.create("wale")
    	self.assertNotEqual(test.search("wale"),"wale not available in notes")
    
    ''' test an unsuccessfull search'''
    def test_search_unsuccessfully(self):
    	test = NotesApplication("Adewale",["Babatunde"])
    	test.create("adewale")
    	test.create("wale")
    	self.assertNotEqual(test.search("jadesola"),"wale not available in notes")

    ''' test get list with element above length '''
    def test_invalid_getfromList(self):
    	test = NotesApplication("Chidi",["Bootcamp"])
    	test.create("Halos")
    	self.assertEqual(test.get(3),"3 is less than list size")

    '''test that data entered to search for list index is a valid input e.g an integer'''
    def test_invalid_getfromList(self):
    	test = NotesApplication("Chidi",["Bootcamp"])
    	test.create("Halos")
    	self.assertEqual(test.get("babatu"),"babatu is invalid")

    '''test that list is not empty after occupying it'''
    def test_list_occupied(self):
    	test = NotesApplication("kenny",["adewale"])
    	self.assertEqual(test.list(),"List has entries")


    '''test is list is empty after two insertions and deletions'''
    def test_list_emptied(self):
    	test = NotesApplication("Babatunde",["hello","who are you"])
    	test.delete(0)
    	test.delete(0)
    	self.assertEqual(test.list(),"Empty notes")
    

    ''' test that author is valid'''

    def test_author_entry(self):
    	test = NotesApplication("Babatunde",["hey"])
    	self.assertEqual(test.getAuthor(),"Babatunde")


    def test_toString_valid(self):
    	test = NotesApplication("Jolaade",[])
    	test.create("Babatunde")
    	test.create("James")
    	test.create("Ola")
    	test.create("Badmus")
    	self.assertEqual(str(test),"Jolaade 4")
    
    def test_toString_invalid(self):
    	test = NotesApplication("Jolaade",[])
    	test.create("Babatunde")
    	test.delete(0)
    	test.create("Ola")
    	test.create("Badmus")
    	self.assertNotEqual(test,"Jolaade 3")










if __name__ == '__main__':
    unittest.main()