#!/usr/bin/env python3
# 语义手册（Semantic Atlas）生成器 —— 大白话版，HTML 直进 GitHub
import json, html, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'site')
os.makedirs(os.path.join(OUT, 'repos'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'ch'), exist_ok=True)
inv = json.load(open(os.path.join(HERE, 'inventory.json')))
GH = 'https://github.com/xf8410'
BASE = 'https://xf8410.github.io/repo-atlas'  # GitHub Pages 绝对路径
TODAY = datetime.date.today().isoformat()

# ---------- 仓库分组与大白话介绍 ----------
GROUPS = [
    ("🐴 赛马娘 AI 核心（这次修的就是这条线）", [
        ("umaai-rs", "主仓库（Rust 重写的育成 AI）。所有实验的老家，上游是 xulai1001 的原版。MCTS 搜索、评分、策略都在这里。"),
        ("umaai-rs-fanfix", "本次修复实验仓。『拉面杯溢出/松弛修复』的主战场：补丁（patches/）、九臂 A/B 测试（bench）、判词（docs/）都在这。语义手册住在专门的 repo-atlas 仓库（总入口有链接）。"),
        ("umaai-rs-fanskip", "粉丝数跳过版：真机 AI 可以配置跳过『粉丝数达标』判定。注意：主人最新判断是粉丝数可能根本不用管（每个马娘都有必打的育成目标赛），待实测。"),
        ("uma-ramen-nn-lab", "神经网络实验室（EXP-001~009）：MCTS+神经网络决策器迭代的主场。EXP-009b 冠军 66734.8 分（注意：未经跨世界线复验）。"),
        ("uma-ramen-nn-lab-exp010", "EXP-010 自蒸馏：让神经网络当搜索引擎的评估器。跑完归档回主仓。"),
        ("uma-ramen-teacher-lab", "教师实验仓（EXP-013 起）：先修好『教师』再蒸馏给学生。这是论文（DAgger）指出的正路。"),
        ("uma-train", "AI 训练框架：MCTS+神经网络，剧本机制隔离，拉面杯模拟器已按 MDB/实机截图校准。"),
        ("uma-data", "训练数据集仓库：MCTS 策略+比赛模拟器价值评估数据。里面有完整 master.mdb（41MB 游戏数据表）和逆向资料。"),
    ]),
    ("📖 机制与知识库", [
        ("umamusume-scenario-mechanics", "赛马娘全育成剧本的机制说明书：协议接口、响应结构、MDB 与运行时证据。泳装青云天空的公式闭环交接书就在这里的分支里。"),
        ("umamusume-mechanics-archive", "机制私人规范化归档：审计账本、迁移记录。『2798 个悬空 blob 没提交』的教训就记在这。"),
        ("uma-wiki", "赛马娘育成 Wiki：机制条目与攻略整理，带 CI 校验。"),
        ("ramen-manual", "拉面杯规则手册：玩法机制、流程与规则的中文整理存档。第一次玩拉面杯先看这个。"),
        ("uma-kouryaku-tools-mirror", "攻略站全量镜像：140 条赛道的分段/坡道/相位 + 317 场赛事数据。"),
        ("uma-saidao-shuju", "赛道数据挖掘：140 赛道静态表、天气马场、技能条件、末脚/焦躁/封堵机制。"),
        ("uma-zmyz", "种马因子数据集：育成继承链路的结构化因子库。"),
    ]),
    ("🔧 Hachimi 框架与插件（注入/观测层）", [
        ("hlpatch", "育成内存读取插件：基于 Hachimi 框架，从游戏内存实时读数据+HTTP 端点+自动推送。分支最多（52 个），全是各阶段功能开发记录。"),
        ("hlpatch-observation-architecture", "观测数据归档仓：泳装青云天空 465 协议交换会话的索引在这。⚠️ 原始载荷（2798 文件）当年只建了 blob 没提交，已被 GitHub 回收，源文件还在手机上。"),
        ("Hachimi-Edge", "Hachimi-Edge 上游 fork（kairusds）：资源注入框架增强分支的基座。"),
        ("hachimi-edge-gala", "Hachimi-Edge 的 BestSoccer 改造版：给足球游戏做资源替换注入。"),
        ("hachimi-template-gala", "Hachimi mod 模板：BestSoccer 资源替换 mod 的开发模板。"),
        ("uma-patcher-gala", "UmaPatcher-Edge 改造版：BestSoccer 的运行时补丁器。"),
        ("umahachimios", "UmachimiOS 安装器插件：Hachimi 系安装器辅助。"),
        ("uma-landscape", "强制横屏 Zygisk 模块：引擎级朝向 hook。"),
        ("uma-liuchang-hachimiso", "卡顿诊断插件：帧率/卡顿采样分析。"),
        ("cygames-hachimi-tl-zh-cn", "Cygames Hachimi 的中文翻译仓库（含泳装青云剧情翻译）。"),
    ]),
    ("📱 手机端应用", [
        ("uma-juece", "育成辅助浮窗：Android 悬浮窗实时显示属性/训练增益/Buff/AI 决策推荐。"),
        ("uma-juece-ramen", "拉面杯专用决策浮窗：基于 uma-juece，机制对齐上游。34 个分支全是迭代记录。"),
        ("ramen-scenario-analyzer-mobile", "拉面杯纯状态分析器（Android）：素材/盛況度/支援卡显示，纯展示不决策。"),
        ("ramen-training-advisor", "拉面杯训练决策器：手写逻辑移植+动态权重（Kotlin）。"),
        ("uma-ai-assistant", "赛马娘 AI 助手：悬浮窗仪表盘+截图 OCR。"),
        ("uma-mobile-decision-pipeline", "手机端采集流水线：Session 同步+MessagePack 解码+上传决策链路。"),
        ("uma-container", "Android 容器化运行研究：把游戏嵌进宿主 App 同屏运行（实验性，有账号风险）。"),
        ("Agora-Workbench", "安卓 AI 工作台：多模型对话/工具调用/GitHub 全套工具。分支最多（125 个），每个分支一个修复或功能。"),
        ("uma-workbench", "繁体/简体中文 AI 开发研究与数据分析桌面工作台（Android 端）。"),
    ]),
    ("⚽ 最佳球会（BestSoccer）", [
        ("football-game", "足球游戏 Godot 4 原型：BestSoccer 玩法原型场。"),
        ("football-game-kotlin", "足球游戏 Kotlin+LibGDX 移植版：玩法验证场，22 个开发分支。"),
        ("duel-links-lite", "决斗链接离线学习伴侣：卡牌查库/组合检索本地化工具。"),
    ]),
    ("🗄️ 其他", [
        ("ranko-love-archive", "ranko.love 站点数据归档：非赛马娘项目的资料收藏仓。"),
    ]),
]
REPO2GROUP = {}
for g, items in GROUPS:
    for name, _ in items:
        REPO2GROUP[name] = g

