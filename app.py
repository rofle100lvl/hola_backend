import json

from flask import Flask
from Models.Kit import Kit
from Models.Question import Question
from db import DataBase

app = Flask(__name__)

db = DataBase()


@app.route('/kits/', methods=['GET'])
def get_kits():
    result = db.get_kits_id()
    kits = []
    for res in result:
        kits.append(get_kit(res[0]).__dict__())
    return json.dumps(kits, ensure_ascii=False)


@app.route('/kit/<int:kit_id>', methods=['GET'])
def get_questions(kit_id):
    ans = json.dumps(get_kit(kit_id).__dict__(), ensure_ascii=False)
    return ans


def get_kit(kit_id):
    kit_res = db.get_kit(kit_id)
    if not kit_res:
        return ""
    kit_res = kit_res[0]
    questions_res = db.get_questions_by_kit(kit_id)
    kit = Kit(kit_res[0], kit_res[1], kit_res[2], kit_res[3], kit_res[4], kit_res[5])
    for res in questions_res:
        kit.cards.append(Question(res[0], res[1]).__dict__())
    return kit


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

    db.clear_tables()
