Flask login and logout:
Requirements : flask and mysql-connector-python

Need to understand the Flask flow from code01.py file to template files( home.html ,login.html ) and connectivity between rout,function.

Flowchart in python file : 
# code01.py

1) Instance creation for Flask and Mysql

a1= Flask(__name__)    # App is an instance for Flask declaration 

mysql=MYSQL()           # mysql is a instance for MYSQL 

2) Configuration of Database with Flask:

a1.config['MYSQL_HOST'] = 'localhost'

a1.config['MYSQL_USER'] = 'user'

a1.config['MYSQL_PASSWORD'] = 'password'

a1.config['MYSQL_DB'] = 'mydb1_new'

mysql.init_app(a1)        #initiating the db 

3) Route will enable us to associate function with particular url.

@a1.route('/')

def main():                               #---------------> first function and it will redirect to

  return render_template('login.html')       login page mentioned in render template( login.html )

# login.html

        <body>
            <form action="/logged_in" method="POST">  # here logged_in redirect to second function [ login() ] that starts to run once username & password submitted.
                <p>Login</p>
                <input type="text" name="username">
                <input type="text" name="password">
                <input type="submit">
            </form>
        </body>

# again to code01.py 
@a1.route('/logged_in',methods=['GET','POST'])

def login():

    if request.method=="POST":                      # if the requested method is 'POST'
    
        username=request.form['username']           # entered username data in login page will routed to this login function to this username
        
        password=request.form['password']           # entered user password data in login page will routed to this login function to this password
        
        s2=mysql.connect                            # this helps to connect with our db 
        
        curse=s2.cursor()                           
        
        curse.execute("select * from table02 where username=%s AND password=%s",(username,password))      # Username and password will forward it to this execute line and get assigned
        
        data=curse.fetchone()                       # this helps to fetch data from db
        
        if data is None:                            # if data not available, which means entered username & password in login page not available in DB 
        
            return"Username or password is incorrect"           # it returns the this message
            
        else:
        
            return render_template('home.html')     #if data is available, which means entered username & password in login page available in DB wil redirect to mentioned template to home.html
            

# Home.html 

<body>
  <h1>Dashboard</h1>
  <p>Loggedin to Dashboard</p>
  <div>
    <a href="{{url_for('logout')}}">logout</a>    # this url_for will rediret to logout function.
  </div>
</body>
