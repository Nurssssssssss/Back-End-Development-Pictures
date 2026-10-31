"""Picture REST endpoints following the IBM capstone /picture contract."""
import json
from pathlib import Path
from flask import jsonify, request
from . import app

_data_file = Path(__file__).parent / 'data' / 'pictures.json'
data = json.loads(_data_file.read_text(encoding='utf-8'))

@app.get('/health')
def health():
    return jsonify(status='OK'), 200

@app.get('/count')
def count():
    return jsonify(length=len(data)), 200

@app.get('/picture')
def get_pictures():
    return jsonify(data), 200

@app.get('/picture/<int:id>')
def get_picture_by_id(id):
    picture = next((item for item in data if item['id'] == id), None)
    if picture is None:
        return jsonify(message='picture not found'), 404
    return jsonify(picture), 200

@app.post('/picture')
def create_picture():
    item = request.get_json(silent=True)
    if not isinstance(item, dict) or not isinstance(item.get('id'), int) or not item.get('pic_url'):
        return jsonify(message='id (integer) and pic_url required'), 400
    if any(record['id'] == item['id'] for record in data):
        return jsonify(Message=f"picture with id {item['id']} already present"), 302
    data.append(item.copy())
    return jsonify(item), 201

@app.put('/picture/<int:id>')
def update_picture(id):
    item = request.get_json(silent=True)
    if not isinstance(item,dict):
        return jsonify(message='JSON object required'), 400
    for i, record in enumerate(data):
        if record['id'] == id:
            updated = {**record, **{k:v for k,v in item.items() if k != 'id'},'id':id}
            data[i]=updated
            return jsonify(updated), 200
    return jsonify(message='picture not found'), 404

@app.delete('/picture/<int:id>')
def delete_picture(id):
    for i, record in enumerate(data):
        if record['id']==id:
            data.pop(i)
            return '',204
    return jsonify(message='picture not found'),404
