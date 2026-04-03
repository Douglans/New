# 猜数字小游戏 v2.0 增强版
# 作者：Douglans
# 功能：难度选择、次数限制、本地排行榜、重新开局、输入校验
# 运行环境：Python 3.x

import random

# 排行榜
leaderboard = []

def show_leaderboard():
    print("\n📊 排行榜")
    print("=" * 30)
    sorted_board = sorted(leaderboard, key=lambda x: x[1])
    for i, (name, count) in enumerate(sorted_board[:3], 1):
        print(f"第{i}名：{name} - {count} 次")
    if not sorted_board:
        print("暂无记录")
    print("=" * 30)

def get_input(prompt, min_num=None, max_num=None):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("⚠️ 请输入数字！")
            continue
        num = int(text)
        if min_num is not None and num < min_num:
            print(f"⚠️ 不能小于 {min_num}")
            continue
        if max_num is not None and num > max_num:
            print(f"⚠️ 不能大于 {max_num}")
            continue
        return num

def choose_difficulty():
    print("\n🎮 选择难度")
    print("1 - 简单 (10次机会)")
    print("2 - 普通 (5次机会)")
    print("3 - 困难 (3次机会)")
    choice = get_input("请选择(1-2-3)：", 1, 3)
    if choice == 1:
        return 10, "简单模式"
    elif choice == 2:
        return 5, "普通模式"
    else:
        return 3, "困难模式"

def play():
    chances, difficulty = choose_difficulty()
    secret = random.randint(1, 100)
    count = 0
    left = chances

    print(f"\n✅ 已选择：{difficulty}")
    print(f"🎯 你有 {left} 次机会！")

    while left > 0:
        print(f"\n剩余机会：{left}")
        guess = get_input("请猜数字(1-100)：", 1, 100)
        count += 1
        left -= 1

        if guess > secret:
            print("❌ 太大了！")
        elif guess < secret:
            print("❌ 太小了！")
        else:
            print("\n🎉 恭喜你猜对了！")
            print(f"答案：{secret}")
            print(f"你用了 {count} 次！")
            name = input("输入你的名字记录排行：")
            leaderboard.append((name, count))
            show_leaderboard()
            return

    print("\n💥 机会用完！")
    print(f"答案是：{secret}")

def main():
    print("=" * 40)
    print("    猜数字小游戏 v2.0 增强版")
    print("=" * 40)
    show_leaderboard()

    while True:
        print("\n======== 新游戏 ========\n")
        play()
        again = input("再玩一局？(y/n)：").lower()
        if again != "y":
            print("\n👋 游戏结束！")
            break

if __name__ == "__main__":
    main()
