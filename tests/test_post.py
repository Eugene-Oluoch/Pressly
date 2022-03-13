import unittest
from app.models import Post


class TestBlog(unittest.TestCase):
    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_blog = Post(
            user_id=1,
            title="Test Title",
            content="Test Content",
            date_posted="2022-03-13"
        )

    def test_instance(self):
        """
        Test to check if the blog object is an instance of the Blog class
        """
        self.assertTrue(isinstance(self.new_blog, Post))