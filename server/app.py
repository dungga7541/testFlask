import pyrebase

config={
    "apiKey": "AIzaSyBAbHaGULEqWOUnD4erNktFehP8Hdn3vxo",
    "authDomain": "testfire271120.firebaseapp.com",
    "databaseURL": "https://testfire271120.firebaseio.com",
    "projectId": "testfire271120",
    "storageBucket": "testfire271120.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form.get('submit') == 'add':

			name = request.form.get('name')
			db.child("name").push(name)
			todo = db.child("name").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form.get('submit') == 'delete':
			db.child("name").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)