import unittest
from pydiner import Diner
import redis

r = redis.Redis()

class TestIncrement(unittest.TestCase):
    def setUp(self):
        self.diner = Diner(key='awesometestkey')
        self.diner.incr('awesometestvalue', 10)

    def tearDown(self):
        r.delete('diner:awesometestkey')

    def test_creation(self):
        self.assertEquals(r.exists('diner:awesometestkey'), True)

    def test_increment(self):
        diner = self.diner
        self.assertEquals(r.zscore('diner:awesometestkey', 'awesometestvalue'), 10)
                                                                            
class TestRank(unittest.TestCase):
    def setUp(self):
        self.diner = Diner(key='awesometestkey3')
        self.diner.incr('awesometestvalue1', 20)
        self.diner.incr('awesometestvalue2', 40)
        self.diner.incr('awesometestvalue3', 100)

    def tearDown(self):
        r.delete('diner:awesometestkey3')

    def test_rank(self):
        diner = self.diner
        self.assertEquals(diner.rank('awesometestvalue2'),
                '[{"diner_key":"awesometestkey3"},{"rank":1,"element":"awesometestvalue2"}]')




if __name__ == '__main__':
    unittest.main()

	

