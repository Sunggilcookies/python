import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

def select():
    conn = sqlite3.connect("c:/pydb/mydb.db")  # 연결 객체 생성
    # print(conn)
    cursor = conn.cursor()  # cursor 클래스 변수 생성
    sql = "SELECT * FROM employee"
    cursor.execute(sql)  # execite() - #모든 조작(삽입, 검색, 수정, 삭제)를 수행하는 함수
    # 전체검색 - fetchall(), 특정 1개 검색 fetchone()
    rs = cursor.fetchall()  # 자료 구조가 리스트, 개별요소는 튜플임
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn =sqlite3.connect("c:/pydb/mydb.db")
    cursor = conn.cursor()
    sql = "UPDATE employee SET age=40 WHERE empid = 'e101'"
    cursor.execute(sql)
    conn.commit() #삽입, 수정, 삭제 시에 반드시 커밋 해줌
    conn.close()

def update():
    conn =sqlite3.connect("c:/pydb/mydb.db")
    cursor = conn.cursor()
    sql = "UPDATE employee SET age=40 WHERE empid = 'e101'"
    cursor.execute(sql)
    conn.commit() #삽입, 수정, 삭제 시에 반드시 커밋 해줌
    conn.close()

def select_one(): #특정요소 검색
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM employee WHERE empid = 'e103'"
    cursor.execute(sql)
    rs = cursor.fetchone()
    print(rs)
    conn.close()

def delete():
        conn = sqlite3.connect("c:/pydb/mydb.db")
        cursor = conn.cursor()
        sql = "DELETE FROM employee WHERE empid = 'e102'"
        cursor.execute(sql)
        conn.commit()  # 삽입, 수정, 삭제 시에 반드시 커밋 해줌
        conn.close()


#메인 영역에서 호출해서 사용
# update()
#insert()
select()
delete()
# select_one()
