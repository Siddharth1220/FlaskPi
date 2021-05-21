from flask import Flask, render_template
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT, initial=GPIO.LOW)
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('on.html')

@app.route('/on')
def on():
    print ('ON')
    GPIO.output(14,GPIO.HIGH)
    return render_template('off.html')


@app.route('/off')
def off():
    print ('OFF')
    GPIO.output(14,GPIO.HIGH)
    return render_template('on.html')
    


app.run(debug=True,host='0.0.0.0')
