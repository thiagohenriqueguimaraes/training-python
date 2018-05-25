from bottle import Bottle, run, template, route

app = Bottle()
@app.route('/')

@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

# matches /wiki/Learning_Python
@app.route('/wiki/<pagename>')
def show_wiki_page(pagename):
    return template('ok {{x}}',x=pagename)

# matches/follow/defnull
@route('/<action>/<user>')
def user_api(action, user_api): 
    return template('ok')

run(app, host="localhost", port=8080, debug=True)