# ---------- 语义章节 ----------
CHAPTERS = [
    ("player", "👤 玩家语义", "第一次玩这个游戏的人，先从这里开始"),
    ("game", "🎮 游戏语义", "拉面杯这个剧本到底在玩什么"),
    ("code", "🛠️ 代码维护语义", "仓库地图 + 分支规矩 + 怎么改代码"),
    ("fix", "🩹 修复语义", "补丁、A/B 测试、判词、转正——修东西的黑话全解"),
    ("compat", "🔗 兼容性语义", "怎么保证新改动不弄坏旧东西"),
    ("bugfix", "🐛 修 Bug 维护语义", "复现、种子、世界线——抓虫子的纪律"),
    ("pr", "📬 PR 语义", "提交代码前必须懂的规矩（含世界线教训）"),
    ("glossary", "📖 术语白话对照表", "看到看不懂的词，来这里查"),
]

def esc(s): return html.escape(str(s))

CSS = """
:root{--bg:#0f1419;--card:#1a2129;--card2:#212a35;--line:#2d3743;--txt:#e6e9ed;--sub:#9aa7b4;
--acc:#5eb1ff;--acc2:#ffd166;--ok:#4ade80;--bad:#f87171;--warn:#fbbf24;--hold:#a78bfa}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.75;font-size:16px}
.wrap{max-width:1080px;margin:0 auto;padding:24px 20px 80px}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
h1{font-size:1.9em;margin:12px 0 6px}h2{font-size:1.35em;margin:34px 0 12px;border-left:4px solid var(--acc);padding-left:10px}
h3{font-size:1.12em;margin:22px 0 8px;color:var(--acc2)}
p{margin:8px 0}ul,ol{margin:8px 0 8px 24px}li{margin:5px 0}
.nav{position:sticky;top:0;z-index:9;background:rgba(15,20,25,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:10px 20px;display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.92em}
.nav b{color:var(--acc2)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:12px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}
.repo-card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;transition:transform .12s}
.repo-card:hover{transform:translateY(-2px);border-color:var(--acc)}
.repo-card .name{font-weight:700;font-size:1.05em}
.repo-card .desc{color:var(--sub);font-size:.9em;margin:6px 0}
.tag{display:inline-block;padding:1px 9px;border-radius:20px;font-size:.78em;margin-right:5px;border:1px solid var(--line);color:var(--sub)}
.tag.hot{color:var(--acc2);border-color:var(--acc2)}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:.93em}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--card2)}
tr:nth-child(even){background:rgba(255,255,255,.02)}
.ok{color:var(--ok)}.bad{color:var(--bad)}.warn{color:var(--warn)}.hold{color:var(--hold)}
.callout{border-left:4px solid var(--warn);background:rgba(251,191,36,.07);padding:10px 14px;border-radius:0 8px 8px 0;margin:12px 0}
.callout.danger{border-color:var(--bad);background:rgba(248,113,113,.07)}
.callout.info{border-color:var(--acc);background:rgba(94,177,255,.07)}
.big-num{font-size:2em;font-weight:800;color:var(--acc2)}
footer{margin-top:60px;color:var(--sub);font-size:.85em;border-top:1px solid var(--line);padding-top:16px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.chip{background:var(--card2);border:1px solid var(--line);border-radius:8px;padding:6px 12px;font-size:.9em}
br-table{display:block;overflow-x:auto}
@media print{.nav{position:static}body{background:#fff;color:#000}}
"""

def head(title, crumbs=''):
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} · 花落仓库语义手册</title>
<style>{CSS}</style></head><body>
<div class="nav"><b>语义手册</b> <a href="../index.html">🏠 总入口</a> {' '.join(f'<a href="ch/{c}.html">{t}</a>' for c, t, _ in CHAPTERS)} <a href="../index.html#repos">📦 仓库地图</a></div>
<div class="wrap">{crumbs}"""

FOOT = f"""<footer>花落仓库语义手册 · 生成于 {TODAY} · 全部页面互相跳转，直接存放在 GitHub 仓库内，免积分查看。<br>
维护方法：改 <code>semantic_atlas/gen_atlas.py</code> 里的文字，重新运行生成，推送到 repo-atlas 仓库。</footer>
</div></body></html>"""

def page(fname, content):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

# ---------- 总入口 ----------
repo_cards = []
for gname, items in GROUPS:
    repo_cards.append(f'<h2>{esc(gname)}</h2><div class="grid">')
    for name, blurb in items:
        info = inv.get(name, {})
        nb = len(info.get('branches', []))
        sz = info.get('size_kb', 0) // 1024
        hot = ' hot' if name in ('umaai-rs-fanfix', 'uma-ramen-nn-lab', 'hlpatch') else ''
        repo_cards.append(f"""<div class="repo-card"><div class="name"><a href="repos/{name}.html">{esc(name)}</a></div>
