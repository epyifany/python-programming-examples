import cherrypy
import json

class RatingController:
	def __init__(self, mdb):
		self.mdb = mdb
	def GET(self, key):
		output = {'result':'success'}
		mid = int(key)
		output['movie_id'] = mid

		try:
			output['rating'] = mdb.get_rating(mid)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
