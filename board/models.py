import mysql.connector
from django.db import models

# Create your models here.
from django.http import HttpResponseRedirect


def conn():
    return mysql.connector.connect(host='localhost', port='3306', database='webDB', user='webDB', password='webDB')

def countno():
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f"""select count(a.no) as count from board a, user b where a.user_no = b.no """
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results.get("count")

def scountno(kwd):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f'''select count(a.no) as count from board a join user b on a.user_no = b.no where a.contents like "%{kwd}%" or a.title like "%{kwd}%" or b.name like "%{kwd}%"'''
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results.get("count")

def maxgno():
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f"""select max(g_no) as max from board"""
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results.get("max")

def listcall(page,limit):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f"""select a.no, a.g_no, a.o_no, a.depth, a.title, b.name, a.hit, a.reg_date, a.user_no from board a join user b on a.user_no = b.no order by a.g_no desc, a.o_no asc limit {int(page)*10-10},{limit}"""
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def searchcall(page,limit,kwd):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f'''select a.no, a.g_no, a.o_no, a.depth, a.title, b.name, a.hit, a.reg_date, a.user_no from board a join user b on a.user_no = b.no where a.contents like "%{kwd}%" or a.title like "%{kwd}%" or b.name like "%{kwd}%" order by a.g_no desc, a.o_no asc limit {int(page)*10-10},{limit}'''
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def hit(no):
    def hitcount(hit):
        db = conn()
        cursor = db.cursor(dictionary=True)
        hit = hit+1
        query2 = '''update board set hit=%s where no=%s'''
        cursor.execute(query2, (hit, no))
        db.commit()
        cursor.close()
        db.close()
        return print(hit)
    db = conn()
    cursor = db.cursor(dictionary=True)
    query1 = f"""select hit from board where no={no}"""
    cursor.execute(query1)
    hit = cursor.fetchone()
    cursor.close()
    db.close()
    return hitcount(hit.get("hit"))

def contentscall(no):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f"""select no, title, contents, user_no, g_no, o_no, depth, hit from board where no={no}"""
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results

def insert (title, contents, no):
    db = conn()
    newgno = maxgno() + 1
    cursor = db.cursor(dictionary=True)
    query = """insert into board values(null, %s, %s, 0, %s, 1, 0, now(), %s)"""
    cursor.execute(query, (title,contents,newgno,no))
    db.commit()
    cursor.close()
    db.close()

def update(title, contents, no):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = '''update board set title=%s, contents=%s where no=%s'''
    cursor.execute(query, (title, contents, no))
    db.commit()
    cursor.close()
    db.close()

def delete(no):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = f'''delete from board where no={no}'''
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()

def reply(title, contents, gno, ono, depth, no):
    db = conn()
    cursor = db.cursor(dictionary=True)
    query = """insert into board values(null, %s, %s, 0, %s, %s, %s, now(), %s)"""
    cursor.execute(query, (title, contents, gno, ono, depth, no))
    db.commit()
    cursor.close()
    db.close()


