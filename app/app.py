from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = '127.0.0.1'  # or your host
app.config['MYSQL_USER'] = 'root'  # or your username
app.config['MYSQL_PASSWORD'] = 'abc123'  # or your password
app.config['MYSQL_DB'] = 'notes'  # or your database name

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        cur = mysql.connection.cursor()
    except Exception as e:
        return render_template('error.html', error=str(e))

    if request.method == 'POST':
        try:
            note_details = request.form
            note = note_details['note']
            cur.execute("INSERT INTO notes(note) VALUES (%s)", [note])
            mysql.connection.commit()
            cur.close()
        except Exception as e:
            return render_template('error.html', error=str(e))
        return redirect(url_for('index'))  # redirect back to the home page
    else:
        try:
            cur.execute("SELECT * FROM notes")
            notes = cur.fetchall()
            return render_template('index.html', notes=notes)
        except Exception as e:
            return render_template('error.html', error=str(e))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)