<div class="desc">{esc(blurb)}</div>
<span class="tag{hot}">{nb} 个分支</span><span class="tag">{sz}MB</span><span class="tag"><a href="{GH}/{name}" target="_blank" rel="noopener noreferrer">GitHub ↗</a></span></div>""")
    repo_cards.append('</div>')

TOTAL_BRANCHES = sum(len(v['branches']) for v in inv.values())
idx = head('总入口') + f"""
<h1>🏠 花落仓库语义手册</h1>
<p style="color:var(--sub)">这是全部 {len(inv)} 个仓库、{sum(len(v['branches']) for v in inv.values())} 个分支的大白话说明书。<b>不写术语，只讲语义</b>——第一次玩赛马娘、第一次看代码的人也能读懂。</p>

<div class="callout info"><b>怎么用这本手册：</b>① 先读下面前两个语义章节（玩家/游戏），搞懂游戏在玩什么；② 要改代码就读「代码维护语义」；③ 修 bug / 提 PR 前先读对应章节——里面记着踩过的坑（包括 2798 个文件丢失的教训）。每个仓库点卡片进去，能看到每个分支是干嘛的。</div>

<div class="chips">
<div class="chip">📦 <span class="big-num">38</span> 个仓库</div>
<div class="chip">🌿 <span class="big-num">{sum(len(v['branches']) for v in inv.values())}</span> 个分支</div>
<div class="chip">📅 盘点日期 {TODAY}</div>
</div>

<h2>📚 先读语义（按顺序）</h2>
<div class="grid">
{''.join(f'<div class="repo-card"><div class="name"><a href="ch/{c}.html">{esc(t)}</a></div><div class="desc">{esc(d)}</div></div>' for c, t, d in CHAPTERS)}
</div>

<h2 id="repos">📦 仓库地图</h2>
{''.join(repo_cards)}

<h2>⚠️ 三条必须记住的教训</h2>
<div class="card"><ol>
<li><b class="bad">上传文件必须提交进分支。</b>泳装青云天空的 2798 个原始抓包文件只传了 blob 没提交，被 GitHub 回收，永久丢失。教训记在「修 Bug 语义」。</li>
<li><b class="bad">不同口径的分数不能互相比。</b>64271（REC 直跑）、66734.8（EXP-009b 冠军）、72000/76000（神经网络迭代、数据在暮雪流年的电脑）是三把不同的尺子。</li>
<li><b class="bad">冠军必须换种子复验。</b>EXP-009 把同时期最优结论落地、砍掉不良结论，等于在不同世界线之间挑樱桃——那个"最优"可能只是运气。详见「PR 语义」。</li>
</ol></div>
""" + FOOT
page(os.path.join(OUT, 'index.html'), idx)
print('index.html done')

# ---------- 术语表 ----------
GLOSSARY = [
    ("育成", "陪一个马娘从入学训练到毕业比赛的全过程。玩一局=育成一次。"),
    ("马娘", "游戏里的角色，每个都是要培养的赛马拟人少女。"),
    ("支援卡", "育成时带的辅助卡牌，相当于请来的教练团，影响训练效果。"),
    ("拉面杯（Scenario 14）", "游戏里的一个特定剧本/玩法，代号 14。这局育成要在做拉面、试吃、打卡点之间安排训练。我们现在修的就是这个剧本的 AI。"),
    ("回合", "游戏的基本节拍。每回合你要选一件事：训练、外出、休息、或者去比赛。"),
    ("五维属性", "马娘的五项能力值（速度/耐力/力量/毅力/智力）。训练就是涨这些数。"),
    ("属性上限（status cap）", "每项属性有个天花板（five_status_limit）。练超过天花板的数值，游戏不记账——这就是'溢出'，我们修的病灶之一。"),
    ("PT（料理点）", "拉面杯里攒的一种点数。游戏里真实价值约 1 点=2 分。注意代码里的 pt_rate=16/64 是人为抬高的'报价'，不是真实价。"),
    ("守门值（reserve，40）", "AI 给自己留的体力缓冲线，红线，谁都不许动。"),
    ("MCTS", "蒙特卡洛树搜索——AI 提前在脑子里模拟很多种走法、挑最好的一种。可以理解为'脑内彩排'。"),
    ("神经网络（NN）", "用大量对局数据训练出来的评分大脑。MCTS 负责想，NN 负责打分。"),
    ("教师/学生", "蒸馏的说法：先有一个厉害但慢的'教师'，再把教师的判断教给快但笨的'学生'。论文说：教师有病，学生必歪——所以要先修教师。"),
    ("种子（seed）", "随机数的起点。同一个种子=同一条世界线，所有随机事件完全重放。"),
    ("世界线", "一局游戏从头到尾的随机事件序列。换种子=换世界线。"),
    ("A/B 测试（bench）", "把两个版本的 AI 用同一批种子各跑 N 局，比总分。一次只改一个变量，才知道是谁的功劳。"),
    ("臂（arm）", "A/B 测试里的一个参赛版本。九臂=九个版本同场比。"),
    ("补丁（patch）", "一小段改动文件，默认不生效（关着）。想试就开对应的 token 开关。这样主代码永远干净。"),
    ("token", "开补丁的钥匙。比如 rclamp、slack20。带 token 跑=开对应补丁。"),
    ("判词", "A/B 测试后的官方结论：转正（采纳）/中性（没影响）/判死（此路不通，不翻案）/留观（再看）。"),
    ("转正", "补丁经过考验，正式合并进主线代码。"),
    ("留观", "有一点点希望但不够，先放着，下次再测。"),
    ("REC 直跑", "不做搜索、直接按策略跑一局，用来快速打分。分数比完整 MCTS 低，是正常的。"),
    ("口径", "分数的测量方式。口径不同，分数不能互相比。就像米和尺，数字不一样不代表东西变长变短。"),
    ("悬空 blob", "传到 GitHub 但没有被任何分支引用的文件。约两周后会被 GitHub 自动清掉。2798 个抓包文件就是这样没的。"),
    ("上游（upstream）", "我们的代码是从别人的仓库复制改造来的，那个原仓库叫上游（xulai1001/umaai-rs）。"),
    ("fork", "把别人的仓库复制一份到自己名下改造。"),
    ("main/master", "仓库的主干分支=正式版本。workbench/* 开头的分支都是实验工作台。"),
    ("CI", "自动质检机器人。每次推代码，它自动编译+跑测试，绿=过，红=有问题。"),
    ("cherry-pick（挑樱桃）", "从一堆结果里只挑好看的。在实验里这是作弊——会得出虚假的'最优'。"),
    ("粉丝数", "育成中积累的粉丝量。原版游戏里是某些条件，但每个马娘都有必打的育成目标赛，所以粉丝数可能不用管（待实测）。"),
    ("暮雪流年", "另一台电脑的名字。72000/76000 分的神经网络迭代数据在那台电脑上，目前拿不到。"),
]
g = head('术语白话对照表', '<p><a href="../index.html">← 回总入口</a></p>') + "<h1>📖 术语白话对照表</h1><p>按出现频率排序。看到不懂的词，Ctrl+F 搜它。</p><table><tr><th style='width:180px'>术语</th><th>白话解释</th></tr>"
for t, d in GLOSSARY:
    g += f"<tr><td><b>{esc(t)}</b></td><td>{esc(d)}</td></tr>"
g += "</table>" + FOOT
page(os.path.join(OUT, 'ch', 'glossary.html'), g)
print('glossary done')

# ---------- 语义章节正文 ----------
CH_PLAYER = """
<h1>👤 玩家语义</h1>
<p style="color:var(--sub)">第一次玩这个游戏的人，先从这里开始。全部大白话。</p>

