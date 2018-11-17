import MySQLdb

# MySQLサーバーに接続し、コネクションを取得する。
# ユーザー名とパスワードを指定してscrapingデータベースを使用する。接続に使用する文字コードはutf8mb4とする。
conn = MySQLdb.connect(db='scraping', user='root', passwd='', charset='utf8mb4')

c = conn.cursor() # カーソルを取得する

# execute()メソッドでSQL文を実行する。
# スクリプトを何回実行しても同じ結果になるようにするため、citiesテーブルが存在する場合は削除する。
c.execute('DROP TABLE IF EXISTS cities')

# citiesテーブルを作成する。
c.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        rank_id int,
        city varchar(10),
        population int
    )
''')

# パラメータで置き換える場所（プレースホルダー）は%sで指定する。
c.execute('insert into cities values(%s,%s,%s)',(1,'東京',20180101))

conn.commit() # 変更をコミット（保存）する

c.execute('select * from cities') # 保存したデータを取得する。
for row in c.fetchall(): # クエリの結果はfetchall()メソッドで取得できる。
    print(row)

conn.close()