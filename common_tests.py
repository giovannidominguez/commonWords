import unittest
import commonModule

class common_tests(unittest.TestCase):

    def testRemoveTop100(self):
        self.assertEqual(commonModule.removeTop100(""), "")
        self.assertEqual(commonModule.removeTop100("123"), "123")  
        self.assertEqual(commonModule.removeTop100("the word"), "word")
        self.assertEqual(commonModule.removeTop100("the be to hello this is a test today"), "hello is test today")
    
    def testCreateCall(self):
        self.assertEqual(commonModule.createCall(20122494), "https://hacker-news.firebaseio.com/v0/item/20122494.json?print=pretty")
        self.assertEqual(commonModule.createCall(0), "https://hacker-news.firebaseio.com/v0/item/0.json?print=pretty")
        self.assertEqual(commonModule.createCall(''), "https://hacker-news.firebaseio.com/v0/item/.json?print=pretty")
        self.assertEqual(commonModule.createCall('20122494'), "https://hacker-news.firebaseio.com/v0/item/20122494.json?print=pretty")
    
    def testGetTitle(self):
        self.assertEqual(commonModule.getTitle(20122494), None)
        self.assertEqual(commonModule.getTitle('string'), '')
        self.assertEqual(commonModule.getTitle(8863), 'My YC app: Dropbox - Throw away your USB drive')
    
    def testGetCommentIds(self):
        self.assertEqual(commonModule.getCommentIds(20129184), None) 
        self.assertListEqual(commonModule.getCommentIds(8863), [ 9224, 8917, 8952, 8884, 8887, 8869, 8958, 8940, 8908, 9005, 8873, 9671, 9067, 9055, 8865, 8881, 8872, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8870, 8878, 8980, 8934, 8943, 8876 ])
        self.assertListEqual(commonModule.getCommentIds(21211), [ 21250 ])
    
    def testgetComment(self):
        self.assertEqual(commonModule.getComment(8863), None)
        self.assertEqual(commonModule.getComment(21221), "I'm sorry, I read the title very quickly and misread it.  My opinion on the actual question is that I generally like it when the log in is the email address and there is a separate display name.  This way the username is easy to remember, but the email address remains private.")

    def testFrequency(self):
        test1 = [('the', 1)]
        test2 = [('three', 3),('two', 2), ('one', 1)]
        self.assertListEqual(commonModule.wordFrequency('the', 1), test1)
        self.assertListEqual(commonModule.wordFrequency('the', 3), test1)
        self.assertListEqual(commonModule.wordFrequency('three three three two two one', 3), test2)