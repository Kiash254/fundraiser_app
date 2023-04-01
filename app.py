"""
my first flask app using flask funny framework
"""
from flask import Flask

app_name=Flask(__name__)

@app_name.route('/')
def index():
    return 'Hello World'

@app_name.route('/app/')
def user(name):
    name='Devops developers'
    return f'Hello {name}'


if __name__ == '__main__':
    app_name.run(debug=True)