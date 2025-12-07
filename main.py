from random import random
def getInputs():
    '''
    乒乓球规则是一局比赛中先得11分为胜,10平时,先得2分为胜
    一场比赛采用三局两胜，当每人各赢一局时，最后一局为决胜局
    :return: 两位选手在各自发球回合中的获胜概率
    '''
    probA = float(input("请输入选手A的能力值(0-1):"))
    probB = float(input("请输入选手B的能力值(0-1):"))
    return probA, probB


def simOneGame(probA, probB):
    '''
    模拟一局比赛
    :param probA: A在发球回合的获胜概率
    :param probB: B在发球回合的获胜概率
    :return: 获胜方的选手编号A或B
    '''
    scoreA, scoreB = 0, 0
    serving = 'A'
    i = 1
    while not gameOver(scoreA, scoreB):
        serving = switchServing(i, serving)
        i += 1

        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
    print(scoreA, '---', scoreB)
    return Winner(scoreA, scoreB)

def gameOver(scoreA, scoreB):
    """判断一局比赛是否结束(最大比分12:10)"""
    # 只允许：11:0-11:9 或 12:10 结束比赛
    return (max(scoreA, scoreB) == 11 and abs(scoreA - scoreB) >= 2) or \
           (max(scoreA, scoreB) == 12 and abs(scoreA - scoreB) == 2)

def switchServing(i, serving):
    '''
    根据发球次数，换发球权
    :param i: 发球次数
    :param serving: 发球选手
    :return: 此时发球选手
    '''
    if i % 2 == 0 and i > 0:
        if serving == 'A':
            serving = 'B'
        else:
            serving = 'A'
    return serving

def Winner(scoreA, scoreB):
    '''
    判断一局比赛的获胜方
    :param scoreA: A的得分
    :param scoreB: B的得分
    :return: 获胜方选手编号A或B
    '''
    if scoreA ==12 or scoreB == 12:
        if scoreA == 12:
            return 'A'
        else:
            return 'B'
    else:
        if scoreA == 11:
            return 'A'
        else:
            return 'B'

def simOneChampion():
    '''
    模拟一场比赛
    :return: 无
    '''
    A, B, round = 0, 0, 1 #A,B分别获胜局数，round为当前进行的局次
    probA, probB = getInputs()

    while True:
        print('第{}局'.format(round))
        r = simOneGame(probA, probB)
        round += 1
        if r == 'A':
            A += 1
        else:
            B += 1
        if A == 2:
            print('A获胜')
            break
        elif B == 2:
            print('B获胜')
            break
        else:
            continue

simOneChampion()
