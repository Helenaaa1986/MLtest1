from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    temperature = float(request.form.get('temperature'))
    prediction = model.predict(np.array([[temperature]]))
    output = round(prediction[0], 2)
    prediction_text = f'Total revenue generated is Rs.{output}/-'
    return render_template('index1.html', prediction_text=prediction_text)

if __name__ =='__main__':
    app.run(debug=True)



