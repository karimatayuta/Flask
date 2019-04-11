# app.py
from flask   import Flask, render_template, request
from session import engine,Session # from : ファイル名 import : 値
from sample  import sample_model, post   # from : ファイル名 import : クラス

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    result  = session.query( sample_model ).all() # 全件取得　session.query(★★ class_name ★★).all()
    session.close()
    # app.logger.debug() # デバッグ用
    return render_template('index.html',result=result)

# 投稿ページ
@app.route('/post')
def post_page():
    return render_template('post.html')

# 投稿一覧ページ
@app.route('/post_list', methods=['POST'])
def post_list_page():
    title   = request.form['title'] # name を受け取る
    opinion = request.form['opinion']
    
    session = Session()
    
    post_list   = post(title=title,opinion=opinion)
    session.add(post_list)
    #session.add(opinion_db)
    session.commit()

    post_list  = session.query( post ).all()
    session.close()
    return render_template('post_list.html',post_list=post_list,title=title,opinion=opinion)

@app.route('/sample', methods=['POST'])
def sample():
    title   = request.form['title'] # name を受け取る
    opinion = request.form['opinion']

    session = Session()
    sample = sample_model(id=title) # インスタンスを作成
    session.add(sample) # データ追加
    session.commit() # データをDBへ反映
    session.close() # セッションを閉じる
    return render_template('sample.html',title = title, opinion = opinion)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

