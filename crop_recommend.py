# Impor libraries and modules

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle



app = Flask(__name__)

# Loading crop recommendation model

model = pickle.load(open('crop.pkl', 'rb'))



# render home page

@ app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    
    eval_features = [eval(x) for x in request.form.values()]
    final_features = [np.array(eval_features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    
    if output == 0:
        return render_template('index.html', prediction='Crop to grow apple')
    
    elif output == 1:
        return render_template('index.html', prediction='Crop to grow banana')
    
    elif output == 2:
        return render_template('index.html', prediction='Crop to grow blackgram')
    
    elif output == 3:
        return render_template('index.html', prediction='Crop to grow chickpea')
    
    elif output == 4:
        return render_template('index.html', prediction='Crop to grow coconut')
    
    elif output == 5:
        return render_template('index.html', prediction='Crop to grow coffee')
    
    elif output == 6:
        return render_template('index.html', prediction='Crop to grow cotton')
   
    elif output == 7:
        return render_template('index.html', prediction='Crop to grow grapes')
    
    elif output == 8:
        return render_template('index.html', prediction='Crop to grow jute')
    
    elif output == 9:
        return render_template('index.html', prediction='Crop to grow kidneybeans')
    
    elif output == 10:
        return render_template('index.html', prediction='Crop to grow lentil')
    
    elif output == 11:
        return render_template('index.html', prediction='Crop to grow maize')
    
    elif output == 12:
        return render_template('index.html', prediction='Crop to grow mango')
    
    elif output == 13:
        return render_template('index.html', prediction='Crop to grow mothbeans')
    
    elif output == 14:
        return render_template('index.html', prediction='Crop to grow mungbean')
    
    elif output == 15:
        return render_template('index.html', prediction='Crop to grow muskmelon')
    
    elif output == 16:
        return render_template('index.html', prediction='Crop to grow orange')
    
    elif output == 17:
        return render_template('index.html', prediction='Crop to grow papaya')
    
    elif output == 18:
        return render_template('index.html', prediction='Crop to grow pigeonpeas')
    
    elif output == 19:
        return render_template('index.html', prediction='Crop to grow pomegranate')
    
    elif output == 20:
        return render_template('index.html', prediction='Crop to grow rice')
    
    else:
        return render_template('index.html', prediction='Crop to grow watermelon')



if __name__ == '__main__':
    app.run(debug=False)