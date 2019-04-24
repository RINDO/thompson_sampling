import random


class Arm:
    '''バンディットアルゴリズムのアーム'''
    def __init__(self, p):
        self._p = p

    def draw(self):
        '''ベルヌーイ分布に従って報酬を出す'''
        if self._p > random.random():
            return 1
        else:
            return 0

    @property
    def p(self):
        return '{}%'.format(round(self._p * 100, 2))
