from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'

@app.route('/test')
def query():
    query_param=request.args
    return query_param

def main():
    app.debug = True
    app.run(host='192.168.1.252', port=5000)

if __name__ == '__main__':
    main()


