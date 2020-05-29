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


@app.route('/update_tools')
def update_tools_address():
    data = {}
    try:
        pg = pgdb()
        pg.insert(table_name='tools_address', data=data)
        return jsonify({'code': 1, 'message': '新增成功'})
    except Exception as e:
        return jsonify({'code': 0, 'message': e})


@app.route('/delete_tools')
def delete_tools_address():
    id = ''
    try:
        pg = pgdb()
        pg.delete(table_name='tools_address', id=id)
        return jsonify({'code': 1, 'message': '删除成功'})
    except Exception as e:
        return jsonify({'code': 0, 'message': e})


@app.route('/insert_tools', methods=['POST'])
def insert_tools_address():
    data = {}
    try:
        pg = pgdb()
        pg.insert(table_name='tools_address', data=data)
        return jsonify({'code': 1, 'message': '插入成功'})
    except Exception as e:
        return jsonify({'code': 0, 'message': e})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
