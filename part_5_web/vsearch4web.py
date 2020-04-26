"""
Introduce with flask!
"""

from flask import Flask, render_template, request
from _public.study_python.part_4_function.mymodules.vsearch import search_letters_in_phrase as search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase=phrase, letters=letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log') as log:
        print(req, res, file=log)


if __name__ == '__main__':
    app.run(debug=True)
