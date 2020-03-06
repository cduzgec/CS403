from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {} #resource 

class HelloWorld(Resource):  #@app.route but we didnt give extra route so its index route
    def get(self):
        return {
            'secret': 'value'
        }

class TodoSimple(Resource):
    def get(self, todo_id):
        item = todos.get(todo_id, {})
        if not item:
            return item, 404 #item is not found
        return item

    def put(self, todo_id):
        todos[todo_id] = request.form['content']
        return {
            todo_id: todos[todo_id]
        }, 201

api.add_resource(HelloWorld, '/')  #adding resource 
api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
