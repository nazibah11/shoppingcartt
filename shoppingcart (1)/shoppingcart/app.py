import sqlite3
from flask import Flask, render_template,request
app= Flask(__name__)

@app.route('/login' , methods=['GET','POST'])

def index():
   if request.method=='POST':

       connection = sqlite3.connect("user.db")
       cursor = connection.cursor()

       name=request.form("username")
       
       password=request.form("password")

       print(name,password)

       query ='"SELECT * FROM users WHERE (Name,Password)  VALUES(?,?)", username, password'

       cursor.execute(query)

       result = cursor.fetchall()

       if len(result)==0:
            print("somthing went wrong")
       else:
            return render_template("register.html")

   else: 
     return render_template('index.html')

@app.route("/register", methods=["GET", "POST"])
def register():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":

        # Ensure username was submitted
        return render_template("register.html")

    else:
         connection = sqlite3.connect("user.db")
         cursor = connection.cursor()

         username= request.form.get("username")
         password= request.form.get("password")
         reenter = request.form.get("Re-enter")

         if not username:
             return ("Enter Username")
         if not password:
             return ("Enter passwoed")
         if not reenter:
             return("retype password")
         if password  != reenter :
              return("Passwords did not match")

        
    new_user= '"INSERT INTO users (Name,Password) VALUES (?,?)" , username, password'
    cursor.execute(new_user)    
    connection.cursor()
    
    return render_template("login.html")
    
@app.route("/add")
def admin():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT categoryId, name FROM categories")
        categories = cur.fetchall()
    conn.close()
    return render_template('add.html', categories=categories)