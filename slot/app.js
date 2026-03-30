// 货币系统
let balance = 100; // 初始余额，可自行调整
const history = []; // 投注历史记录

function updateBalanceDisplay() {
    document.getElementById('balance').textContent = balance.toFixed(2);
}

function addHistoryEntry(bet, win) {
    const time = new Date().toLocaleTimeString();
    const entry = { time, bet, win, balance };
    history.push(entry);
    updateHistoryDisplay();
}

function updateHistoryDisplay() {
    const tbody = document.querySelector('#historyTable tbody');
    tbody.innerHTML = '';
    // 只展示最近5条记录，最新的在上方
    const entries = history.slice().reverse().slice(0, 5);
    entries.forEach(e => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${e.time}</td><td>${e.bet}</td><td>${e.win}</td><td>${e.balance.toFixed(2)}</td>`;
        tbody.appendChild(row);
    });
}

// 符号定义
const symbols = [
    { id: 'A', name: '魔法宝石', rarity: '高', weight: 1, pay: {3: 5, 4: 20, 5: 100} },
    { id: 'K', name: '金色戒指', rarity: '中', weight: 2, pay: {3: 4, 4: 15, 5: 80} },
    { id: 'Q', name: '魔法卷轴', rarity: '中', weight: 2, pay: {3: 3, 4: 10, 5: 60} },
    { id: 'J', name: '木质护符', rarity: '低', weight: 3, pay: {3: 2, 4: 8, 5: 40} },
    { id: '10', name: '普通符号', rarity: '低', weight: 3, pay: {3: 1, 4: 5, 5: 20} },
    { id: '9', name: '普通符号', rarity: '低', weight: 3, pay: {3: 1, 4: 3, 5: 15} }
];

/*
    符号权重  概率
    A	1	7.14%
    K	2	14.29%
    Q	2	14.29%
    J	3	21.43%
    10	3	21.43%
    9	3	21.43%
        14

    因为每次 5个独立抽取。
    某个符号出现 k 次 的概率：二项分布：
    P(k) = C(5,k) * p^k * (1-p)^(5-k)  k = 3,4,5

    奖励：
    组合	概率	奖励
    3A	0.00339	    5
    4A	0.00026	    20
    5A	0.000002	100
    E_A = 0.0224

    A   0.022
    K   0.117
    Q   0.085
    J   0.203
    10  0.109
    9   0.092
    ----------------
    Total ≈ 0.628   RTP ≈ 62.8%
 */ 

function pickSymbol() {   /***/
    // 根据权重随机选取一个符号
    const total = symbols.reduce((sum, s) => sum + s.weight, 0);
    let r = Math.random() * total;
    for (const s of symbols) {
        if (r < s.weight) return s;
        r -= s.weight;
    }
    return symbols[symbols.length - 1];
}

function spin() {
    // 获取当前押注
    const betInput = document.getElementById('betAmount');
    const bet = Math.max(0, parseFloat(betInput.value) || 0);
    if (bet <= 0) {
        document.getElementById('message').textContent = '请先输入押注金额';
        return;
    }

    if (balance < bet) {
        document.getElementById('message').textContent = '余额不足，请充值';
        return;
    }

    balance -= bet; // 扣除押注
    updateBalanceDisplay();

    const reels = [];
    for (let i = 0; i < 5; i++) {
        reels.push(pickSymbol());
    }

    // 更新界面
    reels.forEach((s, idx) => {
        document.getElementById('r' + idx).textContent = s.id;
    });

    // 计算胜利情况
    const counts = {};
    reels.forEach(s => counts[s.id] = (counts[s.id] || 0) + 1);
    let win = 0;
    let messages = [];
    for (const sym of symbols) {
        const cnt = counts[sym.id] || 0;
        if (cnt >= 3) {
            const payout = sym.pay[cnt] || 0;
            if (payout > 0) {
                win += payout * bet; // 乘以押注金额
                messages.push(`${cnt}个${sym.id} -> ${payout} x 押注`);
            }
        }
    }
    if (win > 0) {
        balance += win;
        updateBalanceDisplay();
    }
    const msg = win > 0 ? `本次赢得 ${win}：` + messages.join('，') : '未中奖';
    document.getElementById('message').textContent = msg;

    // 记录本次投注历史
    addHistoryEntry(bet, win);
}

document.getElementById('spinBtn').addEventListener('click', spin);
// 充值按钮
const addBtn = document.getElementById('addMoneyBtn');
if (addBtn) {
    addBtn.addEventListener('click', () => {
        balance += 100;
        updateBalanceDisplay();
        document.getElementById('message').textContent = '已充值 100 元';
    });
}

// 页面加载时显示初始余额
updateBalanceDisplay();


// 简单的 RTP 估算（可在控制台运行）
function estimateRTP(trials = 1000000) {
    let total = 0;
    for (let i = 0; i < trials; i++) {
        const reels = [];
        for (let j = 0; j < 5; j++) reels.push(pickSymbol());
        const counts = {};
        reels.forEach(s => counts[s.id] = (counts[s.id] || 0) + 1);
        for (const sym of symbols) {
            const cnt = counts[sym.id] || 0;
            if (cnt >= 3) total += (sym.pay[cnt] || 0);
        }
    }
    console.log('估算RTP:', (total / trials * 100).toFixed(2) + '%');
}

// 如果你想了解这个配置大约的RTP，可以在控制台输入 estimateRTP();
// 输出类似 “估算RTP: 63.05%”
