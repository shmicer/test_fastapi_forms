from pymongo import MongoClient
from envparse import Env

env = Env()
MONGODB_URL = env.str('MONGODB_URL', default='mongodb://localhost:27017/test_collection')

client = MongoClient(MONGODB_URL)

db = client.test_collection

template_collection = db['test_collection']
