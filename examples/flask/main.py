# Simple Website with Htmotor + Flask

from flask import Flask
from htmotor import HTML

app = Flask(__name__)
motor = HTML(prevent_xss=True)

@app.route('/')
def index():
    return motor.render_file("./test.htmo", title="Simple App", name="DateTime")

if __name__ == '__main__':
    app.run()
