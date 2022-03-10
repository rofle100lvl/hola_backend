import os

directory = 'Kits'

def filldb(db):
    db.clear_tables()
    for filename in os.listdir(directory):
        file_name = os.path.join(directory, filename)
        if os.path.isfile(file_name):
            print(filename)
            db.add_kit(filename[:-4])
            with open(file_name) as f:
                lines = f.readlines()
                for line in lines:
                    db.add_question(line[:-1])
                    db.add_relation(filename[:-4], line[:-1])
    with open('Developers/Description.csv') as f:
        lines = f.readlines()
        for line in lines:
            arg = line.split(',')
            db.add_developer(arg[0], arg[1], arg[2][:-1])



