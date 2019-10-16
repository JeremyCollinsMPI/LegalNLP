from flask import Flask
from flask_restful import Resource, Api
from load_data_pipeline import load
from search import search_by_id
from unique_ids import *
import os

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
api = Api(app)

directory_name = 'Files'

class Load(Resource):
  def get(self):
    load(directory_name)
    return 'Success'

class Search(Resource):
   def get(self, search_id):
     return str(search_by_id(search_id))

class ReusableForm(Form):
    name = TextField('Search term:', validators=[validators.required()])
    
    @app.route("/search", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            search_id=request.form['name']
            return str(search_by_id(search_id))
        return render_template('form.html', form=form)

class UniqueIds(Resource):
  def get(self):
    result = find_unique_ids()
    result = [x.decode('utf-8') for x in result]
    return result

api.add_resource(Load, '/load')
api.add_resource(Search, '/search/<string:search_id>')
api.add_resource(UniqueIds, '/ids')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')