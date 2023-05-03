# 컨트롤러 start_app.py
# templates 폴더, static 폴더
# 웹 서버 - flask
# sql을 할때는 띄어쓰기를 주의할것...........................................

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'abc1234'


# url - '/' 경로 설정
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

def getconn():
    conn = sqlite3.connect("c:/green_project/sqlworks/pydb/memberdb.db")
    return conn

# 회원 목록 (경로이름 함수이름 똑같이하세연!)
@app.route('/memberlist', methods=['GET'])
def memberlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)  # 검색 수행
    rs = cursor.fetchall()
    # print(rs)
    conn.close()
    return render_template('memberlist.html', rs=rs)

#회원가입
@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == "POST":
        #가입 폼에 입력된 자료를 넘겨받기
        id = request.form['memberid']
        pw = request.form['passwd1']
        name = request.form['name']
        gender = request.form['gender']

        #db에 저장
        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO member(memberid, passwd, name, gender)" \
              f"VALUES ('{id}','{pw}','{name}','{gender}')"

        session['usedid'] = request.form['memberid']
        cursor.execute(sql)  #검색 수행
        conn.commit() #커밋 완료
        conn.close()

        # redirect : 회원가입 후 회원 목록 페이지로 강제로 이동
        return redirect(url_for('memberlist'))
    else:
        return render_template('register.html')


#로그인 페이지
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        #로그인 폼에 입력된 데이터 넘겨 받음
        id = request.form['memberid']
        pw = request.form['passwd']

        #database에 접속 - 로그인체크
        conn = getconn()
        cursor = conn.cursor()
        sql = f"SELECT * FROM member " \
              f"WHERE memberid = '{id}' AND passwd = '{pw}'"
        cursor.execute(sql)
        rs = cursor.fetchone()
        print(rs)
        conn.close()

        if rs: #rs - Ture
            session['usedid'] = rs[0] #memeberid를 세션에 저장(세션발급)
            return redirect(url_for('index'))
        else:
            error_msg = "아이디 비번 확인"
            return render_template("login.html", error_msg=error_msg)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

app.run()