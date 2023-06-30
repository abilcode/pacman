from sqlalchemy import create_engine, text
import sqlite3

PATH = 'Users/abilfad/Documents/CODE'
CONFIG = (f'sqlite:////{PATH}/pacman/tugas_1/project : intro to Software and Data Engineering/data/tugas_1.db')

print(CONFIG)

engine = create_engine(CONFIG)
conn = engine.connect()

# # bikin table
# querry = text(
#     """
#     CREATE TABLE loan(
#     ID INT PRIMARY KEY,
#     nama VARCHAR(255)
#     )
#     """
# )


dict_input = {
    'ID':1,
    'nama':'Alex',
}

querry = text(
    """
    INSERT INTO loan (ID,nama)
    VALUES (:ID,:nama)
    """
)

conn.execute(querry,
             ID = dict_input['ID'],
             nama = dict_input['nama']
             )

conn.close()