<h2>你在玩什么</h2>
<div class="card">
<p>你是一名 <b>训练员</b>。你的工作：把一个刚入学的马娘（赛马拟人少女），花大约 78 个回合（游戏里叫"三年"），训练成能赢比赛的选手。</p>
<p>每个回合你只能选 <b>一件事</b> 做：</p>
<ul>
<li>🏋️ <b>训练</b>——涨属性（速度/耐力/力量/毅力/智力），但消耗体力</li>
<li>🚶 <b>外出</b>——恢复心情</li>
<li>😴 <b>休息</b>——恢复体力</li>
<li>🏇 <b>比赛</b>——去打比赛，有的比赛是必须打的（育成目标赛）</li>
</ul>
<p>毕业时按属性和比赛成绩算一个总分，分越高越好。</p>
</div>

<h2>支援卡是什么</h2>
<div class="card"><p>育成开始前你要带 6 张支援卡，相当于请了一个教练团。训练时支援卡会出现在训练场上，和她们一起练收益更高。带谁、怎么练，是策略的一部分。</p></div>

<h2>粉丝数要不要管</h2>
<div class="callout info"><b>最新结论（2026-09-13，主人定）：</b>粉丝数<b>可能不需要管</b>。因为每个马娘都有自己的育成目标比赛，是必须要打的——该打的比赛一场都少不了，粉丝自然够。有个仓库（umaai-rs-fanskip）专门做"跳过粉丝数判定"，还有个仓库（umaai-rs-fanfix）最初就是修粉丝数达标判定的。<b>但这条结论还要实测确认。</b></div>

<h2>AI 在里面干什么</h2>
<div class="card">
<p>我们做的就是替你选"每回合干哪件事"的 AI。它的决策链是：</p>
<ol>
<li><b>看局面</b>：体力多少、属性多少、离上限还有多远、下回合有什么比赛</li>
<li><b>脑内彩排</b>（MCTS 搜索）：把几种走法往后模拟几步</li>
<li><b>打分</b>：给每种走法算一个分数</li>
<li><b>选最高分</b> 的那个动作执行</li>
</ol>
<p>现在修的病灶就在第 3 步打分：以前给"练到上限之外"的动作算高了分（游戏其实不记账），给休息的定价也有些错位。</p>
</div>

<h2>一个值得注意的信号</h2>
<div class="callout"><b>主人观察（待实测）：</b>如果 AI 在某个回合自选了比赛，可能说明当前回合的训练选项确实非常垃圾，AI 才去"逃"进比赛。这个行为可以当诊断信号用，但要实际测试验证。</div>
"""

CH_GAME = """
<h1>🎮 游戏语义</h1>
<p style="color:var(--sub)">拉面杯这个剧本到底在玩什么，以及分数是怎么算的。</p>

<h2>拉面杯（Scenario 14）</h2>
<div class="card">
<p>赛马娘有很多育成剧本，拉面杯是第 14 号剧本。特点：除了常规训练，还要 <b>做拉面</b>。</p>
<ul>
<li>🍜 做拉面会攒 <b>料理点（PT）</b>，还能提升"盛況度"</li>
<li>👅 定期有 <b>试吃</b> 检查点，达标给奖励</li>
<li>📍 训练场地上有 <b>打卡点（checkpoint）</b>，凑齐给被动加成</li>
</ul>
<p>所以每回合的选择题比普通剧本多一层：不光练什么，还要不要分心做拉面。</p>
</div>

<h2>分数是怎么算出来的</h2>
<div class="card">
<p>育成结束时的总分，大头来自五维属性。规则（从 1200 段真实数据里量出来的）：</p>
<ul>
<li><b>1 点属性 ≈ 3 分</b>（1200 分段的换算率）</li>
<li><b>1 点 PT 真实价值 ≈ 2 分</b></li>
<li>比赛名次、技能等另加一点</li>
</ul>
<p>我们的 bench（测试场）目前基准线：A 组平均分 <b>64271</b>。</p>
</div>

