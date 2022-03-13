import json

from flask import Flask
from Models.Kit import Kit
from Models.Question import Question
from Models.Developer import Developer
from db import DataBase
from dbfiller import filldb

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
    kit = get_kit(kit_id)
    ans = json.dumps(kit.__dict__(), ensure_ascii=False)
    return ans


@app.route('/developers/', methods=['GET'])
def get_developers():
    results = db.get_developers()
    developers = []
    for result in results:
        developers.append(Developer(result[0], result[1], result[2], result[3], result[4]).__dict__())
    return json.dumps(developers, ensure_ascii=False)


def get_kit(kit_id):
    kit_res = db.get_kit(kit_id)
    if not kit_res:
        return []
    kit_res = kit_res[0]
    questions_res = db.get_questions_by_kit(kit_id)
    kit = Kit(kit_res[0], kit_res[1], kit_res[2], kit_res[3], kit_res[4], kit_res[5], kit_res[6])
    for res in questions_res:
        kit.cards.append(Question(res[0], res[1]).__dict__())
    return kit


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
