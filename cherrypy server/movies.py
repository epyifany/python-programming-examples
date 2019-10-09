import cherrypy
import json
from _movie_database import _movie_database

class MovieController(object):
	def __init__(self, mdb):
		mdb = _movie_database()
		mdb.load_movies('data/movies.dat')
		mdb.load_users('data/users.dat')
		mdb.load_ratings('data/ratings.dat')
		mdb.load_images()

	def GET(self):
		output = {'result':'success'}
		entries = []

		for key in mdb.movies:
			try:
				entries.append({'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'result':'success', 'img':mdb.images[key]})
			except KeyError as ex:
				entries.append({'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'result':'success'})
		try:
			output['movies'] = entries
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self):#adding a new movie
		output = {'result':'success'}
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['title'])
		data.append(the_body['genres'])
		mid = max(mdb.movies.keys()) + 1 #generate new movie id
		output['id'] = mid
		try:
			mdb.movies[mid] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {"result":"success"}

		mdb.movies = {}

		return json.dumps(output)

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			if key in mdb.images:
				output = {'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1], 'img':mdb.images[key]}
			else:
				output = {'id':key, 'title':mdb.movies[key][0], 'genres':mdb.movies[key][1]}
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		key = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['title'])
		data.append(the_body['genres'])

		try:
			mdb.movies[key] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			del mdb.movies[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