<h2>三个容易搞混的数字（口径陷阱）</h2>
<table>
<tr><th>数字</th><th>什么口径</th><th>在哪</th></tr>
<tr><td><b>~64271</b></td><td>bench REC 直跑（不做搜索，直接按策略跑），种子 61444，每臂 10 局</td><td>umaai-rs-fanfix 的 CI</td></tr>
<tr><td><b>66734.8</b></td><td>EXP-009b 冠军（神经网络迭代出来的最优模型，<span class="warn">未经换种子复验</span>）</td><td>uma-ramen-nn-lab</td></tr>
<tr><td><b>72000 / 76000</b></td><td>神经网络深度迭代的最好成绩，口径不明（可能是完整 MCTS 或不同 build）</td><td>在暮雪流年的电脑里，<span class="bad">拿不到</span></td></tr>
</table>
<div class="callout danger"><b>铁律：不同口径的分数不能互相比。</b>就像米和尺，数字不同不代表东西变了。讨论"提升"之前，先问"同一把尺吗"。</div>

<h2>属性上限与溢出</h2>
<div class="card">
<p>每项属性有天花板（比如 1200）。练到天花板之后，<b>再练的部分游戏不记账</b>——练了白练，还花了体力和回合。</p>
<p>以前的 AI 打分时没把这算清楚，给"练过头"的动作虚高的分，这就是"溢出"病灶。补丁 0008（slack20）试的就是：让 AI 在"选择层"把天花板看得松一点，但游戏记账照旧诚实。</p>
</div>

<h2>体力、守门与休息</h2>
<div class="card">
<ul>
<li>训练消耗体力，体力低了训练效果差、还可能失败</li>
<li><b>守门值 40</b>：AI 给自己留的体力缓冲底线。<span class="bad">红线，不许动</span></li>
<li>休息的价值 = 基础恢复 + 体力缺口换算。v10 判词发现：一局里平均休息 4.1 次，其中 1.8 次归守门管、2.3 次归匿名层管、<b>打分层只管 0.01 次</b>——所以改打分层的休息定价基本没用，作用域错位了</li>
</ul>
</div>
"""

CH_CODE = """
<h1>🛠️ 代码维护语义</h1>
<p style="color:var(--sub)">仓库地图、分支规矩、改代码的动线。零经验也能照着做。</p>

<h2>30 秒看懂仓库地图</h2>
<div class="card">
<p>38 个仓库分成五片：<b>赛马娘 AI 核心</b>（修的就是这条线）、<b>机制知识库</b>、<b>Hachimi 插件层</b>（从游戏内存读数据）、<b>手机应用</b>、<b>最佳球会</b>。详细卡片在 <a href="../index.html#repos">总入口</a>。</p>
<p>最重要的一句：<b>umaai-rs 是主仓，umaai-rs-fanfix 是本次修复实验仓</b>，本手册就住在 fanfix 里。</p>
</div>

<h2>分支命名规矩</h2>
<table>
<tr><th>分支名</th><th>意思</th></tr>
<tr><td><b>main / master</b></td><td>主干 = 这个仓库的正式版本。main 和 master 意思一样，只是仓库建的时期不同</td></tr>
<tr><td><b>workbench/xxx</b></td><td>工作台实验分支。一个分支一件事，名字里写着干嘛的（比如 workbench/slack-fix-v2 = 溢出松弛修复第二版）</td></tr>
<tr><td><b>backup/xxx</b></td><td>备份快照，别在上面改东西</td></tr>
<tr><td><b>release/xxx、publish/xxx</b></td><td>发布用分支</td></tr>
</table>

<h2>改代码的标准动线（补丁流）</h2>
<div class="card">
<ol>
<li>从主干拉一个 workbench 分支</li>
<li>改动写成 <b>补丁文件</b>（patches/000X-名字.patch），<b>默认不生效</b>——想试的时候用 token 打开</li>
<li>推上去，CI（自动质检机器人）自动跑编译+测试</li>
<li>bench（A/B 测试）里加一个"臂"，和基准同种子对跑</li>
<li>出判词：转正 / 中性 / 判死 / 留观</li>
</ol>
<p><b>为什么这样：</b>主干永远干净，每个改动自带开关和证据，随时可退。这叫"补丁即证据单元"。</p>
</div>

<h2>CI 是什么，红了怎么办</h2>
<div class="card">
<p>CI = GitHub Actions 自动质检。每次推代码它自动：编译 → 跑测试 → 跑 bench。<b>绿=过，红=有问题。</b></p>
<p><span class="bad">铁律：推送后必查 CI，红了必须修到绿再交付。</span></p>
<p>已知例外：libtests 有 4 个上游基线红（上游本来就红，我们不背不藏，写在明处）。</p>
</div>

<h2>动手前检查清单</h2>
<ul>
<li>☐ 这个仓库是赛马娘相关仓库吗？是的话，<b>先问主人要不要动</b>（有许可规则）</li>
<li>☐ 改动是不是默认关闭、不影响现有行为？</li>
<li>☐ 有没有引入魔法数字（没出处的裸数字）？有就消灭或标来源</li>
<li>☐ 提交信息写清楚改了什么、为什么</li>
</ul>
"""

CH_FIX = """
<h1>🩹 修复语义</h1>
<p style="color:var(--sub)">补丁、臂、判词、转正——修东西的黑话全解，附刚出炉的 v10 判词。</p>

