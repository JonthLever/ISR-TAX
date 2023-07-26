from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/obtener', methods=['POST'])
def obtener():
    monto = request.form['mont']
    print(monto)
    return render_template('index.html', message="Las credenciales no son correctas")

if __name__ == '__main__':
    app.run(debug=True)