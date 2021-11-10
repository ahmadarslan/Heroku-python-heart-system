
from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods=['POST'])
def predict():
   
   
   inputs = []
   inputs.append(request.form['age'])
   inputs.append(request.form['gender'])    
   inputs.append(request.form['bp'])
   inputs.append(request.form['chol'])
   
   age1 = request.form['age']
   gender1 = request.form['gender'] 
   bp1 = request.form['bp']
   chol1 = request.form['chol']
   

   
   
   final_inputs = [np.array(inputs)]
   prediction = svc_model.predict(final_inputs)
    #unseen_feature_vectors = request.form.values()
   
   if prediction[0] == 1:
        categorical_array = "Diagnosed"
   if prediction[0] == 0:
        categorical_array = "Not Diagnosed"
    
   result= categorical_array
   
       
   if gender1=="1":
       gender1 = "Female"
   if gender1=="0":
       gender1 = "Male"
     
   
       
   
       
   return render_template('Home.html', prediction_text1=result, age2 = age1, gender2=gender1, bp2=bp1, chol2=chol1)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)