<h2>一次修复的完整生命周期</h2>
<div class="card">
<p><b>发现症状 → 定位病灶 → 写补丁（默认关）→ bench 加臂 → 同种子 A/B → 出判词 → 转正或放弃</b></p>
<p>关键词解释：</p>
<ul>
<li><b>补丁</b>：一小段改动文件。平时关着，主代码逐位不变；带 token 跑才生效</li>
<li><b>臂</b>：bench 里的一个参赛版本。一次改一个变量，才知道分数变化归谁</li>
<li><b>判词</b>：测试后的官方结论，写进 docs/，<b>判死不翻案</b></li>
<li><b>转正</b>：补丁合入主线（走 0005 式流程）</li>
<li><b>留观</b>：有微弱信号，记下来下次再测</li>
</ul>
</div>

<h2>现有补丁家谱</h2>
<table>
<tr><th>补丁</th><th>干什么</th><th>判词</th></tr>
<tr><td>0001 rclamp</td><td>体力储备惩罚的增益钳制</td><td class="ok">已转正（成为 0005）</td></tr>
<tr><td>0002</td><td>早期实验</td><td class="warn">未进链</td></tr>
<tr><td>0003 vcurve</td><td>体力价值曲线软化</td><td class="bad">判死：亏损不来自降到几，而来自软化本身（保护性先验，不翻案）</td></tr>
<tr><td>0004 rera</td><td>储备分年代系数</td><td class="hold">中性（零翻转）</td></tr>
<tr><td>0006 capf25</td><td>上限折扣地板</td><td class="hold">噪声内偏负，无信号</td></tr>
<tr><td>0007 restdamp</td><td>休息按年份衰减</td><td class="hold">零翻转——打分层休息定价作用域错位</td></tr>
<tr><td>0008 slack20</td><td>选择层上限放宽 20（记账仍诚实）</td><td class="ok">唯一非负+弱信号（+4.4 分），留观 slack40</td></tr>
</table>

<h2>v10 九臂判词（2026-09-13 刚出）</h2>
<table>
<tr><th>臂</th><th>均分</th><th>对比 A</th><th>一句话</th></tr>
<tr><td>A-preset(转正)</td><td>64271.5</td><td>—</td><td>基准</td></tr>
<tr><td>B-rclamp</td><td>64271.5</td><td>0</td><td>和 A 逐位相同（转正自检通过）</td></tr>
<tr><td>C-vcurve / D-both / E-vcurve30</td><td>~64060</td><td class="bad">−0.32%~−0.34%</td><td>判死维持，不翻案</td></tr>
<tr><td>F-rera</td><td>64271.5</td><td>0</td><td>零翻转，中性</td></tr>
<tr><td>G-capf25</td><td>64212.7</td><td class="bad">−0.09%</td><td>噪声带内，无信号</td></tr>
<tr><td>H-restdamp</td><td>64271.5</td><td>0</td><td>零翻转（打分层休息仅 0.01 次/局）</td></tr>
<tr><td>I-slack20</td><td>64275.9</td><td class="ok">+0.007%</td><td>唯一非负，留观</td></tr>
</table>
<div class="callout info"><b>总判词（范围要圈准）：</b>v10 只证明——在"现在这套看得见的项目"里，单点调参拧到头了（纯错误修完，剩余旋钮边际收益趋零）。<b>它不证明手写路线枯竭。</b>下一步增量两条腿：①蒸馏与搜索侧（教师先行，见 uma-ramen-teacher-lab）②手写侧特征扩展（见下节路线图）。</div>

<h2>为什么"方向错了还有提升"</h2>
<div class="card">
<p>提升有两种：<b>止损型</b>（填坑，方向无关）和 <b>开疆型</b>（找到更好的走法，方向有关）。</p>
<p>之前的提升全是止损型：悬崖双重收费每次罚 1149 分，修掉它任何方向都涨。v10 判词证明：在现在这套看得见的项目里，开疆型的旋钮没有了（四个臂零变化）。</p>
</div>

<h2>手写 7 万路线图：缺的是功能，不是调参（2026-09-13 定）</h2>
<div class="card">
<p><b>锚点事实：人类玩家能打到 7 万。</b>这证明上限不在游戏机制——同一把牌人能打出 7 万，我们打 6.4 万，差距通常不是"旋钮不够细"，而是"人看得见的一些东西，我们的评分层看不见或不会表示"。</p>
<p><b>路线 = 扩可见面</b>：把人打牌时盯的东西列成清单，逐项对照评分层，缺一项补一项：</p>
<ul>
<li>训练等级门槛（几级训练才值得点）</li>
<li>体力红线与休息时机（不是休息定价，是何时必须休）</li>
<li>支援卡羁绊触发时机（绊满前该站哪格）</li>
<li>事件窗口（连续事件链的取舍）</li>
<li>失败率管理（高风险训练的期望值）</li>
<li>PT 换分效率（点数花在哪最值）</li>
<li>粉丝数——按实测前提划掉（每个马娘有必打目标赛，粉丝数可能不用管，待实测确认）</li>
</ul>
<p><b>纪律：</b>每补一项做成新特征+新 token，默认关，同种子进 bench 配对验——用防骗三规管着，不许拿单世界线的运气当结论。</p>
<p><b>证据链：</b>72000/76000 两个数字的记录正在全量历史 CI 里打捞。捞到就能还原当时的分支/配置，和现在的 64271 做同世界线 diff——把"人能达到"变成可定位的差距清单。</p>
</div>
"""

CH_COMPAT = """
<h1>🔗 兼容性语义</h1>
<p style="color:var(--sub)">怎么保证新改动不弄坏旧东西。</p>

<h2>第一原则：默认关 = 逐位不变</h2>
<div class="card">
<p>所有补丁默认不生效。不带 token 跑，程序的行为和打补丁前 <b>一个比特都不差</b>。这保证了：主干永远是可信的基准，任何实验都不污染它。</p>
<p>自检方法：bench 里 A 臂（不带 token）和旧基准逐位对比，分数必须完全相等。v10 里 A≡B≡F≡H 四臂等值，就是这个自检。</p>
</div>

