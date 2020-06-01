from flask import Flask,request,render_template
import numpy as np
import ast
import pickle
app = Flask(__name__)

# initial route
@app.route('/')
def home():
    return render_template('0.html')


@app.route('/result', methods=['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        data = request.form
        Radius = float(data['Radius Mean'])
        Texture = float(data['Texture Mean'])
        Perimeter = float(data['Perimeter Mean'])
        Area = float(data['Area Mean'])
        Smoothness = float(data['Smoothness Mean'])
        Compactness = float(data['Compactness Mean'])
        Concavity = float(data['Concavity Mean'])
        Concave = float(data['Concave Points Mean'])
        Symmetri = float(data['Symmetry Mean'])

        data_new = [Radius,Texture,Perimeter,Area,Smoothness,Compactness,Concavity,Concave,Symmetri]

        data_new = np.array(data_new)

        data1 = scaler.transform([data_new])

        # print(data1)
        # print(data_new)
        # return 'ok'


        x = model.predict(data1)[0]

        # print(data_new)
        return  render_template('1.html',x=x)
        # 'Prediksi = ' + str(x)


if __name__ == '__main__':
    model = pickle.load(open("MachineModel", 'rb'))
    scaler = pickle.load(open("scal", 'rb'))
    app.run(debug=True, port=1234)
