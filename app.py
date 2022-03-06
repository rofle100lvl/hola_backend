import json

from flask import Flask
from Models.Kit import Kit
from Models.Question import Question
from db import DataBase

app = Flask(__name__)

db = DataBase()


@app.route('/kits/', methods=['GET'])
def get_kits():
    ans = ""
    result = db.get_kits()
    for res in result:
        kit = Kit(id=res[0], name=res[2], number=res[1])
        ans += json.dumps(kit.__dict__())
    return ans


@app.route('/questions/<int:kit_id>', methods=['GET'])
def get_questions(kit_id):
    ans = ""
    result = db.get_questions_by_kit(kit_id)
    if result is None:
        return ans
    elif type(result) != type(list):
        result = [result]

    for res in result:
        question = Question(res[0], res[1], res[2])
        ans += json.dumps(question.__dict__())
    return ans


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    db.clear_tables()
