import time
import calendar

dict = {
  "你好": "你好",
  "很高兴见到您": "我也很高心见到你",
  "你喜欢吃什么水果": "我喜欢橘子",
  "你今年多大了": "18岁了",
  "你很漂亮": "谢谢",
  # "现在的时间": "你好",
  # "这个月的阳历": "你好",
}

flag = ('A')
work = True
print('你好，我是你的机器人助手\n')
print('请问有时间和我聊聊么\n')

while flag == 'A' or 'B':
  flag = input('A:陪我聊天,B:训练我聊天,C:给我翻译,D:天气,E:结束\n')
  if flag == "B":
      question = input('请输入你想问的\n')
      answer = input('请输入问题的答案\n')
      dict[str(question)] = str(answer)
      print('学习成功\n')
      print('现在我已经学会了%d个问题\n'%len(dict))
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
      elif flag == 'E':
          print('好的，我们下次再聊\n')
          break
      else:
          continue
      # elif flag == 'C':
