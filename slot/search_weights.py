"""老虎机 RTP 搜索辅助。

本模块提供了一个简单的蒙特卡洛估算器，用于计算给定符号权重的
5 转轮老虎机的玩家回报率（RTP）。
脚本还包含一个暴力搜索，用于查找其估计 RTP 接近目标（默认为0.96）的
权重配置。
"""

import random

# payout table: symbol -> {count: payout}
pay = {'A':{3:5,4:20,5:100},'K':{3:4,4:15,5:80},'Q':{3:3,4:10,5:60},'J':{3:2,4:8,5:40},'10':{3:1,4:5,5:20},'9':{3:1,4:3,5:15}}
# order of symbols corresponding to weights
SYMS=['A','K','Q','J','10','9']

def estimate(weights, trials=200000):
    """根据符号权重列表估算 RTP。

    权重列表的顺序必须与 SYMS 相同。每次试验都根据给定的离散分布
    随机选择 5 个符号（每个转轮一个），并累加任何三连或更多相同符号
    的支付。每次试验的平均支付近似于 RTP。

    :param weights: 用作每个符号相对概率的非负数序列。
    :param trials: 蒙特卡洛迭代的次数。
    :return: 估计的 RTP（浮点数）。
    """
    total=0
    for i in range(trials):
        reels=[]
        tot=sum(weights)
        # pick one symbol per reel
        for j in range(5):
            r=random.random()*tot
            for w,sym in zip(weights,SYMS):
                if r<w:
                    reels.append(sym)
                    break
                r-=w
        # count occurrences of each symbol
        counts={}
        for r in reels:
            counts[r]=counts.get(r,0)+1
        # add payouts for winning combinations
        for sym in SYMS:
            cnt=counts.get(sym,0)
            if cnt>=3:
                total+=pay[sym].get(cnt,0)
    return total/trials

# 简单搜索循环：随机生成权重向量，并保留产生 RTP 最接近 0.96
# （任意目标）的配置。此示例仅供说明，并非高效优化器。

best_diff=1
best_conf=None
for _ in range(5000):
    # 为每个符号生成 1 到 15 之间的随机权重
    ws=[random.randint(1,15) for __ in SYMS]
    rtp=estimate(ws,100000)
    diff=abs(rtp-0.96)
    if diff<best_diff:
        best_diff=diff
        best_conf=(ws,rtp)
print('best',best_conf,'diff',best_diff)
