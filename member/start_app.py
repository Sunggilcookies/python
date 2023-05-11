# 컨트롤러 start_app.py
# templates 폴더, static 폴더
# 웹 서버 - flask
# sql을 할때는 띄어쓰기를 주의할것...........................................
# 내용에 오류가있을시에는 홈페이지 에러가 뜰수있음 스펠링 잘 체크할것.

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'abc1234'


# url - '/' 경로 설정
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')
#맴버테이블과 연동

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
        # 자동 로그인 - 세션 발급
        session['userid'] = request.form['memberid']
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
            session['userid'] = rs[0] #memeberid를 세션에 저장(세션발급)
            return redirect(url_for('index'))
        else:
            error_msg = "아이디 비번 확인"
            return render_template("login.html", error_msg=error_msg)
    else:
        return render_template('login.html')

# 로그 아웃
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# 게시판 목록
@app.route('/boardlist', methods=['GET'])
def boardlist():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM board ORDER BY createdate DESC"
    cursor.execute(sql)
    boardlist = cursor.fetchall()

    conn.close()
    return render_template("boardlist.html", boardlist=boardlist)

# 글쓰기
@app.route('/writing', methods = ['GET','POST'])
def writing():
    if request.method == 'POST':
        #입력된 글을 저장해서 db에 저장
        title = request.form['title']
        # content = request.form[title]
        content = request.form['content']
        #userid : session 이름을 가져옴
        memberid = session.get('userid')

        conn = getconn()
        cursor = conn.cursor()
        sql = f"INSERT INTO board(title,content, memberid) "\
                f"VALUES('{title}', '{content} ','{memberid}')"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('boardlist'))
    else:
        return render_template('writing.html')

# 글 상세보기
@app.route('/detail/<int:bno>', methods=['GET'])
def detail(bno): #매개변수로 bno 설정
    # DB board 테이블에서 bno로 검색된 글 가져오기
    conn = getconn()
    cursor = conn.cursor()
    sql = f"SELECT * FROM board WHERE bno = {bno}"
    cursor.execute(sql) #DB에서 꺼내오는 애
    board = cursor.fetchone() #클릭하는 1개 보드에 저장
    return render_template('detail.html', board=board)
    #보드에 맞는 걸 보드에 저장

#게시물 삭제
@app.route('/delete/<int:bno>', methods=['GET'])
def delete(bno):
    conn = getconn()
    cursor = conn.cursor()
    sql = f"DELETE FROM board WHERE bno = {bno}" #숫자이므로 따음표 쓰지 않음;
    cursor.execute(sql)  # DB에서 꺼내오는 애
    conn.commit()
    conn.close()
    return render_template('boardlist.html')

app.run()