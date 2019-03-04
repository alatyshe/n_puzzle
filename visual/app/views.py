from app import app
from flask import render_template
import os
import json


@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"


@app.route('/puzzle', methods=['GET', 'POST'])
def visual():
	coding = {'LEFT': 39, 'RIGHT': 37, 'UP': 40, 'DOWN': 38}

	with open(os.path.join('app', 'db.txt')) as f:
		data = json.load(f)
		size = data.get('size')
		elements = data.get('state')
		move = data.get('commands')

	return render_template(
		'puzzle.html', title='NPUZZLE', size=int(size),
		elements=elements, move=[coding.get(command.upper()) for command in move]
	)
