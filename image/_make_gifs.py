#!/usr/bin/env python3
"""Generate algorithm demo GIFs. Output next to this script."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W, H = 880, 320
BG = (250, 250, 250)
INK = (26, 26, 46)
MUTED = (85, 99, 110)
BLUE = (21, 101, 192)
BLUE_FILL = (187, 222, 251)
ORANGE = (230, 81, 0)
ORANGE_FILL = (255, 224, 178)
GREEN = (46, 125, 50)
GREEN_FILL = (200, 230, 201)
RED = (183, 28, 28)
RED_FILL = (255, 205, 210)
GREY_FILL = (236, 239, 241)
WHITE = (255, 255, 255)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size, index=0)
        except OSError:
            continue
    return ImageFont.load_default()


F16 = font(16)
F15B = font(16)
F13 = font(13)
F12 = font(12)


def canvas(title: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((1, 1, W - 2, H - 2), 12, outline=(224, 224, 224), width=1)
    d.text((W // 2, 22), title, fill=INK, font=F16, anchor="mm")
    return im, d


def box(d, x, y, w, h, text, fill, outline, tfill=INK, width=2):
    d.rounded_rectangle((x, y, x + w, y + h), 8, fill=fill, outline=outline, width=width)
    d.text((x + w / 2, y + h / 2), str(text), fill=tfill, font=F15B, anchor="mm")


def caption(d, text: str, y: int = 292):
    d.text((W // 2, y), text, fill=MUTED, font=F13, anchor="mm")


def save(frames: list[Image.Image], name: str, duration: int = 850):
    path = OUT / name
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(path.name, len(frames), "frames", path.stat().st_size // 1024, "KB")


def reverse_list():
    nodes = [1, 2, 3, 4, 5]
    frames = []

    def draw(edges, prev_i, cur_i, note):
        im, d = canvas("反转链表：每次把 cur.next 拧到 prev")
        xs = [70, 190, 310, 430, 550, 670]
        labels = ["null"] + [str(v) for v in nodes]
        for i, (x, lab) in enumerate(zip(xs, labels)):
            fill, outline, tfill = GREY_FILL, (144, 164, 174), MUTED
            if i == 0:
                pass
            elif i - 1 == cur_i:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            else:
                fill, outline, tfill = (227, 242, 253), BLUE, BLUE
            box(d, x, 90, 72, 48, lab, fill, outline, tfill)
        for a, b in edges:
            x1 = xs[a + 1] + 72 if a >= 0 else xs[0] + 72
            x2 = xs[b + 1] if b >= 0 else xs[0]
            y = 114
            if x2 >= x1:
                d.line((x1, y, x2, y), fill=BLUE, width=2)
                d.polygon([(x2, y), (x2 - 8, y - 5), (x2 - 8, y + 5)], fill=BLUE)
            else:
                d.line((x1 - 72, y + 28, (x1 + x2) / 2, y + 52), fill=ORANGE, width=2)
                d.line(((x1 + x2) / 2, y + 52, x2 + 72, y + 28), fill=ORANGE, width=2)
        if prev_i is not None:
            px = xs[0] if prev_i < 0 else xs[prev_i + 1]
            d.text((px + 36, 160), "prev", fill=ORANGE, font=F13, anchor="mm")
        if cur_i is not None:
            cx = xs[cur_i + 1]
            d.text((cx + 36, 178), "cur", fill=BLUE, font=F13, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw([(0, 1), (1, 2), (2, 3), (3, 4)], -1, 0, "初始：prev = null，cur = 1")
    draw([(-1, 0), (1, 2), (2, 3), (3, 4)], 0, 1, "拧 1：1.next = prev，prev 走到 1，cur 走到 2")
    draw([(-1, 0), (0, 1), (2, 3), (3, 4)], 1, 2, "拧 2：2.next = 1")
    draw([(-1, 0), (0, 1), (1, 2), (3, 4)], 2, 3, "拧 3")
    draw([(-1, 0), (0, 1), (1, 2), (2, 3)], 3, 4, "拧 4")
    draw([(-1, 0), (0, 1), (1, 2), (2, 3), (3, 4)], 4, None, "拧 5：cur 变空，prev 就是新头")
    save(frames, "reverse-list.gif", 900)


def three_sum():
    arr = [-4, -1, -1, 0, 1, 2]
    frames = []

    def draw(i, L, R, note, found=False):
        im, d = canvas("三数之和：排序后固定 i，左右夹逼")
        xs = [70 + k * 110 for k in range(6)]
        for k, v in enumerate(arr):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if k == i:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            elif k in (L, R):
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            if found and k in (i, L, R):
                fill, outline, tfill = GREEN_FILL, GREEN, GREEN
            box(d, xs[k], 90, 80, 48, v, fill, outline, tfill)
        d.text((xs[i] + 40, 160), "i", fill=ORANGE, font=F13, anchor="mm")
        d.text((xs[L] + 40, 178), "L", fill=BLUE, font=F13, anchor="mm")
        d.text((xs[R] + 40, 160), "R", fill=BLUE, font=F13, anchor="mm")
        s = arr[i] + arr[L] + arr[R]
        d.text((W // 2, 220), f"sum = {arr[i]} + {arr[L]} + {arr[R]} = {s}", fill=INK, font=F15B, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw(0, 1, 5, "固定 -4，L=-1，R=2，sum=-3 < 0，L 右移")
    draw(0, 2, 5, "仍是 -3，L 继续右移")
    draw(0, 3, 5, "sum=-2，还小")
    draw(0, 4, 5, "sum=-1，还小；L、R 相遇，这一轮结束")
    draw(1, 2, 5, "固定第一个 -1，跳过重复后再夹")
    draw(1, 3, 5, "sum=0，收到 [-1,0,2]")
    draw(1, 3, 5, "命中一组：[-1, 0, 2]", found=True)
    draw(1, 2, 4, "换下一对：[-1,-1,2] 也是 0", found=True)
    save(frames, "three-sum.gif", 950)


def binary_insert():
    arr = [1, 3, 5, 6]
    target = 2
    frames = []
    left, right = 0, 3
    steps = []
    while left <= right:
        mid = (left + right) // 2
        steps.append((left, right, mid, "比较"))
        if arr[mid] == target:
            break
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    steps.append((left, right, left, "插入"))

    def draw(L, R, mid, note):
        im, d = canvas("搜索插入位置：二分到空区间，left 就是插入点")
        xs = [140, 300, 460, 620]
        for k, v in enumerate(arr):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if L <= k <= R:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            if k == mid and "插入" not in note:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[k], 100, 80, 52, v, fill, outline, tfill)
            d.text((xs[k] + 40, 170), str(k), fill=MUTED, font=F12, anchor="mm")
        d.text((W // 2, 210), f"target = {target}    left={L}  mid={mid}  right={R}", fill=INK, font=F15B, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw(0, 3, 1, "left=0, right=3, mid=1，nums[1]=3 > 2，收缩右半")
    draw(0, 0, 0, "left=0, right=0, mid=0，nums[0]=1 < 2，left 移到 1")
    draw(1, 0, 1, "left > right，区间空了，插入下标 = left = 1")
    save(frames, "search-insert.gif", 1100)


def josephus():
    frames = []
    people = [1, 2, 3, 4, 5]
    M = 3
    order = []
    q = people[:]
    idx = 0
    snapshots = [("开始：5 人围圈，数到 3 出列", q[:], None, order[:])]
    while q:
        idx = (idx + M - 1) % len(q)
        out = q.pop(idx)
        order.append(out)
        snapshots.append((f"{out} 出列，出列顺序 {order}", q[:], out, order[:]))
        if not q:
            break
        idx %= len(q)

    def draw(note, remain, out, seq):
        im, d = canvas("报数游戏：N=5, M=3，约瑟夫环")
        n = 5
        cx, cy, r = 440, 150, 88
        import math
        for i, v in enumerate(people):
            ang = -math.pi / 2 + i * 2 * math.pi / n
            x = cx + r * math.cos(ang) - 24
            y = cy + r * math.sin(ang) - 24
            if v == out:
                fill, outline, tfill = RED_FILL, RED, RED
            elif v in remain:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            else:
                fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            box(d, x, y, 48, 48, v, fill, outline, tfill)
        caption(d, note + "    目标：3 1 5 2 4")
        frames.append(im)

    for s in snapshots:
        draw(*s)
    save(frames, "count-off.gif", 900)


def longest_substr():
    s = list("abcabcbb")
    frames = []
    last = {}
    L = 0
    best = 0
    states = []
    for R, ch in enumerate(s):
        if ch in last and last[ch] >= L:
            L = last[ch] + 1
        last[ch] = R
        best = max(best, R - L + 1)
        states.append((L, R, best, f"窗口 [{L},{R}] = {''.join(s[L:R+1])}，最长 {best}"))

    def draw(L, R, best, note):
        im, d = canvas("最长无重复子串：右扩，撞重复就把左指针推过去")
        xs = [40 + k * 100 for k in range(8)]
        for k, ch in enumerate(s):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if L <= k <= R:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            if k == R:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[k], 100, 72, 48, ch, fill, outline, tfill)
        d.text((xs[L] + 36, 170), "L", fill=BLUE, font=F13, anchor="mm")
        d.text((xs[R] + 36, 188), "R", fill=ORANGE, font=F13, anchor="mm")
        caption(d, note)
        frames.append(im)

    for st in states:
        draw(*st)
    save(frames, "longest-substring.gif", 700)


def climb_stairs():
    frames = []
    dp = [0, 1, 2, 3, 5, 8]

    def draw(k, note):
        im, d = canvas("爬楼梯：dp[i] = dp[i-1] + dp[i-2]")
        xs = [70 + i * 130 for i in range(6)]
        for i in range(6):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if i == 0:
                lab = "i=0"
                val = "—"
            else:
                lab = f"i={i}"
                val = str(dp[i]) if i <= k else "?"
            if i == k:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            elif i < k:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            box(d, xs[i], 100, 90, 52, val, fill, outline, tfill)
            d.text((xs[i] + 45, 172), lab, fill=MUTED, font=F12, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw(1, "1 阶：只有一种走法")
    draw(2, "2 阶：1+1 或 2")
    draw(3, "3 = 2 + 1")
    draw(4, "5 = 3 + 2")
    draw(5, "8 = 5 + 3，这就是斐波那契")
    save(frames, "climbing-stairs.gif", 1000)


def parentheses():
    s = list("()[]{}")
    frames = []
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    ok = True
    snaps = []
    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append(ch)
            snaps.append((stack[:], i, f"遇到 {ch}，入栈  →  {''.join(stack)}"))
        else:
            if not stack or stack[-1] != mapping[ch]:
                ok = False
                snaps.append((stack[:], i, f"{ch} 对不上，失败"))
                break
            stack.pop()
            snaps.append((stack[:], i, f"遇到 {ch}，弹出配对  →  栈 {''.join(stack) or '空'}"))
    snaps.append((stack[:], len(s) - 1, "扫完栈空，有效" if ok and not stack else "无效"))

    def draw(st, i, note):
        im, d = canvas("有效括号：左括号进栈，右括号必须刚好弹出配对")
        xs = [80 + k * 120 for k in range(6)]
        for k, ch in enumerate(s):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if k < i:
                fill, outline, tfill = GREEN_FILL, GREEN, GREEN
            if k == i:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[k], 80, 72, 48, ch, fill, outline, tfill)
        d.text((80, 180), "栈：", fill=MUTED, font=F13, anchor="lm")
        if st:
            for j, ch in enumerate(st):
                box(d, 130 + j * 70, 156, 56, 44, ch, BLUE_FILL, BLUE, BLUE)
        else:
            d.text((140, 178), "空", fill=MUTED, font=F13, anchor="lm")
        caption(d, note)
        frames.append(im)

    for sn in snaps:
        draw(*sn)
    save(frames, "valid-parentheses.gif", 850)


def two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    frames = []
    seen = {}
    snaps = []
    for i, v in enumerate(nums):
        need = target - v
        snaps.append((dict(seen), i, need, f"看 {v}，缺 {need}" + ("，哈希里有" if need in seen else "，记下自己")))
        if need in seen:
            snaps.append((dict(seen), i, need, f"命中：下标 {seen[need]} 和 {i}，{nums[seen[need]]}+{v}={target}"))
            break
        seen[v] = i

    def draw(mp, i, need, note):
        im, d = canvas("两数之和：一边走一边把值丢进哈希")
        xs = [90, 280, 470, 660]
        for k, v in enumerate(nums):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if v in mp:
                fill, outline, tfill = GREEN_FILL, GREEN, GREEN
            if k == i:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[k], 90, 90, 52, f"{v}", fill, outline, tfill)
            d.text((xs[k] + 45, 160), f"下标 {k}", fill=MUTED, font=F12, anchor="mm")
        mp_txt = ", ".join(f"{a}→{b}" for a, b in mp.items()) or "空"
        d.text((W // 2, 210), f"哈希表：{mp_txt}    当前缺 {need}", fill=INK, font=F13, anchor="mm")
        caption(d, note)
        frames.append(im)

    for sn in snaps:
        draw(*sn)
    save(frames, "two-sum.gif", 1000)


def house_robber():
    nums = [2, 7, 9, 3, 1]
    frames = []
    dp = [0] * 5
    dp[0] = 2
    dp[1] = max(2, 7)
    for i in range(2, 5):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    def draw(k, note):
        im, d = canvas("打家劫舍：偷 i 就不能偷 i-1")
        xs = [70 + i * 150 for i in range(5)]
        for i, v in enumerate(nums):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if i < k:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            if i == k:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[i], 90, 90, 48, v, fill, outline, tfill)
            val = str(dp[i]) if i <= k else "?"
            d.text((xs[i] + 45, 168), f"dp={val}", fill=INK, font=F13, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw(0, "只有第 1 家：dp=2")
    draw(1, "前两家取大的：max(2,7)=7")
    draw(2, "max(7, 2+9)=11")
    draw(3, "max(11, 7+3)=11，3 不偷更优")
    draw(4, "max(11, 11+1)=12")
    save(frames, "house-robber.gif", 1000)


def peak():
    nums = [1, 2, 3, 1]
    frames = []
    left, right = 0, 3
    snaps = []
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            snaps.append((left, right, mid, f"nums[{mid}]={nums[mid]} > 右边，峰在左侧（含 mid）"))
            right = mid
        else:
            snaps.append((left, right, mid, f"nums[{mid}]={nums[mid]} < 右边，峰在右侧"))
            left = mid + 1
    snaps.append((left, right, left, f"收敛到下标 {left}，峰值 {nums[left]}"))

    def draw(L, R, mid, note):
        im, d = canvas("寻找峰值：往更高的一侧收缩，O(log n)")
        xs = [140, 300, 460, 620]
        for k, v in enumerate(nums):
            fill, outline, tfill = GREY_FILL, (176, 190, 197), MUTED
            if L <= k <= R:
                fill, outline, tfill = BLUE_FILL, BLUE, BLUE
            if k == mid:
                fill, outline, tfill = ORANGE_FILL, ORANGE, ORANGE
            box(d, xs[k], 100, 80, 52, v, fill, outline, tfill)
            d.text((xs[k] + 40, 170), str(k), fill=MUTED, font=F12, anchor="mm")
        caption(d, note)
        frames.append(im)

    for sn in snaps:
        draw(*sn)
    save(frames, "find-peak.gif", 1100)


def candy():
    arr = [1, 0, 2]
    frames = []
    n = 3
    candies = [1, 1, 1]
    frames_notes = [(candies[:], "每人先发 1 颗")]
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    frames_notes.append((candies[:], "从左到右：右边更高就比左边多 1"))
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    frames_notes.append((candies[:], "从右到左：左边更高再补，最少 2+1+2=5"))

    def draw(c, note):
        im, d = canvas("分糖果：两遍扫描，相邻更高的必须更多")
        xs = [180, 400, 620]
        for i, v in enumerate(arr):
            box(d, xs[i], 80, 90, 48, f"分{v}", BLUE_FILL, BLUE, BLUE)
            box(d, xs[i], 150, 90, 48, f"{c[i]}颗", ORANGE_FILL, ORANGE, ORANGE)
        caption(d, note)
        frames.append(im)

    for c, note in frames_notes:
        draw(c, note)
    save(frames, "candy.gif", 1200)


def basketball():
    frames = []
    # 示例：push 4,5,6,7,0,1,2  pop 6,4,0,1,2,5,7  -> RLRRRLL
    push = [4, 5, 6, 7, 0, 1, 2]
    want = [6, 4, 0, 1, 2, 5, 7]
    bucket = []
    out = ""
    wi = 0
    snaps = [("空桶，老师按 4,5,6,7,0,1,2 放，目标取出 6,4,0,1,2,5,7", bucket[:], out)]
    for x in push:
        bucket.append(x)
        snaps.append((f"右边放入 {x}", bucket[:], out))
        while bucket:
            if bucket[0] == want[wi]:
                bucket.pop(0)
                out += "L"
                wi += 1
                snaps.append((f"左边取出，操作 {out}", bucket[:], out))
            elif bucket[-1] == want[wi]:
                bucket.pop()
                out += "R"
                wi += 1
                snaps.append((f"右边取出，操作 {out}", bucket[:], out))
            else:
                break
    snaps.append((f"完成：{out}", bucket[:], out))

    def draw(note, bkt, ops):
        im, d = canvas("篮球游戏：桶是双端队列，右边进，两边出")
        d.text((80, 90), "左 L", fill=BLUE, font=F13, anchor="lm")
        d.text((800, 90), "右 R", fill=ORANGE, font=F13, anchor="rm")
        if bkt:
            total = len(bkt)
            start = 200
            for i, v in enumerate(bkt):
                box(d, start + i * 80, 110, 64, 48, v, BLUE_FILL, BLUE, BLUE)
        else:
            d.text((W // 2, 134), "（空）", fill=MUTED, font=F13, anchor="mm")
        d.text((W // 2, 200), f"操作串：{ops or '（还没有）'}", fill=INK, font=F15B, anchor="mm")
        caption(d, note)
        frames.append(im)

    # 太多步会很长，抽关键帧：空、放入到第一次取出、以及每次取出
    keep = [snaps[0]]
    last_ops = ""
    for sn in snaps[1:]:
        if sn[2] != last_ops or "放入" in sn[0]:
            keep.append(sn)
            last_ops = sn[2]
    for sn in keep:
        draw(*sn)
    save(frames, "basketball.gif", 700)


def replant():
    """N=10, dead=[2,4,7], K=1 → cover 7 → consecutive 6."""
    n, dead, k = 10, [2, 4, 7], 1
    frames = []

    def draw(cover, note, hi=None):
        im, d = canvas("补种胡杨：窗口盖住最多 K 棵死树，求最长连续活树")
        xs = [40 + i * 80 for i in range(n)]
        cover_set = set(cover)
        for i in range(1, n + 1):
            x = xs[i - 1]
            if i in dead and i not in cover_set:
                box(d, x, 90, 64, 48, i, RED_FILL, RED, RED)
                d.text((x + 32, 154), "死", fill=RED, font=F12, anchor="mm")
            elif i in cover_set:
                box(d, x, 90, 64, 48, i, ORANGE_FILL, ORANGE, ORANGE)
                d.text((x + 32, 154), "补", fill=ORANGE, font=F12, anchor="mm")
            else:
                box(d, x, 90, 64, 48, i, GREEN_FILL, GREEN, GREEN)
                d.text((x + 32, 154), "活", fill=GREEN, font=F12, anchor="mm")
        if hi:
            x0, x1 = xs[hi[0] - 1], xs[hi[1] - 1] + 64
            d.rounded_rectangle((x0 - 6, 80, x1 + 6, 168), 10, outline=BLUE, width=3)
            d.text(((x0 + x1) / 2, 200), f"连续 {hi[1] - hi[0] + 1} 棵", fill=BLUE, font=F13, anchor="mm")
        caption(d, note)
        frames.append(im)

    draw([], "编号 1-10，死树在 2、4、7，只能补 1 棵", None)
    draw([2], "补 2：连续 1-3，长度 3", (1, 3))
    draw([4], "补 4：连续 3-6，长度 4", (3, 6))
    draw([7], "补 7：连续 5-10，长度 6（最优）", (5, 10))
    save(frames, "replant-poplar.gif", 1200)


def main():
    reverse_list()
    three_sum()
    binary_insert()
    josephus()
    longest_substr()
    climb_stairs()
    parentheses()
    two_sum()
    house_robber()
    peak()
    candy()
    basketball()
    replant()


if __name__ == "__main__":
    main()
