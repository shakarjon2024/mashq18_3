from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    num = int(request.args.get('num'))
    res = "Juft" if num % 2 == 0 else "Toq"
    return render_template('result.html', result=res)

app.run(debug=True)
