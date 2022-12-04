import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="g52hS9C8C6aT",
  database="challenge"
)

cursor = db.cursor()


def creat_user(id:str):
    if search(id):
        return "**This discord id already have an account**"
    
    query = f"INSERT INTO SCOREBOARD (SCORE,DC_ID,LEVEL) VALUES(0,'{id}',0)"
    try:
        cursor.execute(query)
        db.commit()

    except Exception as e:
        print(str(e))

    return "User Create Succeed"

#Create db query
def creat_db():
    
    query = """CREATE TABLE SCOREBOARD
    (DC_ID INT NOT NULL,
    SCORE INT NOT NULL,
    LEVEL BIGINT NOT NULL);"""

    cursor.execute(query)
    db.commit()
    return "Datebase created"
    
def search(id:str):
    cursor.execute(f"SELECT * FROM SCOREBOARD WHERE DC_ID='{id}'")
    return cursor.fetchall()

    
def insert(id:str,score:int,level:int):
    
        query = f"SELECT * FROM SCOREBOARD WHERE DC_ID='{id}';"
        cursor.execute(query)
        res = cursor.fetchall()
        
        if not(res):
            return "**User not found**"

        query = f"UPDATE SCOREBOARD SET SCORE=SCORE+'{score}', LEVEL='{level}' WHERE DC_ID='{id}'"
        cursor.execute(query)
        db.commit()
        
        return "Update succeed"

def test():

    query = f"SELECT * FROM SCOREBOARD"
    cursor.execute(query)
    
    return cursor.fetchall()

def readflag():

    query = f"SELECT * FROM info"
    cursor.execute(query)
    res = cursor.fetchall()
    flag = []

    for k in res:

        flag.append(k[2])
    
    return flag

def info():

    query = "SELECT * FROM info"
    cursor.execute(query)
    res = cursor.fetchall()

    return res    

def instance_validate(id:str):

    query = f"SELECT * FROM instance WHERE `id`={id}"
    cursor.execute(query)
    res = cursor.fetchall()

    if(not(res)):

        return True

    else:
        return False

def find_used_port():

    query = "SELECT * FROM instance"
    cursor.execute(query)
    res = cursor.fetchall()
    port_list = [] 

    for i in res:

        port_list.append(i[2])
    
    return port_list


def save_instance_record(dc_id:str,container_id:str,port:int):

    query = f"INSERT INTO instance(`container`, `id`, `port`) VALUES ('{container_id}','{dc_id}',{port})"
    cursor.execute(query)
    db.commit()

def id_to_container(id:str):

    query = f"SELECT * FROM instance WHERE `id`= '{id}'"
    cursor.execute(query)
    res = cursor.fetchall()
    return res[0]

def remove_container(id:str):

    query = f"DELETE FROM instance WHERE `id` = '{id}'"
    cursor.execute(query)
    db.commit()

def can_create(level:int):

    start_list = [14]
    if(level in start_list): return True
    else: return False
    

