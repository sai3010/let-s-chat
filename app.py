from flask import Flask, render_template,request,session
from flask_socketio import SocketIO,join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index',methods=["POST"])
def index():
    session['uname']=request.values.get("user")
    session['room']=request.values.get("room")
    return render_template('index.html',name=request.values.get("user"),room=request.values.get("room"))

@socketio.on('joined')
def on_join(data):
    uname=session.get('uname')
    room = session.get('room')
    join_room(room)
    socketio.emit('status', {'msg': session.get('uname') + ' has entered the room.'}, room=room)


@socketio.on('msg')
def handle_uname(json,methods=['GET', 'POST']):
    print('my_response: ' + str(json))
    uname=session.get('uname')
    room = session.get('room')
    data={'name':uname,'msg':json}
    socketio.emit("response",data,broadcast=True,room=room)

if __name__ == '__main__':
    socketio.run(app)