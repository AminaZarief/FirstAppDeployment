from flask import Flask,render_template,request
import pickle


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():

    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        X1=float(request.form['F1'])
        X2=float(request.form['F2'])
        X3=float(request.form['F3'])
        X4=float(request.form['F4'])

        loaded_model = pickle.load(open('model.pkl', 'rb'))
        prediction=loaded_model.predict([[X1,X2,X3,X4]])[0]
        
        return render_template('index.html',prediction=prediction)
  
    
@app.route("/add",methods=['GET','POST'])
def add():

  
    if request.method=='GET':
        return render_template('add.html')
    if request.method=='POST':
        
        X=request.form['F1']
        Y=request.form['F2']

        result= int(X)+int(Y)
        
        return render_template('add.html',result=result)
   
@app.route("/sub",methods=['GET','POST'])
def sub():
    if request.method=='GET':
        return render_template('sub.html')
    if request.method=="POST":
        X=request.form['F1']
        Y=request.form['F2']
        result=int(X)-int(Y)
        return render_template('sub.html',result=result)
    

@app.route("/mul/<int:F1>/<int:F2>")
def mul(F1,F2):
    return str(F1*F2)

if __name__=="__main__":
    app.run(debug=True)
