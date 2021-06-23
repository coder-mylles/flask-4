import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    '''
   Test Class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_comment = Comment(id = 2, comment = "Hope it works", posted = 2019/9/23, post_id = 1, user_id = 1)
        
        
    def tearDown(self):
        Comment.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,3)
        self.assertEquals(self.new_comment.comment,"Hope it works")
        self.assertEquals(self.new_comment.posted,2019/9/23)
        self.assertEquals(self.new_comment.user_id,4)
        self.assertEquals(self.new_comment.blog_id,2)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(4)
        self.assertTrue(len(got_comments) == 1)
        