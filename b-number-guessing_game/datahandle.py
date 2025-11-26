# using sqlite for data handling
import sqlite3 

conn = sqlite3.connect("b-number-guessing_game/scores.db")
conn.execute('CREATE TABLE IF NOT EXISTS scores (name TEXT, attempts INTEGER)')
conn.commit()

def add_score(name,attempts):
    conn.execute('INSERT INTO scores (name, attempts) VALUES (?,?)',(name,attempts))
    conn.commit()

    conn.execute('DELETE FROM scores WHERE rowid NOT IN (SELECT rowid FROM scores ORDER BY attempts ASC LIMIT 5)')

def get_score():
    return conn.execute('SELECT name, attempts FROM scores ORDER BY attempts ASC LIMIT 5').fetchall()

def clear_score():
    conn.execute('DELETE FROM scores')
    conn.commit()
    print("All scores have been cleared")

clear_score()

# add_score("",110)

score_data = get_score()
print(len(score_data))
print(score_data[0])
print(score_data[0][0])
score_lst = []
for i in range (0,len(score_data)):
    score_lst.append(score_data[i][1])


new_score = 5
if new_score<max(score_lst):
    ask = input("Enter your name, your score was in top 5 : ")
    add_score(ask,5)