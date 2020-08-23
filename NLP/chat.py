import time
import calendar

import cPickle as pickle

flag = ('A')
work = True
print('你好，我是你的机器人助手\n')
print('让我们一起聊聊天吧\n')

while flag == 'A' or 'B':
  flag = input('A:陪我聊天,B:训练我聊天,C:给我翻译,D:天气,E:结束\n X:查看字典\n a: 测试写入数据\n')
  if flag == "B":
      question = input('请输入你想问的\n')
      answer = input('请输入问题的答案\n')
      dict[str(question)] = str(answer)
      print('学习成功\n')
      print('现在我已经学会了%d个问题\n'%len(dict))
      # 将训练后的数据写入到字典中
      # dict.update({str(question): str(answer)})
      continue
  elif flag == 'A':
      if len(dict) == 0:
          print("现在我还不会回答任何问题，请让我学习;\n")
          continue
      chat_world = input('谢谢你跟我聊天，你想对我说点什么？\n')

      for key in sorted(dict.keys()):
          if str(chat_world) == key:
              work = True
              print(dict[key])
              break
          else:
              work = False
      if work == False:
          print('sorry，这个问题我回答不上来\n')
          work = True
  elif flag == 'E': # ending
      print('好的，我们下次再聊\n')
      break
  elif flag == 'X':
      # check dict information
      print(dict)
  elif flag == 'a':
      # print(dict)
      # dict.update(hello = 'hi')
      # print(dict)
      exDict = { 'hello': 'hi' }
      with open('./dict/chatDict.py', 'r', encoding='utf-8') as f:
          print(f.read())
          f.write(pickle.dumps(exDict))
          print(f.read())
