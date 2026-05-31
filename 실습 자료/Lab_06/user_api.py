# [실습 3] API Specification
# 미션: AI에게 "이 코드의 OpenAPI(Swagger) 스펙을 YAML로 작성해줘"라고 요청하세요.
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify({"id": id, "name": "Test User"})

@app.route('/users', methods=['POST'])
def create_user():
    return jsonify({"status": "created"}), 201
