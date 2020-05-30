from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


developers = [
  {
    'id': '0',
    'name': 'João Victor',
    'skills': ['Python', 'Flask', 'Javascript', 'Node', 'React JS', 'React Native']
  },
  # Other Developers Below...
]

def log(type, message):
  if type == 'Error':
    message =  {'Status': 'Error', 'Message': message}
  elif type == 'Success':
    message = {'Status': 'Sucess', 'Message': message}
  return message

class Developer(Resource):
  def get(self, id):
    try:
      response = developers[id]
    except IndexError:
      message = 'Developer ID {} not exists!'.format(id)
      response = log('Error', message)
    except Exception:
      message = 'Unknown Error. Contact the Administrator of API'
      response = log('Error', message)
    
    return response
  def put(self, id):
    data = json.loads(request.data)
    developers[id] = data
    return data
  def delete(self, id):
    developers.pop(id)
    message = 'Record ID {} deleted'.format(id)
    return log('Success', message)

api.add_resource(Developer, '/dev/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)