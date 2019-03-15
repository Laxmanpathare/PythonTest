#bottle and flask are micro framework
#Django and web2py also most used frameworks
import bottle

app=bottle.Bottle()

@app.error(404)

def errorpage(e): #taking Care of error page
    return 'Page in progress'
@app.route('/')
def homepage():
    return 'Welcome'
@app.route('/<name>') #redirecting pages or menus
def aboutpage(name):
    return '<b>About</b>'
@app.route('/emp/<id:int>')

def empid(id):
    return 'Your ID :'+str(id)
@app.route('/path/<p:path>')#full path

def fullpath(p):
    return 'This is your Path:'+str(p)
@app.route('/reg/<l:re:[a-z0-9]+>') #reguler expression
#reuler expression not supported in flask
def regex(l):
    return 'Here what you just did: ' +str(l)

@app.route('/login')
def loginpage():
    return '''<form action='/verifylogin' method='post'>
              User Name:<input type='test' name='uname' /> <br>
              Password:<input type='password' name='pw'/> <br>
                       <input type='submit' value='Login'/>
              </form>'''
@app.post('/verifylogin')
def vlogin():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not (u=='abc' and p=='xyz'):
        return 'Login Failed'
    else:
        # #return 'Login Successful'
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        print(bottle.TEMPLATE_PATH)
        bottle.TEMPLATE_PATH.append(r'C:\Users\Admin\Desktop\Laxman\bin')
        return bottle.template('report.tpl',res=result)
        # #return str(result)

@app.route('/ml')
def ml():
    #bottle.TEMPLATE_PATH.append(r'C:\Users\Admin\Desktop\Laxman\bin')
    return bottle.template('mach_display.tpl',)
@app.post('/submitdata')
def readdata():
    P1=bottle.request.forms.get('p1')
    P2=bottle.request.forms.get('p2')
    P3=bottle.request.forms.get('p3')
    P4=bottle.request.forms.get('p4')
    import machlearn
    res=machlearn.getresult(P1,P2,P3,P4)
    if res==0:
        return 'Type is : Setosa'
    elif res==1:
        return 'Type is : Versicolor'
    elif res==2:
        return 'Type is : Virginica'
    else:
        return 'Type is : Not Defined'

@app.route('/json')
def jsondata():
    import json
    D={'A':10,'B':20}
    F=open('mydata.json','w')
    json.dump(D,F)
    F.close()
    F=open('mydata.json')
    r=json.load(F)
    F.close()
    return r
@app.route('/download/<fname>')
def staticfile(fname):
    return bottle.static_file(fname, root=r'C:\Users\Admin\Desktop\Laxman\bin')


#in Flask framework > .html #{%for%} #{%endfor%} #{{var}}
app.run(port=12345)#host='172.20.227.116'
