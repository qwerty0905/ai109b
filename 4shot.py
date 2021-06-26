# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:47:41 2021

@author: user
"""

import random

screen = [] #棋盤列表

def into():#初始空白棋盤
  for i in range(6):
    list_width=[]
    for j in range(8):
      list_width.append(' '+'|')
    screen.append(list_width)

def screen_print():#列印棋盤
  print('',1,2,3,4,5,6,7,8,sep=' ')
  print('', 1, 2, 3, 4, 5, 6, 7, 8, sep=' ', file=file, flush=True)
  for i in range(6):
    print('|',end='')
    print('|', end='', file=file, flush=True)
    for j in range(8):
      print(screen[i][j],end='')
      print(screen[i][j], end='', file=file, flush=True)
    print('')
    print('', file=file, flush=True)
  print('——'*(9))
  print('——' * (9), file=file, flush=True)

def eeferee():#判斷輸贏
  #判斷行
  for i in range(6):
    for j in range(8-3):
      if screen[i][j][0]==screen[i][j+1][0]==screen[i][j+2][0]==screen[i][j+3][0] and screen[i][j][0]!=' ':
        return False
  #判斷列
  for i in range(6-3):
    for j in range(8):
      if screen[i][j][0]==screen[i+1][j][0]==screen[i+2][j][0]==screen[i+3][j][0] and screen[i][j][0]!=' ':
        return False
  #判斷斜線
  for i in range(3):
    for j in range(5):
      if screen[i][j][0]==screen[i+1][j+1][0]==screen[i+2][j+2][0]==screen[i+3][j+3][0] and screen[i][j][0]!=' ':
        return False
      if j>=3:
        if screen[i][j][0] == screen[i+1][j-1][0] == screen[i+2][j-2][0] == screen[i+3][j-3][0] and screen[i][j][0] != ' ':
          return False
  return True

def full():
  for i in screen:
    for j in i:
      if j[0] == ' ':
        return True
  return False

def lara(): # 勞拉
  global screen
  while True:
    coordinate=random.randint(0,7)
    flag = True
    high = 0
    for i in range(5,-1,-1):
      if screen[i][coordinate][0] == ' ':
        high = i
        break
      if i == 0 and screen[i][coordinate][0] != ' ':
        flag = False
    if flag:
      print('>>>輪到我了,我把O棋子放在第%d列...'%(coordinate+1))
      print('>>>輪到我了,我把O棋子放在第%d列...' % (coordinate + 1), file=file, flush=True)
      screen[high][coordinate] = 'O' + '|'
      break
  screen_print()

def user():
  global screen
  while True:
    print(">>>輪到你了,你放X棋子,請選擇列號(1-8): ",end='')
    print(">>>輪到你了,你放X棋子,請選擇列號(1-8): ", end='', file=file, flush=True)
    coordinate = int(input())-1
    if coordinate not in range(87):
      print('輸入錯誤的列號，請重新輸入')
      print('輸入錯誤的列號，請重新輸入', file=file, flush=True)
      continue
    flag=True
    high=0
    for i in range(5,-1,-1):
      if screen[i][coordinate][0] == ' ':
        high=i
        break
      if i==0 and screen[i][coordinate][0] != ' ':
        flag = False
        print('你輸入的地方已經有棋子了，請重新輸入')
        print('你輸入的地方已經有棋子了，請重新輸入', file=file, flush=True)
    if flag:
      screen[high][coordinate] = 'X' + '|'
      break
  screen_print()


if __name__ == '__main__':
  file=open('四連環Log-%d.txt'%random.randint(10000,99999),'w',encoding='utf-8')
  print("""我們來玩一局四連環。我用O型棋子，你用X型棋子。
遊戲規則：雙方輪流選擇棋盤的列號放進自己的棋子，
    若棋盤上有四顆相同型號的棋子在一行、一列或一條斜線上連線起來，
    則使用該型號棋子的玩家就贏了!""")
  print("""Hi,我是勞拉，我們來玩一局四連環。我用O型棋子，你用X型棋子。
  遊戲規則：雙方輪流選擇棋盤的列號放進自己的棋子，
      若棋盤上有四顆相同型號的棋子在一行、一列或一條斜線上連線起來，
      則使用該型號棋子的玩家就贏了!""", file=file, flush=True)
  into()
  print('開始了！這是棋盤的初始狀態：')
  print('開始了！這是棋盤的初始狀態：', file=file, flush=True)
  screen_print()
  flag=True
  while eeferee() and full():
    lara()
    if not eeferee() and full():
      flag=False
      break
    user()
  if full():
    print('******* 難分勝負！@_@')
    print('******* 難分勝負！@_@', file=file, flush=True)
  if flag:
    print('******* 好吧，你贏了！^_^')
    print('******* 好吧，你贏了！^_^', file=file, flush=True)
  else:
    print('******* 耶，我贏了！^_^')
    print('******* 耶，我贏了！^_^', file=file, flush=True)