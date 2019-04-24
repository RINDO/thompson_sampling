import random
import numpy as np
from tqdm import tqdm

class ThompsonSampling:
    '''トンプソンサンプリング'''

    def __init__(self, arms):
        self._arms = arms
        self._a = np.zeros(len(arms), dtype=int)
        self._b = np.zeros(len(arms), dtype=int)
        self._values = np.zeros(len(arms))

    def run(self, trail_num):
        '''探求と活用'''
        for _ in tqdm(range(trail_num)):
            index = self.__select_arm_index()
            self.__update(index)

    def counts(self):
        '''アームごとの検証回数を返す'''
        return [self._a[i] + self._b[i] for i in range(len(self._arms))]

    @property
    def values(self):
        return self._values.tolist()
  
    def __select_arm_index(self):
        exps = [random.betavariate(self._a[i]+1, self._b[i]+1) for i in range(len(self._arms))]
        return np.argmax(exps)

    def __update(self, index):
        reward = self._arms[index].draw()
        self._values[index] += reward
        if reward > 0:
            self._a[index] += 1
        else:
            self._b[index] += 1
