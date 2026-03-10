# Jump King 的跳跃高度数值设计

<img src="https://www.nintendoworldreport.com/media/54231/4/1.jpg" alt="Jump King Review - Review - Nintendo World Report" style="zoom:25%;" /><img src="https://www.nintendoworldreport.com/media/54231/4/2.jpg" alt="Jump King Review - Review - Nintendo World Report" style="zoom:25%;" /><img src="https://media.pocketgamer.com/artwork/na-37208-1740064175/jump-king-screenshot-5_jpg_820.jpg" alt="Jump King review - &quot;Getting some serious vertical rage!&quot; | Pocket Gamer" style="zoom: 33%;" />

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



<img src="/home/yao/Documents/somethingshows/作品集关卡分析/Jump King 的跳跃高度数值设计/Figure_1.png" alt="Figure_1" style="zoom:25%;" />

显然：

在跳跃过程中$v_x$保持不变，而$v_y$先减少后增加，方向相反。

所以，易得当$v_y$为0时，上升的高度达到最大值。

此时：
$$
t = |\frac{v_y}g|\\
h = \frac{{v_y}^2}{2g}
$$

---

##### 示例设计

假设:
$$
g = -2000 {px/s^2}\\
v_y = 900 px/s 
$$
计算：
$$
h = 202px
$$
最大跳跃高度约 **200px**。

## 2、Jump King 核心机制：蓄力跳跃

Jump King 的关键设计是：

>跳跃速度 = 蓄力时间

 

设计公式：

~~~python
v_y = v_min + charge_ratio * (v_max - v_min)
~~~

其中

~~~python
charge_ratio = charge_time / max_charge_time
~~~



---

##### 示例数值

~~~python
v_min = 400
v_max = 900
max_charge_time = 0.8秒
~~~

蓄力结果：

| 蓄力时间 | 初速度 | 最大高度 |
| -------- | ------ | -------- |
| 0.2s     | 525    | 69px     |
| 0.4s     | 650    | 106px    |
| 0.6s     | 775    | 150px    |
| 0.8s     | 900    | 202px    |

这样玩家可以 **控制不同高度跳跃**。



![Figure_2](/home/yao/Documents/somethingshows/作品集关卡分析/Jump King 的跳跃高度数值设计/Figure_2.png)

## 3、平台高度设计

Jump King 的关卡是 **围绕跳跃高度设计的**。

一般规则：

~~~
平台高度 = 最大跳跃高度 × 0.7 ~ 0.9
~~~

例如：

最大跳跃高度：

~~~
200px
~~~

平台高度设计：

| 类型 | 高度  |
| ---- | ----- |
| 简单 | 120px |
| 普通 | 150px |
| 极限 | 180px |

这样：

- 新手能跳上去，但误差空间很小

## 4、Jump King 的“难度来源”

它不是靠高难度操作，而是 **误差惩罚设计**。

例如：

##### 1 失误掉落

平台间设计：

~~~
失败 = 掉回两层（甚至更多）
~~~

##### 2 起跳位置限制

~~~
平台宽度 < 跳跃距离
~~~

##### 3 空中不可调整

很多平台游戏允许空中控制：

~~~
空中移动速度
~~~

Jump King 基本 **不可调整**。

## 5、水平跳跃距离设计

水平距离公式：
$$
x = 2 v_x \cdot t_{total}\\
t =2 \frac{v_y}{g}
$$
假设：

~~~
vx = 200
vy = 900
g = 2000
~~~

~~~py
t_total = 0.9s
~~~

水平距离：

~~~
x = 200 × 0.9 ≈ 180px
~~~

## 6、Jump King 的隐藏数值设计

##### 1 跳跃容错

落地检测会稍微扩大：

~~~
平台碰撞体 > 视觉模型
~~~

提高成功率。

##### 2 输入延迟

跳跃释放会有：

~~~
0.02s delay
~~~

增加微妙难度。

---

##### 3 重力偏大

很多平台游戏：

~~~
g ≈ 1200
~~~

Jump King：

~~~
g ≈ 2000+
~~~

这样跳跃 **更干脆**。

## 7.进阶难度设计

Jumping king 后期的关卡中，难度的增加依靠的是更加复杂的地图设计（如撞墙反弹）、风力的阻碍（改变跳跃的速度）等。

递增的难度搭配上“一跳回到解放前”的失误风险，提升了主播直播的节目效果，更有利于游戏的宣传（faker最爱的小游戏）。

