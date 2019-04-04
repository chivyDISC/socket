from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from models import*
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socket = SocketIO(app)
db.init_app(app)

@socketio.on('message')
def handle_message(msg):
    message = Message(message = msg)
    db.session.add(message)
    db.session.commit()
    send(msg, broadcast=True)

@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))

@app.route("/")
def index():
    messages = Message.query.all()
    return render_template("index.html", messages = messages)


