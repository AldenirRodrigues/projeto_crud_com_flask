import flask
from flask import Flask, jsonify, request

import professor
import aluno

database = dict()
database['ALUNOS'] = []
database['professorers'] = []

app = Flask(__name__)


@app.route('/')
def all():
    return jsonify(database)


@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNOS'])


@app.route('/professores')
def professores():
    return jsonify(database['professor'])


@app.route('/alunos', methods=['POST'])
def novo_aluno():
    aluno_novo = request.get_json()
    database['ALUNOS'].append(aluno_novo)
    return jsonify(database['ALUNOS'])


@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404


app.run()
