# 가상환경 설정, pip install flask flask_sqlalchemy 다운로드
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# DB기본 코드----------------------------------------------------

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.username} {self.title} 추천 by {self.username}'


with app.app_context():
    db.create_all()
# -----------------------------------------------------------------


@app.route("/")
def home():
    name = '데이터드림'
    motto = "메인페이지에 올라갈 내용을 적어주세요!-백두산 수정"

    context = {
        "name": name,
        "motto": motto,
    }
    return render_template('motto.html', data=context)


@app.route("/Introduce/")  # 경로 바꾸면 redirect경로도 바꿔주기
def music():
    song_list = Song.query.all()
    return render_template('Introduce.html', data=song_list)


@app.route("/music/<username>")
def render_music_filter(username):
    filter_list = Song.query.filter_by(username=username).all()
    return render_template('Introduce.html', data=filter_list)


@app.route("/music/create/")
def music_create():
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_receive = request.args.get("image_url")

    song = Song(username=username_receive, title=title_receive,
                artist=artist_receive, image_url=image_receive)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('Introduce'))


if __name__ == "__main__":
    app.run(debug=True)
#깃푸쉬 테스트 ㅇㄴㅁㄹㄴㅇㄹㄴㅇㄹㅇㄹㄹㄹㄹㄹㄹ