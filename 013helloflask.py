from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return 'open the url in another tab, and then go to/hello/yourname'

@app.route('/hello/<name>')
def hello_name(name):
    return 'hello ' + name + '!'

if __name__ == '__main__':
  app.run()