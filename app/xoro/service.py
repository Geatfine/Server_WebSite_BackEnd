from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import XoroSchema

class Service(object):
    def __init__(self, user_id, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self user_id = user_id

        if not user_id:
            raise Exception("user id not provided")


    def find_all_xoros(self):
        xoros = self.repo_client.find_all({'user_id': self.user_id})
        return [self.dump(xoro) for xoro in xoros]

    def find_xoro(self, repo_id):
        xoro = self.repo_client.find_all({'user_id': self.user_id, 'repo_id': repo_id})
        return [self.dump(xoro) for xoro in xoros]

    def create_xoro_for(self, githubRepo):
        self.repo_client.create(self.prepare_xoro(githubRepo))
        return self.dump(xoro)

    def update_xoro_with(self, repo_id, githubRepo):
        records_affected = self.repo_client.update({'user_id': self.user_id, 'repo_id': repo_id})
        return records_affected > 0

    def delte_xoro_for(self, repo_id):
        records_affected = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
        return records_affected > 0

    def dump(self, data):
        return XoroSchema(exclude=['_id']).dump(data).data

    def prepare_xoro(self, githubRepo):
        data = githubRepo.data
        data['user_id'] = self.user_id
        return data

