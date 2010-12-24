import urllib
import urllib2
from urllib2 import HTTPError

BASE_URL = "http://localhost:4567"

class DinerError(Exception):
    def __init__(self, msg, error_code=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class Diner(object):
    def __init__(self, key):
        self.key = key

    def incr(self, element, score):
        url = '%s/%s' % (BASE_URL, self.key)
        params = {
            'element': element,
            'score': score,
            'command': 'increment'
        }

        try:
            data = urllib.urlencode(params)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req).read()
            return response
        except HTTPError, e:
            raise DinerError("Didn't increment. %s" %(e))

    def card(self):
        url = '%s/%s?command=%s' % (BASE_URL, self.key, 'card')
        try:
            response = urllib2.urlopen(url).read()
            return response
        except HTTPError, e:
            raise DinerError("Didn't return cardinality. %s" %(e))           
           
    def rank(self, element):
        url = '%s/%s?command=%s&element=%s' % (BASE_URL, self.key, 'rank', element)
        try:
            response = urllib2.urlopen(url).read()
            return response
        except HTTPError, e:
            raise DinerError("Didn't return rank. %s" %(e))

    def score(self, element):
        url = '%s/%s?command=%s&element=%s' % (BASE_URL, self.key, 'score', element)
        try:
            response = urllib2.urlopen(url).read()
            return response
        except HTTPError, e:
            raise DinerError("Didn't return score. %s" %(e))



