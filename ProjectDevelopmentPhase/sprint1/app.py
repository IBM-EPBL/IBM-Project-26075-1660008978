from flask import Flask, render_template, request, redirect, url_for, session, flash
import re
import alert 
app = Flask(__name__)
  
app.secret_key = 'a'

print(conn)
print("Connecting Successful!!!!!!!!")

@app.route('/')

def homer():
    return render_template('home.html')
    
if __name__ == '__main__':
   app.run(host='0.0.0.0')
