# Jump King 的跳跃高度数值设计

<img src="https://www.nintendoworldreport.com/media/54231/4/1.jpg" alt="Jump King Review - Review - Nintendo World Report" style="zoom:25%;" /><img src="https://www.nintendoworldreport.com/media/54231/4/2.jpg" alt="Jump King Review - Review - Nintendo World Report" style="zoom:25%;" /><img src="https://media.pocketgamer.com/artwork/na-37208-1740064175/jump-king-screenshot-5_jpg_820.jpg" alt="Jump King review - &quot;Getting some serious vertical rage!&quot; | Pocket Gamer" style="zoom: 33%;" />

1 Jump King机制分析
2 跳跃物理模型
3 蓄力系统设计
4 跳跃高度曲线
5 平台高度设计
6 水平距离设计
7 难度控制
8 玩家容错设计

**Jump King 的核心体验：**

- 只有 **跳跃** 一个主要动作
- **高度完全由蓄力时间决定**
- **落点误差极其敏感**
- **失误会造成巨大回退**

因此它的数值设计重点是：

> **让玩家“可以精确控制跳跃高度”，但又“很难完全掌控”。**

## 1、基础跳跃物理模型

平台跳跃游戏一般使用 **抛物线运动模型**。

基础公式：
$$
x = v_xt\\
y = v_yt + \frac12gt^2
$$
其中：

| 参数 | 含义                   |
| ---- | ---------------------- |
| x    | x方向上的位移          |
| y    | y方向上的位移（高度）  |
| g    | 重力加速度（方向向下） |
| t    | 时间                   |
| v_x  | 速度在x方向上的分量    |
| v_y  | 速度在y方向上的分量    |



显然：

在跳跃过程中$v_x$保持不变，而$v_y$先减少后增加，方向相反。

所以，易得当$v_y$为0时，上升的高度达到最大值。

