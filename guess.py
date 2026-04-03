# 猜数字小游戏 —— 零基础可直接运行
import random

# 程序生成一个1~100的随机数
secret_num = random.randint(1, 100)
print("========== 欢迎来到猜数字游戏 ==========")
print("我已经想好一个 1 到 100 之间的数字啦！")
print("快来猜猜看吧！")

# 记录猜的次数
count = 0

# 开始循环猜数字
while True:
    # 用户输入数字
    guess = input("\n请输入你猜的数字：")
    
    # 判断是不是数字
    if not guess.isdigit():
        print("⚠️ 请输入一个有效的数字！")
        continue
    
    # 转成数字类型
    guess = int(guess)
    count += 1

    # 判断大小
    if guess > secret_num:
        print("❌ 太大了！再小一点试试～")
    elif guess < secret_num:
        print("❌ 太小了！再大一点试试～")
    else:
        # 猜对了
        print("🎉 恭喜你！猜对啦！")
        print(f"🎯 正确数字就是：{secret_num}")
        print(f"📝 你一共猜了 {count} 次！")
        break

print("\n========== 游戏结束 ==========")

