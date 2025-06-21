from flask import Flask, request, jsonify
import pymongo

client = pymongo.MongoClient('mongodb+srv://darshil_nakrani:YNIRy5LtNeZ5dN36@cluster0.nipgkfg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.test
collection = db['flask-assignment']

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the backend"

@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.json)
    print(data)
    try:
        collection.insert_one(data)
        return jsonify({'success': True, 'message': 'Inserted Successfully'}), 200
    except Exception as e:
        print("Insert error:", str(e))
        return jsonify({'success': False, 'message': str(e)}), 500
    
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({'success': False, 'message': 'Both itemName and itemDescription are required'}), 400

    todo_item = {
        'itemName': item_name,
        'itemDescription': item_description
    }

    try:
        collection.insert_one(todo_item)
        return jsonify({'success': True, 'message': 'To-Do item inserted successfully'}), 201
    except Exception as e:
        print("Insert error:", str(e))
        return jsonify({'success': False, 'message': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)