#member 테이블과 연동
#board 테이블과 연동

import sqlite3



def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/memberdb.db")
    return conn
print(getconn(), "연결 객체 생성됨")

#board 테이블 연동
#board 테이블 생성
def create_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE board(
        bno INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        createdate DATETIME DEFAULT (datetime('now','localtime')),
        hit INTEGER DEFAULT 0,
        memberid TEXT NOT NULL ,
        FOREIGN KEY(memberid) REFERENCES member(memberid) ON DELETE CASCADE
        
    )
"""
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성!")
# 함수 호출

def drop_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "DROP TABLE board"
    cursor.execute(sql)
    conn.commit()
    conn.close()





def insert_board():
    conn = getconn()
    cursor = conn.cursor()
    sql = "INSERT INTO board(title, content, memberid) VALUES (?, ?, ?)"
    cursor.execute(sql, ('가입인사', '안녕하세요.. 유성길입니다.', 'rabbitsg1234'))
    conn.commit()
    conn.close()






def select_board():




# drop_board()
# create_board()
# insert_board()
select_board()

# def insert():
#     conn = getconn()
#     cursor = conn.cursor()
#     # 동적바인딩
#     sql = "INSERT INTO member(memberid, passwd, name, gender)"
#           "VALUES (?,?,?,?)"
#     cursor.execute(sql, ('today123','m123456$', '투데이', '여'))# 검색 수정
#     conn.commit() #커밋완료
#     conn.close()

# def select_one():
#     conn = getconn()
#     cursor = conn.cursor()
#     sql = "SELECT * FROM member WHERE memberid = ? AND passwd = ?"
#     cursor.execute(sql,('test', 'test1234'))
#     rs = cursor.fetchone()
#     print(rs)
#     conn.close()






