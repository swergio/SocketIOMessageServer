import os
from Server import app, socketio
from flask_socketio import emit
    
@socketio.on('disconnect')
def client_disconnect():
    pass

@socketio.on('connect')
def client_disconnect():
    pass

#namespaces = ['OpenAIGym', 'QATrainer','TinaBob','PythonEvaluation','InternReview']

'''
Set events for provided namespaces
'''
namespaces = os.getenv('NAMESPACES')
def hanlde_mymessage(json):
    emit('mymessage',json,broadcast=True)

for ns in namespaces:
    socketio.on_event('mymessage',hanlde_mymessage, namespace='/' + ns )

'''
Set event handler for communciation with intern review
'''
@socketio.on('mymessage',namespace='/InternReview')
def hanlde_mymessage_Review(json):
    emit('mymessage',json) 

'''
@socketio.on('mymessage',namespace='/OpenAIGym')
def hanlde_mymessage(json):
    emit('mymessage',json,broadcast=True)


@socketio.on('mymessage',namespace='/QATrainer')
def hanlde_mymessage(json):
    emit('mymessage',json,broadcast=True)


@socketio.on('mymessage',namespace='/TinaBob')
def hanlde_mymessage(json):
    emit('mymessage',json,broadcast=True)


@socketio.on('mymessage',namespace='/PythonEvaluation')
def hanlde_mymessage(json):
    emit('mymessage',json,broadcast=True)

@socketio.on('mymessage',namespace='/InternReview')
def hanlde_mymessage_Review(json):
    emit('mymessage',json) 
'''
