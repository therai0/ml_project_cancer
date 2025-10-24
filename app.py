
from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline,CustomData


application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predictdata",methods=['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        data = CustomData(
        Sex=request.form.get('sex'),
        ChestPainType=request.form.get('ChestPainType'),
        RestingECG=request.form.get('RestingECG'),
        ExerciseAngina=request.form.get('ExerciseAngina'),
        ST_Slope=request.form.get('ST_Slope'),
        Age=int(request.form.get('Age')),
        Cholesterol=int(request.form.get('Cholesterol')),
        FastingBS=int(request.form.get('FastingBS')),
        MaxHR=int(request.form.get('MaxHR')),
        Oldpeak=float(request.form.get('Oldpeak')),
        RestingBP=int(request.form.get('RestingBP')),
        )
        data_frame = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(data_frame)
        return render_template('predict.html',result=result) 

if __name__ == "__main__":
    app.run(debug=True,port='8000')
