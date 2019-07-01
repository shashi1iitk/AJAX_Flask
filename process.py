from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.form['email']
	name = request.form['name']
	blood_group = request.form['blood_group']
	country = request.form['country']
	selected_sports = request.form['selected_sports']
	# multiselect = request.form['multiselect']

	if name and email:
		newName = name[::-1]

		newEmail = 'Hellos'
		return jsonify({'name' : country+email+name+newName+blood_group+selected_sports})

	return jsonify({'error' : 'Missing data!'})

app.run(debug = True)