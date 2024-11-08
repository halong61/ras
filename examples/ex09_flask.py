from flask import Flask
import led18
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
#/led on, led off 라우팅 하기
#/led on -> def ledon(), "LED ON"
#/led off -> def ledoff(), "ledoff"
#led 18모듈을 불러와서 led/on ->led 켜지게
#/led/df -> led off ->led 꺼지게 
@app.route('/led/on')
def ledon():
    led18.ledon()
    return "LED ON";
@app.route('/led/off')
def ledoff():
    led18.ledoff()
    return "LED OFF";

if __name__ == "__main__":

    app.run(host ="localhost", port = 5000, debug= True)

