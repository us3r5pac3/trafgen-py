from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello():
    return {'ok': 'fine'}
@app.route("/large")
def large():
    return {'ok': '1234' * 20000}
@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    # return f"Received form data: Name - {name}, Email - {email}"
    return f""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    pass