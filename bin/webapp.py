#bottle and flask are micro framework
#Django and web2py also most used frameworks
#import bottle
import flask
#app=bottle.Bottle()
app=flask.Flask('Myapp')
#@app.error(404)
@app.errorhandler(404)
def errorpage(e): #taking Care of error page
    return 'Page in progress'
@app.route('/')
def homepage():
    return 'Welcome'
@app.route('/<name>') #redirecting pages or menus
def aboutpage(name):
    return '<b>About</b>'
#@app.route('/emp/<id:int>')
@app.route('/emp/<int:id>')
def empid(id):
    return 'Your ID :'+str(id)
#@app.route('/path/<p:path>')#full path
@app.route('/path/<path:p>')#full path
def fullpath(p):
    return 'This is your Path:'+str(p)
#@app.route('/reg/<l:re:[a-z0-9]+>') #reguler expression
#reuler expression not supported in flask
#def regex(l):
   # return 'Here what you just did: ' +str(l)

@app.route('/login')
def logipage():
    return '''<form action='/verifylogin' method='post'>
              User Name:<input type='test' name='uname' /> <br>
              Password:<input type='password' name='pw'/> <br>
                       <input type='submit' value='Login'/>
              </from>'''
#@app.post('/verifylogin')
@app.route('/verifylogin', methods=['get','post'])
def vlogin():
    #u=bottle.request.forms.get('uname')
    u=flask.redirect('uname')
    #p=bottle.request.forms.get('pw')
    p=flask.redirect('pw')
    if not (u=='abc' and p=='xyz'):
        return 'Login Failed'
    else:
        return 'Login Successful'

#in bottle framework > .tpl (Template engine files to write the python code inside HTML files) #%for #%end #{{variable}}
#in Flask framework > .html #{%for%} #{%endfor%} #{{var}}
#app.run(port=45676)#host='172.20.227.116'
