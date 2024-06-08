from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)


#it will display the json along with name if we enter the url for example:
#http://127.0.0.1:5000//greet/praneetha
#output:{"message":"Hello, praneetha!"}