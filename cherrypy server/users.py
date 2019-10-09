import cherrypy
import json

class UserController:
	def __init__(self, mdb):
		self.mdb = mdb
	def GET(self):
		output = {'result':'success'}
		entries = []

		for key in mdb.users:
			entries.append({'id':key, 'gender':mdb.users[key][0], 'age':mdb.users[key][1], 'occupation':mdb.users[key][2], 'zipcode':mdb.users[key][3]})

		try:
			output['users'] = entries
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self): #add a new user
		output = {'result':'success'}
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['gender'])
		data.append(the_body['age'])
		data.append(the_body['occupation'])
		data.append(the_body['zipcode'])
		uid = max(mdb.users.keys()) + 1 #generate new user id
		output['id'] = uid
		try:
			mdb.users[uid] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {'result':'success'}

		mdb.users = {}

		return json.dumps(output)

	def GET(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			output = {'id':key, 'gender':mdb.users[key][0], 'age':mdb.users[key][1], 'occupation':mdb.users[key][2], 'zipcode':mdb.users[key][3]}
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT(self,key):
		output = {'result':'success'}
		key = int(key)
		the_body = json.loads(cherrypy.request.body.read())
		data = []
		data.append(the_body['gender'])
		data.append(the_body['age'])
		data.append(the_body['occupation'])
		data.append(the_body['zipcode'])

		try:
			mdb.users[key] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self,key):
		output = {'result':'success'}
		key = int(key)

		try:
			del mdb.users[key]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
