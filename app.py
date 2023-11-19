from urbandict import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_dict = con.execute('SELECT * FROM dicts').fetchall()
    con.close()
    
    dicts = []
    for row in db_dict:
        dicts.append({'word':row[0],'description':row[1],'user_id':row[2]})
    
    return render_template(
        'index.html',
        dicts = dicts
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])
def register():
    word = request.form['word'].strip()  # Remove leading and trailing whitespaces
    description = request.form['description']
    user_id = request.form['user_id']
    
    if not word or not description:
        return redirect(url_for('form'))
    
    else:
        con = sqlite3.connect(DATABASE)
        con.execute('INSERT INTO dicts VALUES (?, ?, ?)', [word, description, user_id])
        con.commit()
        con.close()
        
        return redirect(url_for('index'))

@app.route('/delete/<word>', methods=['GET', 'POST'])
def delete(word):
    if request.method == 'GET':
        return render_template('delete_confirmation.html', word=word)
    elif request.method == 'POST':
        con = sqlite3.connect(DATABASE)
        con.execute('DELETE FROM dicts WHERE word = ?', [word])
        con.commit()
        con.close()
        return redirect(url_for('index'))