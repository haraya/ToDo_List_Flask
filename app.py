# import library Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #object from the class Flask


#example with real list
task = [
    "Buy milk",
    "Study French",
    "Do excercise",
    "I did coffee"
]

# Add task method
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        new_task = request.form['tarea']
        task.append(new_task)

    return render_template('index.html', nombre ="User", tasks = task)



# Remove task method
@app.route('/remove/<int:indice>')
def remove_task(indice):
    task.pop(indice)
    return redirect(url_for('home'))


# Edit task method
@app.route('/edit/<int:indice>', methods=['GET','POST'])
def edit_task(indice):
    if request.method == 'POST':
        task[indice] = request.form['tarea']
        return redirect(url_for('home'))
    return render_template('edit.html', indice=indice, task=task[indice])



if __name__ == "__main__":
    app.run(debug=True) # parameter debug=True