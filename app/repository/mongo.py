import os
from pymongo import MongoClient

COLLECTION_NAME = 'xoro'

class MongoRepository(object):
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).xoro
    
    def find_all(self,selector):
        return self.db.xoro.find(selector)

    def find(self, selector):
        return self.db.xoro.find_one(selector)
      
    def create(self, xoro):
        return self.db.xoro.insert_one(xoro)

    def update(self, selector, xoro):
        return self.db.xoro.replace_one(selector,xoro).modified_count

    def delete(self, selector):
        return self.db.xoro.delete_one(selector).delete_count


