from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, ToDo

app = Flask(__name__)

engine = create_engine('sqlite:///todo.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all todos
@app.route('/')
@app.route('/todo/')
def showToDo():
    todos = session.query(ToDo).all()
    return render_template('todo.html', todos=todos)


@app.route('/todo/new/', methods=['GET', 'POST'])
def newtodo():
    if request.method == 'POST':
        todo1 = ToDo(task_desc=request.form['desc'])
        session.add(todo1)
        session.commit()
        return redirect(url_for('showToDo'))
    else:
        return render_template('newtodo.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)