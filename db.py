from flask_pymongo import PyMongo
import server as s

s.app.config['MONGO_DBNAME'] = 'db_name'
s.app.config['MONGO_URI'] = 'mongodb://db_name:db_password@ds123619.mlab.com:23619/db_table_name'
mongo = PyMongo(s.app)