<h2>上游关系</h2>
<div class="card">
<ul>
<li>我们的代码上游是 <b>xulai1001/umaai-rs</b>（别人写的原版）。我们是 fork/实验，<b>不往上游推东西</b></li>
<li>上游更新时走 sync 分支对齐（umaai-rs 有一堆 workbench/sync-* 和 workbench/101x120-upstream-ramen 分支，都是干这个的）</li>
<li>机制知识的上游是实机数据：所有游戏机制必须从游戏包原始文件、内存 dump、master.mdb 实测里来，<b>禁止脑补游戏机制</b></li>
</ul>
</div>

<h2>接口兼容三查</h2>
<ol>
<li><b>加字段用默认值</b>：新配置项必须有默认值，且默认值=旧行为（比如 cap_discount_floor 默认 0.0 = 不生效）</li>
<li><b>不删不改已有 token 含义</b>：旧 token 的行为冻结，新想法开新 token</li>
<li><b>计价诚实</b>：选择层可以看得宽松，但游戏入账层永远按真实规则截断（0008 补丁就是这么做的）</li>
</ol>

<h2>数据文件兼容</h2>
<div class="callout"><b>规则：</b>master.mdb 等游戏数据表更新时，先比对结构再换；训练数据（状态、策略、价值三元组）的格式改动必须在 uma-data 里留版本记录。三个模块（比赛模拟器/育成模拟器/训练数据）互相独立，<b>禁止跨模块混逻辑</b>。</div>
"""

CH_BUGFIX = """
<h1>🐛 修 Bug 维护语义</h1>
<p style="color:var(--sub)">复现、种子、世界线——抓虫子的纪律，和一次丢 2798 个文件的惨痛教训。</p>

<h2>修 bug 五步</h2>
<div class="card">
<ol>
<li><b>先复现，再谈修</b>：复现不了就先解决复现，别猜</li>
<li><b>固定种子</b>：用固定种子把问题局面录下来，可以一遍遍重放（这叫固定世界线）</li>
<li><b>最小化</b>：把触发条件削到最少</li>
<li><b>写补丁、默认关</b>：修复也要走补丁流，带开关</li>
<li><b>回归验证</b>：修完跑一遍 bench，确认没伤及无辜（分数大盘不能无故掉）</li>
</ol>
</div>

<h2>复现难怎么办</h2>
<div class="callout"><b>真实案例：</b>之前有个局面，CI 里迭代了三次才复现出来。复现难 ≠ 不能修，而是：① 把复现过程本身固化成种子+脚本，写进 CI；② 复现脚本就是修复的验收标准。复现脚本丢了，修复就等于没做。</div>

<h2>2798 个文件失踪案（必读教训）</h2>
<div class="card">
<p><b>案情：</b>泳装青云天空一局完整育成的抓包数据（465 对请求响应，2798 个文件），当年用 API 一个个传到了 GitHub，<b>但只建了 blob、从没提交进任何分支的 tree</b>。这种文件叫"悬空 blob"，GitHub 约两周自动回收。2026-08-16 审计发现时已无力回天。</p>
<p><b>教训：</b></p>
<ul>
<li>上传 ≠ 保存。<b>提交进分支、能在文件页看到，才算保存</b></li>
<li>大批量文件归档，传完立即验证：文件数、总字节、抽查内容三件套</li>
<li>不可替代的原始数据（抓包、dump）至少存两处：GitHub + 云盘/手机</li>
</ul>
<p><b>现状：</b>索引和公式闭环书还在（见 <a href="../repos/hlpatch-observation-architecture.html">hlpatch-observation-architecture</a>），源文件还在手机上（/data/user/0/jp.co.cygames.umamusume/files/hlpatch-observations），想恢复就用 hlpatch 重新导出。</p>
</div>

<h2>验证铁律</h2>
<ul>
<li><span class="bad">大文件交付前必须全量内容校验</span>——只验结构不验内容等于没验</li>
<li>改策略打分类代码，旧基准分数作废重跑，不拿旧分数比</li>
<li>禁止未验证的全量批量修改：跨多处的替换必须逐个验证再合并</li>
</ul>
"""

CH_PR = """
<h1>📬 PR 语义</h1>
<p style="color:var(--sub)">提交代码前必须懂的规矩。含 EXP-009 世界线教训——这次讨论里最重要的方法论。</p>

<h2>一个合格的提交长什么样</h2>
<ul>
<li>✅ 一个提交/一个分支只干一件事</li>
<li>✅ 提交信息说清楚：改了什么、为什么、证据在哪</li>
<li>✅ 推送后必查 CI，红修到绿</li>
<li>✅ 实验性改动默认关，不改变现有行为</li>
<li>❌ 不带未经测试的"顺手改"</li>
</ul>

<h2>🔴 世界线教训（EXP-009 批判）</h2>
<div class="card">
<p><b>出了什么事：</b>EXP-009 的模型迭代，可能是把"同时期的最优结论"落地、把"同时期的不良结论"砍掉。问题是：这些结论来自 <b>不同的随机世界线</b>（不同种子/不同蒙特卡洛抽样）。</p>
<p><b>为什么错：</b>把 A 世界线的最好结果和 B 世界线的失败结果拼在一起，等于在不同世界线之间挑樱桃。拼出来的"最优"可能只是 <b>当前世界线的运气成分</b>——蒙特卡洛穷举状态下被蒙蔽的最优解。这叫相位错误：你以为在优化策略，其实在拟合噪声。</p>
</div>
<div class="callout danger"><b>防骗三规：</b>
<ol>
<li><b>对比必须同世界线</b>：A/B 测试永远同种子配对（我们 bench 的 BASE_SEED 机制就是干这个的）</li>
<li><b>冠军必须换世界线复验</b>：任何"最优模型/最优结论"，必须在一组它没见过的种子上重新测，还赢才算数。<span class="warn">EXP-009b 冠军 66734.8 分目前只是"候选"，复验通过前不能当教师、不能当基线</span></li>
<li><b>砍结论要留尸</b>：被砍掉的不良结论不许物理删除，移进 invalidated/ 目录标注原因——防止以后不知情的人再捡回来，也防止审计断链</li>
</ol></div>

