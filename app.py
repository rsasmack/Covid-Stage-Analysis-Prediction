import numpy as np

from flask import Flask,render_template,request,redirect
import os
import pickle

app=Flask(__name__) #constructor
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/") #root path
def show():
    return render_template('home.html')


@app.route("/index.html",methods=["POST","GET"])
def home():
        if request.method=="POST":
            a=int(request.form['fever'])
            b=int(request.form["cough"])
            c=int(request.form["fatigue"])
            d=int(request.form["loss_smell_taste"])
            e=int(request.form["nassal_congestion"])
            f=int(request.form["red_eyes"])
            g=int(request.form["sore_throat"])
            h=int(request.form["headache"])
            i=int(request.form["muscle_pain"])
            j=int(request.form["skin_rash"])
            k=int(request.form["vomiting"])
            l=int(request.form["diarrhea"])
            m=int(request.form["breathing_issue"])
            n=int(request.form["loss_apetite"])
            o=int(request.form["chest_pain"])
            p=int(request.form["age"])
            yy = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]])
            if yy[0]==0:
                output="No worries you are covid negative"
                return render_template('result.html',prediction_text='{}'.format(output))
            elif yy[0]==1:
                output="You can go for checkup"
                return render_template('result.html',prediction_text='{}'.format(output))
            elif yy[0]==2:
                output="It's serious you should go for checkup"
                return render_template('result.html',prediction_text='{}'.format(output))
            elif yy[0]==3:
                output="It is very serious you should immediately go for checkup"
                return render_template('result.html',prediction_text='{}'.format(output))
             
            
        return render_template('index.html')
            
@app.route("/post")
def post():
    return "successfull"

if __name__=='__main__': #main function 
    app.run()
