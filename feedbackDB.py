import sqlite3

con = sqlite3.connect('feedbacks.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
        CREATE TABLE IF NOT EXISTS fb(
            name VARCHAR2(200),
            cmnt VARCHAR2(1000000000000000000000000000)
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS fbBackUp AS SELECT * FROM fb WHERE 1=1;
    """)

def createFeedback(name,cmnt):
    db.execute("INSERT INTO fb VALUES (?,?)",(name,cmnt))
    db.execute("INSERT INTO fbBackUp VALUES (?,?)",(name,cmnt))
    con.commit()

def getFeedbacks():
    db.execute("SELECT * FROM fb")
    fb = db.fetchall()
    return fb


#createTable()


