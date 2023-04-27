from flask import Flask, render_template

app = Flask(__name__) #app 객체 생성

@app.route('/')
def index():
    return render_template('index.html') #html 페이지 보내기

@app.route('/season')
def get_season():
    season = '봄'
    return render_template('season.html', season=season)


if __name__ == '__main__':
    app.run('127.0.0.1',port=5000,debug=True)

app.run()