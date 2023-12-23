from flask import Flask,render_template,json,request
import urllib
import socketserver
import json

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    data=None
    if request.method=="POST":
        city=request.form.get('city')
        print(city)
        if socketserver.BaseServer:
            source=urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=48a90ac42caa09f90dcaeee4096b9e53").read()
            print(source)
            
            # converting json data to dictionary
            list_of_data = json.loads(source)

            data={
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "city":city,
            }

    return render_template("index.html",data=data)


if __name__=="__main__":
    app.run(debug=True)