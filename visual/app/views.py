from app import app
from flask import render_template
import os


@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"


@app.route('/puzzle', methods=['GET', 'POST'])
def visual():
	with open(os.path.join('app', 'db.txt')) as f:
		data = [line.strip() for line in f.read().splitlines() if not line.startswith('#')]
		size = data.pop(0)
		elements = [int(element) for sub in data for element in sub.split()]

	return render_template(
		'puzzle.html', title='NPUZZLE', size=int(size),
		elements=elements, move=[]
	)
