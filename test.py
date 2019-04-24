'''
トンプソンサンプリングの
検証用スクリプト
'''

import random
from arm import Arm
from thompson_sampling import ThompsonSampling


ARM_NUM = 10
TRAIL_NUM = 100_000

if __name__ == '__main__':
    arms = [Arm(random.uniform(0.01, 0.2)) for i in range(ARM_NUM)]
    ts = ThompsonSampling(arms)
    ts.run(TRAIL_NUM)

    # 結果出力
    print([arms[i].p for i in range(len(arms))])
    print(ts.counts())
    print(ts.values)