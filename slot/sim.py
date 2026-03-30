"""简单的老虎机模拟器。

本模块定义了一组带权重和支付值的符号，然后执行蒙特卡洛模拟来估算 RTP。
"pick" 辅助函数根据权重列表随机选择符号。
"""

import random

# 使用元组编码的符号：(符号, 权重, 支付表)
symbols=[
    ('A',1,{3:5,4:20,5:100}),
    ('K',2,{3:4,4:15,5:80}),
    ('Q',2,{3:3,4:10,5:60}),
    ('J',3,{3:2,4:8,5:40}),
    ('10',3,{3:1,4:5,5:20}),
    ('9',3,{3:1,4:3,5:15})
]
# 为方便起见预先计算权重列表
weights=[s[1] for s in symbols]

def pick():
    """根据定义的权重随机选择一个符号。

    使用累积权重采样。返回符号字符串。
    """
    total=sum(weights)
    r=random.random()*total
    for s,w,p in symbols:
        if r<w:
            return s
        r-=w
    # 作为回退（通常不会发生，除非四舍五入误差）
    return symbols[-1][0]


def simulate(n=1000000):
    """运行 n 次旋转并返回每次旋转的平均支付（RTP 估计）。

    :param n: 模拟旋转次数
    :return: 平均中奖金额
    """
    total_win=0
    for i in range(n):
        reels=[pick() for _ in range(5)]
        counts={}
        for r in reels:
            counts[r]=counts.get(r,0)+1
        for s,w,p in symbols:
            cnt=counts.get(s,0)
            if cnt>=3:
                total_win += p.get(cnt,0)
    return total_win/n

if __name__ == '__main__':
    # 示例用法：运行两百万次旋转并打印 RTP
    print(simulate(2000000))
