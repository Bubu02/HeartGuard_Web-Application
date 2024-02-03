from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('apply.html')

@app.route('/records')
def records():
    return render_template('records.html')

if __name__=="__main__":
    app.run(debug=True, port=8000)