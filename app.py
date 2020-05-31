from flask import Flask, jsonify, render_template, request, redirect, url_for
from basics.pg_tools import pgdb
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return jsonify({'code': '1', 'message': '正在运行'})


@app.route('/get_tools')
def get_tools_address():
    pg = pgdb()
    result = pg.select(table_name='tools_address')
    return jsonify({'code': 1, 'result': result})


@app.route('/update_tools', methods=['POST', 'GET'])
def update_tools_address():
    if request.method == 'POST':
        req = request.get_json()
        id = req.pop("id")
        tools_name = req.pop("toolsName")
        tools_address = req.pop("toolsAddress")
        data = {
            'id': id,
            'tools_name': tools_name,
            'tools_address': tools_address,
        }
        try:
            pg = pgdb()
            pg.update(table_name='tools_address', id=id, data=data)
            return jsonify({'code': 1, 'message': '修改成功'})
        except Exception as e:
            return jsonify({'code': 0, 'message': e})
    else:
        return jsonify({'code': 0, 'message': '请使用POST提交'})


@app.route('/delete_tools', methods=['POST', 'GET'])
def delete_tools_address():
    req = request.get_json()
    id = req.pop("id")
    try:
        pg = pgdb()
        pg.delete(table_name='tools_address', id=id)
        return jsonify({'code': 1, 'message': '删除成功'})
    except Exception as e:
        return jsonify({'code': 0, 'message': e})


@app.route('/insert_tools', methods=['POST', 'GET'])
def insert_tools_address():
    if request.method == 'POST':
        req = request.get_json()
        tools_name = req.pop("toolsName")
        tools_address = req.pop("toolsAddress")
        data = {
            'tools_name': tools_name,
            'tools_address': tools_address,
        }
        try:
            pg = pgdb()
            pg.insert(table_name='tools_address', data=data)
            return jsonify({'code': 1, 'message': '新增成功'})
        except Exception as e:
            return jsonify({'code': 0, 'message': e})
    else:
        return jsonify({'code': 0, 'message': '请使用POST提交'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
