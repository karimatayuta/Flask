# GitHub 自動化
import subprocess

print('please input file')
text = input()

# ファイルをインデックス追加（コマンド入力）
index = 'git add {}'.format(text)
subprocess.call(index.split())

print('please input comment')
comment = input()

# ファイルを登録（コミット）
comment = 'git commit -m {}'.format(comment)
subprocess.call(comment.split())

# データの送信
push = 'git push origin master'
subprocess.call(push.split())

print('file_name:'+ text +' commit:'+ push +'')