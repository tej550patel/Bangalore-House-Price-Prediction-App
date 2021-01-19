#Import Libraries
from flask import Flask, request, render_template
import model 
 
app = Flask(__name__)
 
# render htmp page
@app.route('/')
def home():
    return render_template('index.html')
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    input_features = [x for x in request.form.values()]
    location = input_features[0]
    sqft = input_features[1]
    bath = input_features[2]
    bhk = input_features[3]
     
    # predict the price of house by calling model.py
    predicted_price = model.predict_price(location,sqft,bath,bhk)       
 
 
    # render the html page and show the output
    return render_template('index.html', prediction_text='Predicted Price of Bangalore House is {}'.format(predicted_price))
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")


     
#if __name__ == "__main__":
#    app.run(debug=True)
    
    
     
