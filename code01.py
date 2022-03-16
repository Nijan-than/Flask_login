import mysql.connector
from flask import *
from flask_mysqldb import MySQL,MySQLdb

#instance creation of flask and sql
a1=Flask(__name__)
mysql=MySQL()
#configuration of db with flask 
a1.config['MYSQL_HOST'] = 'localhost'
a1.config['MYSQL_USER'] = 'Nijanthan'
a1.config['MYSQL_PASSWORD'] = 'Whateverittakes3297'
a1.config['MYSQL_DB'] = 'mydb1_new'
mysql.init_app(a1)

#functions and route
@a1.route('/')
def first():
    return render_template('login.html')

@a1.route('/logged_in',methods=['GET','POST'])
def login():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        s2=mysql.connect
        curse=s2.cursor()
        curse.execute("select * from table02 where username=%s AND password=%s",(username,password))
        data=curse.fetchone()
        if data is None:
            return"Username or password is incorrect"
        else:
            return render_template('home.html')

@a1.route('/logout')
def logout():
    return redirect(url_for('first'))

if __name__=="__main__":
    a1.run(debug=True)