import mysql.connector

def conn():
    return  mysql.connector.connect(host='localhost', port='3306', database='webDB', user='webDB', password='webDB')

def findall():
    db = conn()

    # cursor install
    cursor = db.cursor(dictionary=True)

    # query activate
    query = """select no, name, message, date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date
                from guestbook 
                order by reg_date desc"""
    cursor.execute(query)

    # result received
    results = cursor.fetchall()

    # resource close
    cursor.close()
    db.close()

    #반환
    return results

def insert (name, password, message):
    db = conn()

    # cursor install
    cursor = db.cursor(dictionary=True)

    # insert query activate
    query = """insert into guestbook values(null, %s, %s, %s, now()) """

    # 입력하는거라 결과값을 따로 받지 않고, 처리된 결과에 대해서 확인
    count = cursor.execute(query, (name,password,message))

    # commit (insert, update, delete는 반드시 닫아줘야함)
    db.commit()

    # resource close
    cursor.close()
    db.close()

    #return
    return count == 1

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