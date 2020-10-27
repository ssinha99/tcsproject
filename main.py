from flask import Flask,render_template, request,redirect
import pickle

app = Flask(__name__)
filename = 'finalized_model.sav'
model=pickle.load(open(filename, 'rb'))


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def hello1():
    if request.method == 'POST':
        inp2= str(request.form['inp2'])
        inp3= str(request.form['inp3'])
        inp4= str(request.form['inp4'])
        hum= str(request.form['inp5'])
        wspdm= str(request.form['inp6'])
        arr=['Haze','Smoke','Mist','Clear','Widespread Dust','Fog','Scattered Clouds','Partly Cloudy','Shallow Fog'
             ,'Mostly Cloudy','Light Rain','Partial Fog','Patches of Fog','Thunderstorms and Rain',
             'Heavy Fog','Light Drizzle','Rain','Unknown','Blowing Sand','Overcast','Thunderstorm',
             'Light Thunderstorms and Rain','Drizzle','Light Thunderstorm','Light Fog','Heavy Rain',
             'Heavy Thunderstorms and Rain','Thunderstorms with Hail','Squalls','Light Sandstorm',
             'Light Rain Showers','Light Haze','Volcanic Ash','Sandstorm','Funnel Cloud','Rain Showers',
             'Heavy Thunderstorms with Hail','Light Hail Showers','Light Freezing Rain']        
        prediction = model.predict([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19.0, 0, 0,
                                     hum, 1022.0, 0, 0, inp4, 0, 0, 2.0, 110.0, wspdm, inp2, inp3]])
        index=prediction[0]
    return render_template('index.html', output = arr[index])


#if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=8080,debug=True)
if __name__ == '__main__':
    app.run(debug=True)