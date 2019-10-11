from flask import Flask
from flask_restful import Resource, Api
from load_data_pipeline import load
from search import search_by_id

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
     search_id = search_id.capitalize()
     return str(search_by_id(search_id))

class ReusableForm(Form):
    name = TextField('Search term:', validators=[validators.required()])
    
    @app.route("/search", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            search_id = name.capitalize()
            return str(search_by_id(search_id))
        return render_template('form.html', form=form)



api.add_resource(Load, '/load')
api.add_resource(Search, '/search/<string:search_id>')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')