import cherrypy

class ResetController:
	def __init__(self, mdb):
		self.mdb = mdb
	def RESET_ALL(self):
		output = {'result':'success'}
		mdb.load_movies('data/movies.dat')
		mdb.load_users('data/users.dat')
		mdb.load_ratings('data/ratings.dat')
		mdb.load_images('data/images.dat')

		return json.dumps(output)

	def RESET(self, key):
		output = {'result':'success'}
		mdb.load_movie('data/movies.dat', int(key))
