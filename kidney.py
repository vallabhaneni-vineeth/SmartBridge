from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
rfc=pickle.load(open('kidney.pkl','rb'))

@app.route('/')
def home():
    return render_template("kidney_demo.html")
@app.route('/ckd')
def ckd():
    return render_template("kidney.html")

@app.route('/predict',methods=['post'])
def predict():
    Id=int(request.form['id'])
    Age=int(request.form['age'])
    Bp=int(request.form['bp'])
    Sg=int(request.form['sg'])
    Al=int(request.form['al'])
    Su=int(request.form['su'])
    Rbc=int(request.form['rbc'])
    Pc=int(request.form['pc'])
    Pcc=int(request.form['pcc'])
    Ba=int(request.form['ba'])
    Bgr=int(request.form['bgr'])
    Bu=int(request.form['bu'])
    Sc=int(request.form['sc'])
    Sod=int(request.form['sod'])
    Pot=int(request.form['pot'])
    Hemo=int(request.form['hemo'])
    Htn=int(request.form['htn'])
    Dm=int(request.form['dm'])
    Cad=int(request.form['cad'])
    Appet=int(request.form['appet'])
    Pe=int(request.form['pe'])
    Ane=int(request.form['ane'])
    
    
    a=np.array([[Id,Age,Bp,Sg,Al,Su,Rbc,Pc,Pcc,Ba,Bgr,Bu,Sc,Sod,Pot,Hemo,Htn,Dm,Cad,Appet,Pe,Ane]])
    print(a)
    
    pred=rfc.predict(a)
    if(pred == 0):
        output="Chronic Kidney Disease"
        print("Chronic Kidney Disease")
    else:
        output="Not Chronic Kidney Disease"
        print("Not Chronic Kidney Disease")


    return render_template('kidney.html', prediction_text= output)

if __name__ == '__main__':
    app.run()