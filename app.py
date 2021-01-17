from flask import Flask, redirect, request, jsonify
from datetime import datetime

app = Flask(__name__)


taskList = [
    {'name': 'MP1', 'status': True, 'createDate': datetime.today().strftime('%Y-%m-%d'), 
    'completeDate': datetime.today().strftime('%Y-%m-%d')},
    {'name': 'MP2', 'status': False, 'createDate': datetime.today().strftime('%Y-%m-%d'), 'completeDate': None}
]


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify(taskList)

@app.route('/complete', methods=['GET'])
def get_completedtasks():
    completedTasks = []
    for task in taskList:
        if(task['status'] == True):
            completedTasks.append(task)
    return jsonify(completedTasks)

@app.route('/complete/<index>', methods=['PUT'])
def complete_task(index):
    if(taskList[int(index)]['status'] == True):
        return "Task already completed"
    else:
        taskList[int(index)]['status'] = True
        taskList[int(index)]['completeDate'] = datetime.today().strftime('%Y-%m-%d')
        return redirect('/')

@app.route('/delete/<index>', methods=['DELETE'])
def delete_task(index):
    taskList.pop(int(index))
    return redirect('/')

@app.route('/create', methods=['POST'])
def create_task():
    task = {'name': request.values.get('name'), 'status': False, 'createDate': datetime.today().strftime('%Y-%m-%d'), 'completeDate': None}
    taskList.append(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)