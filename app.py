from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

@app.route('/home', methods = ['GET', 'POST'], defaults={'name':'Default'})
@app.route('/home/<string:name>', methods = ['GET', 'POST'])
def home(name):
    return '<h1>Hello {}, you are on the home page.</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key':'value', 'list':[1,2,3]})

@app.route('/query') 
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}, you are from {}. You are on the query page. </h1>'.format(name, location)

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET' :
        return '''<form method="POST" action="/form">
                    <input type="text" name="name"><br>
                    <input type="text" name="location"><br>
                    <input type="submit">
                </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return '<h1>Hi {}, you are from {}.</h1>'.format(name, location)

# @app.route('/process', methods = ['POST'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
#     return '<h1>Hi {}, you are from {}.</h1>'.format(name, location)

@app.route('/processJson', methods = ['POST'])
def processJson():
    data = request.get_json() 
    
    name = data['name']
    location = data['location']
    randomList = data['randomList']
    
    return jsonify({'result': 'Success', 'name': name, 'location':location, 'list':randomList})

if __name__ == '__main__':
    app.run(debug=True)