<h2>口径纪律</h2>
<div class="card">
<p>报分数必须带口径：什么种子、多少局、REC 直跑还是完整 MCTS、哪个 build。不带口径的分数一律拒收。72000/76000 之所以只能听个响，就是因为口径和数据都不在手。</p>
</div>

<h2>审批与边界</h2>
<ul>
<li>动赛马娘相关代码仓库前，<b>先问主人</b>（许可规则）</li>
<li>往上游（xulai1001）推东西：禁止</li>
<li>删除文件：先问，重要数据先备份再删</li>
<li>GitHub token、密钥：永不写进代码和文档，输出日志必须打码</li>
</ul>
"""

for cid, body in [('player', CH_PLAYER), ('game', CH_GAME), ('code', CH_CODE), ('fix', CH_FIX), ('compat', CH_COMPAT), ('bugfix', CH_BUGFIX), ('pr', CH_PR)]:
    title = next(t for c, t, _ in CHAPTERS if c == cid)
    page(os.path.join(OUT, 'ch', f'{cid}.html'), head(title, '<p><a href="../index.html">← 回总入口</a></p>') + body + FOOT)
print('chapters done')

# ---------- 每仓一页 ----------
def branch_note(repo, bname):
    """大白话分支注释：从名字推导，诚实标注"""
    n = bname
    if n in ('main', 'master'):
        return '主干分支：这个仓库的正式版本'
    if n.startswith('backup/'):
        return '备份快照：存档用，别在上面改东西'
    if n.startswith('release/') or n.startswith('publish/'):
        return '发布分支'
    notes = []
    kw = {
        'exp-0': '实验编号 ', 'exp0': '实验编号 ',
        'fix': '修复类', 'hotfix': '紧急修复', 'correct': '纠错类',
        'archive': '归档类', 'audit': '审计类', 'ledger': '账本类',
        'sync': '同步上游', 'upstream': '涉及上游', 'distill': '蒸馏',
        'teacher': '教师模型', 'bench': '测试场', 'repro': '复现',
        'sniff': '抓包嗅探', 'observer': '观测器', 'endpoint': '端点',
        'ramen': '拉面杯相关', 'session': '会话归档', 'fanfix': '粉丝数修复',
        'fanskip': '粉丝数跳过', 'slack': '溢出松弛', 'overflow': '溢出',
        'vcurve': '体力曲线', 'rera': '储备年代', 'rclamp': '储备钳制',
        'swimsuit': '泳装相关', 'seiun': '青云天空',
    }
    for k, v in kw.items():
        if k in n:
            notes.append(v)
    tail = ''
    if n.startswith('workbench/'):
        tail = '工作台实验分支：' + ('、'.join(dict.fromkeys(notes)) if notes else '一次实验一个分支')
    else:
        tail = '、'.join(dict.fromkeys(notes)) if notes else '功能/迭代分支'
    return tail

for name, info in inv.items():
    blurb = dict((x[0], x[1]) for grp in GROUPS for x in grp[1]).get(name, info.get('description', ''))
    brs = info['branches']
    rows = []
    for b in brs:
        note = branch_note(name, b['name'])
        gh_link = f"{GH}/{name}/tree/{b['name']}"
        rows.append(f"<tr><td><b>{esc(b['name'])}</b></td><td>{esc(note)}</td><td>{b['date']}</td><td><a href='{gh_link}' target='_blank' rel='noopener noreferrer'>{b['sha']} ↗</a></td></tr>")
    hot = ''
    if name == 'umaai-rs-fanfix':
        hot = """<div class="callout info"><b>本手册的宿主仓库。</b>当前活跃分支 workbench/slack-fix-v2：补丁 0006/0007/0008 + 九臂 bench + v10 判词都在这条线上。主干（main）保持上游干净基线，所有实验通过 CI 运行期应用补丁完成。</div>"""
    if name == 'hlpatch-observation-architecture':
        hot = """<div class="callout danger"><b>2798 文件失踪案现场。</b>泳装青云天空会话的原始载荷只建了 blob 未提交，已被 GitHub 回收。现存的只有索引（main）和解码器分支。源文件还在手机上，可重新导出。详见「修 Bug 语义」。</div>"""
    page(os.path.join(OUT, 'repos', f'{name}.html'), head(name, f'<p><a href="../index.html">← 回总入口</a> / <a href="{GH}/{name}" target="_blank" rel="noopener noreferrer">GitHub ↗</a></p>') + f"""
<h1>📦 {esc(name)}</h1>
<p>{esc(blurb)}</p>
<p><span class="tag">{len(brs)} 个分支</span><span class="tag">默认分支 {esc(info.get('default',''))}</span><span class="tag">约 {info.get('size_kb',0)//1024}MB</span><span class="tag">最近更新 {esc(info.get('updated',''))}</span>{'<span class="tag hot">fork（复制自上游）</span>' if info.get('fork') else ''}</p>
{hot}
<h2>分支清单（按最近活跃排序）</h2>
<div style="overflow-x:auto"><table>
<tr><th>分支</th><th>大白话注释</th><th>最近提交</th><th>链接</th></tr>
{''.join(rows)}
</table></div>
""" + FOOT)
print(f'repo pages done: {len(inv)}')
print('ALL DONE →', OUT)

