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
    Age=int(request.form['age'])
    Bp=int(request.form['bp'])
    Al=int(request.form['al'])
    Rbc=int(request.form['rbc'])
    Pc=int(request.form['pc'])
    Pcc=int(request.form['pcc'])
    Sc=int(request.form['sc'])
    Hemo=int(request.form['hemo'])
    wc=int(request.form['wc'])
    pcv=int(request.form['pcv'])
    rc=int(request.form['rc'])
    Appet=int(request.form['appet'])
    Ane=int(request.form['ane'])
    
    
    a=np.array([[Age,Bp,Al,Rbc,Pc,Pcc,Sc,Hemo,wc,pcv,rc,Appet,Ane]])
    print(a)
    
    pred=rfc.predict(a)
    if(pred == 0):
        output="Chronic Kidney Disease"
        print("Chronic Kidney Disease")
    else:
        output="Not Chronic Kidney Disease"
        print("Not Chronic Kidney Disease")
    prediction_text=output

    return render_template('kidney.html', prediction_text= 'The Candidate has {}'.format(prediction_text))

if __name__ == '__main__':
    app.run()