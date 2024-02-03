from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

class TestData(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    trestbps = db.Column(db.Integer, nullable=False)
    chol = db.Column(db.Integer, nullable=False)
    fbs = db.Column(db.Integer, nullable=False)
    restecg = db.Column(db.Integer, nullable=False)
    thalach = db.Column(db.Integer, nullable=False)
    exang = db.Column(db.Integer, nullable=False)
    oldpeak = db.Column(db.Integer, nullable=False)
    slope = db.Column(db.Integer, nullable=False)
    ca = db.Column(db.Integer, nullable=False)
    thal = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('apply.html')

@app.route('/records', methods=['GET', 'POST'])
def records():
    if request.method=='POST':
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        data = TestData(
            name=name, 
            age=age, 
            sex=sex, 
            cp=cp, 
            trestbps=trestbps, 
            chol=chol, 
            fbs=fbs, 
            restecg=restecg, 
            thalach=thalach, 
            exang=exang, 
            oldpeak=oldpeak, 
            slope=slope, 
            ca=ca, 
            thal=thal
            )
        db.session.add(data)
        db.session.commit()
    allData = TestData.query.all()
    return render_template('records.html', allData=allData)

if __name__=="__main__":
    app.run(debug=True, port=8000)