import cherrypy
import json

class RecommendationController:
	def __init__(self, mdb):
		self.mdb = mdb
	def DELETE(self):
		output = {'result':'success'}

		return json.dumps(output)

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)
		rec = mdb.get_highest_unrated_movie(key)

		try:
			output['movie_id'] = rec
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		uid = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		mid = int(the_body['movie_id'])
		rating = int(the_body['rating'])

		try:
			mdb.set_user_movie_rating(uid, mid, rating)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
