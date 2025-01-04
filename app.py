from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'key1234'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="auth_todo", 
    port=3307
)

cursor = db.cursor()


def get_todos(user_id):
    cursor.execute("SELECT * FROM todos WHERE user_id = %s", (user_id,))
    todos = cursor.fetchall()
    return todos

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        db.commit()

        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')  


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        todos = get_todos(session['user_id'])
        return render_template('dashboard.html', todos=todos)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/add-todo', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    user_id = session.get('user_id')

    cursor.execute("INSERT INTO todos (title, description, user_id) VALUES (%s, %s, %s)", (title, description, user_id))
    db.commit()

    return redirect(url_for('dashboard'))


@app.route('/delete-todo/<int:todo_id>')
def delete_todo(todo_id):
    cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    db.commit()
    return redirect(url_for('dashboard'))

@app.route('/updater/<int:todo_id>',)
def updater(todo_id):
    cursor.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    todo = cursor.fetchone()
    return render_template('updater.html', todo=todo)


@app.route('/update-todo/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    title = request.form['title']
    description = request.form['description']

    cursor.execute("UPDATE todos SET title = %s, description = %s WHERE id = %s", (title, description, todo_id))
    db.commit()

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)