from bottle import route, run, static_file
import tests

@route('/index.js')
def js():
    return static_file('index.js', root='.')

@route('/MOCK_DATA.json')
def js():
    return static_file('MOCK_DATA.json', root='.')

@route('/')
def index():
    return static_file('index.html', root='.')

run(host='localhost', port=8080)