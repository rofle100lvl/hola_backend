import json

from flask import Flask
from Models.Kit import Kit
from Models.Question import Question
from db import DataBase
import os
from dbfiller import filldb

app = Flask(__name__)

db = DataBase()


@app.route('/kits/', methods=['GET'])
def get_kits():
    result = db.get_kits()
    kits = []
    for res in result:
        kits.append(Kit(id=res[0], name=res[1]).__dict__())
    ans = json.dumps(kits)
    ans = ans.encode('utf-8')
    return ans


@app.route('/questions/<int:kit_id>', methods=['GET'])
def get_questions(kit_id):
    result = db.get_questions_by_kit(kit_id)
    questions = []
    for res in result:
        questions.append(Question(res[0], res[1]).__dict__())
    print(questions)
    ans = json.dumps(questions)
    ans = ans.encode('utf-8')
    return ans


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    db.clear_tables()
