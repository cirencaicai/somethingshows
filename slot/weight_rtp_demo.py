"""演示使用不同权重集合的 RTP 估计器。

本脚本重复使用 estimate() 函数（从 search_weights.py 复制），
并为几个预定义的权重配置打印 RTP 估计，以展示符号频率如何
影响回报。
"""

import random

# 示例共享的支付表
pay = {'A':{3:5,4:20,5:100},'K':{3:4,4:15,5:80},'Q':{3:3,4:10,5:60},'J':{3:2,4:8,5:40},'10':{3:1,4:5,5:20},'9':{3:1,4:3,5:15}}
SYMS=['A','K','Q','J','10','9']

def estimate(weights, trials=200000):
    """返回给定权重向量的 RTP 估计。

    详细信息见 search_weights.py 中的文档。
    """
    total=0
    for i in range(trials):
        reels=[]
        tot=sum(weights)
        for j in range(5):
            r=random.random()*tot
            for w,sym in zip(weights,SYMS):
                if r<w:
                    reels.append(sym)
                    break
                r-=w
        counts={}
        for r in reels: counts[r]=counts.get(r,0)+1
        for sym in SYMS:
            cnt=counts.get(sym,0)
            if cnt>=3:
                total+=pay[sym].get(cnt,0)
    return total/trials

if __name__ == '__main__':
    # 比较三种示例权重配置的 RTP
    base=[1,2,2,3,3,3]
    print('base', base, estimate(base))
    rarer=[0.5,2,2,3,3,3]  # 使符号 A 更少出现
    print('A rarer', rarer, estimate(rarer))
    common=[2,2,2,3,3,3]  # 使符号 A 更常见
    print('A common', common, estimate(common))
