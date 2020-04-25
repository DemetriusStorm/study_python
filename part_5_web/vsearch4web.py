"""
Introduce with flask!
"""

from flask import Flask, render_template
from _public.study_python.part_4_function.mymodules.vsearch import search_letters_in_phrase as search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    return str(search4letters('Life, the universe, and everything!', 'eiru,!'))


@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)
