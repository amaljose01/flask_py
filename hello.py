from flask import Flask

app = Flask(__name__)
###app.run(debug = True)
@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'

app.run()
