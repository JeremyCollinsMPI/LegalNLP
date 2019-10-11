from flask import Flask
from flask_restful import Resource, Api
from load_data_pipeline import load
from search import search_by_id

app = Flask(__name__)
api = Api(app)

directory_name = 'Files'

class Load(Resource):
  def get(self):
    load(directory_name)
    return 'Success'

class Search(Resource):
   def get(self, search_id):
     search_id = search_id.capitalize()
     return str(search_by_id(search_id))

api.add_resource(Load, '/load')
api.add_resource(Search, '/search/<string:search_id>')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')