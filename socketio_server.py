import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '': 'index.html',
    '/': 'index.html',
})

@sio.event
def connect(sid, environ):
    """
    The connect event is an ideal place to perform user authentication,
    and any necessary mapping between user entities in the application and the sid that was assigned to the client.
    The environ argument is a dictionary in standard WSGI format containing the request information, including HTTP headers.
    After inspecting the request, the connect event handler can return False to reject the connection with the client.

    """
    print('connect ', sid)



@sio.event
def message(sid, data):
    sio.emit('response', data)
    print('message: ', sid, data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)