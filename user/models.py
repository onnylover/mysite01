import mysql.connector

def conn():
    return  mysql.connector.connect(host='localhost', port='3306', database='webDB', user='webDB', password='webDB')

def findbyno(no):
    #이름, 이메일, 성별을 updateform 에 뿌려줌
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f"select name, email, gender, password from user where no={no}"
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results

def findbyemail_and_password(email, password):
    db = conn()

    # cursor install
    cursor = db.cursor(dictionary=True)

    # query activate
    query = """select no, name from user where email=%s and password=%s"""
    cursor.execute(query, (email, password))

    # result received
    #여러개 가지고 올때
    #results = cursor.fetchall()
    #하나를 가지고 올때
    results = cursor.fetchone()

    # resource close
    cursor.close()
    db.close()

    # 반환
    return results

def insert (name, email, password, gender):
    db = conn()

    # cursor install
    cursor = db.cursor(dictionary=True)

    # insert query activate
    query = """insert into user values(null, %s, %s, %s, %s, now()) """

    # 입력하는거라 결과값을 따로 받지 않고, 처리된 결과에 대해서 확인
    count = cursor.execute(query, (name,email,password,gender))

    # commit (insert, update, delete는 반드시 닫아줘야함)
    db.commit()

    # resource close
    cursor.close()
    db.close()

    #return
    return count == 1

def update(name, password, gender, no):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = '''update user set name=%s, password=%s, gender=%s where no=%s'''
    count = cursor.execute(query, (name, password, gender, no))
    db.commit()
    cursor.close()
    db.close()

def deletebynoandpw(no, password):
    db = conn()

    # cursor install
    cursor = db.cursor(dictionary=True)

    # insert query activate
    query = '''delete from guestbook where no=%s and password=%s'''

    # 입력하는거라 결과값을 따로 받지 않고, 처리된 결과에 대해서 확인
    count = cursor.execute(query, (no,password))

    # commit (insert, update, delete는 qksemtl vlfdygka)
    db.commit()

    # resource close
    cursor.close()
    db.close()