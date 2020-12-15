"""
To-Do List Application:
Created a web-based To-Do List application that allow the user to
keep a list of their important tasks.
It should contain:
    1) a short string describing the task (.e.g "Buy Milk")
    2) the email address of the person's responsible for the task
    3) the priority level (e.g. Low, Medium, or High)
"""

from flask import Flask, render_template, request, redirect


app = Flask(__name__)
to_do_list = []

task_list = [
        ['Buy groceries', 'blah@blah.com', 'High'],
        ['Take out the trash', 'person1@fake.com', 'Medium'],
        ['Buy gloves', 'none@none.org', 'Low']
    ]

@app.route('/')
def task_list():
    return render_template('to_do_list.html', to_do_list=to_do_list)


@app.route('/add_task')
def add_task():
    request.form['Add_Tasks.']
    return render_template('week_11_add.html')

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    render_template('ToDo.html', task=task, email=email, priority=priority)
    to_do_list.append({task:[email, priority]})
    return redirect('/')

@app.route('/clear')
def clear_To_Do():
    pass

if __name__ == "__main__":
    app.run(debug=True)
