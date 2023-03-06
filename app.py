from flask import Flask 
AI=Flask(__name__)

@AI.route('/wish')
def  wish():
    return '<h1>this is venkat</h1>'

@AI.route('/second')
def second():
    return '<h1>this is second flask file </h1>'

@AI.route('/third')
def third():
    return '<h4> this is third flask file</h4>'

if __name__=='__main__':
    AI.run(debug=True)