import os

directory = 'Kits'
colors = {'Незнакомая компания' : ['#C5DD9D', '#58B5BB'],
          'Познание себя': ['#F4F1CF', '#F4F1CF'],
          'Для пары': ['#ADE2F2', '#4E81B0'],
          'Круг Друзей': ['#E2E392', '#BB83C0']}

descriptions = {
          'Незнакомая компания' : 'Вопросоы, которые помогут вам сделать неуклюжую беседу проще',
          'Познание себя': 'Ключ к достижению личного успеха. Однако научиться понимать себя не так-то просто.',
          'Круг Друзей': 'Список отличных вопросов, которые помогут сблизиться, повеселиться и лучше узнать своих друзей.',
          'Для пары': 'Для тех, кто хочет узнать свою вторую половинку получше'}

links = {

}


def filldb(db):
    db.clear_tables()
    for filename in os.listdir(directory):
        file_name = os.path.join(directory, filename)
        if os.path.isfile(file_name):
            print(filename)
            db.add_kit(filename[:-4], colors[filename[:-4]][0], colors[filename[:-4]][1], descriptions[filename[:-4]])
            with open(file_name) as f:
                lines = f.readlines()
                for line in lines:
                    db.add_question(line[:-1])
                    db.add_relation(filename[:-4], line[:-1])
    with open('Developers/Description.csv') as f:
        lines = f.readlines()
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            arg = line.split(',')

            db.add_developer(arg[0], arg[1], arg[2], arg[3])

