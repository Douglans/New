# 🎮 猜数字小游戏
一个零基础可直接运行的Python入门级小游戏，适合Python初学者学习、展示。

## ✨ 功能特性
- 程序自动生成1~100的随机数，玩家输入数字猜谜
- 完善的输入校验，防止非数字输入导致程序崩溃
- 实时提示「太大了/太小了」，引导玩家快速猜中
- 记录猜中次数，游戏结束后展示结果
- 全程中文友好提示，新手零门槛上手

## 🛠️ 运行环境
- Python 3.x（Python 3.6+ 均可）

## 🎯 运行方法
### 方法1：直接运行
```bash
python3 猜.py


# 猜数字小游戏 网页版 v1.0
# 作者：Douglans
# 基于Streamlit，可直接在线部署

import streamlit as st
import random

# 页面配置
st.set_page_config(page_title="猜数字小游戏", page_icon="🎮", layout="centered")

# 初始化会话状态
if "secret_num" not in st.session_state:
    st.session_state.secret_num = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.chances_left = 10
    st.session_state.game_over = False
    st.session_state.win = False

# 标题
st.title("🎮 猜数字小游戏")
st.subheader("一个零基础可直接玩的Python入门小游戏")

# 难度选择
difficulty = st.selectbox("选择难度", ["简单(10次机会)", "普通(5次机会)", "困难(3次机会)"])
if difficulty == "简单(10次机会)":
    st.session_state.chances_left = 10
elif difficulty == "普通(5次机会)":
    st.session_state.chances_left = 5
else:
    st.session_state.chances_left = 3

# 重置游戏按钮
if st.button("🔄 重新开局"):
    st.session_state.secret_num = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.game_over = False
    st.session_state.win = False
    st.rerun()

# 游戏主体
if not st.session_state.game_over and not st.session_state.win:
    st.info(f"剩余机会：{st.session_state.chances_left}次 | 已猜次数：{st.session_state.count}次")
    guess = st.number_input("请输入你猜的数字（1-100）", min_value=1, max_value=100, step=1)
    
    if st.button("🎯 猜！"):
        st.session_state.count += 1
        st.session_state.chances_left -= 1
        
        if guess > st.session_state.secret_num:
            st.error("❌ 太大了！再小一点试试~")
        elif guess < st.session_state.secret_num:
            st.error("❌ 太小了！再大一点试试~")
        else:
            st.success(f"🎉 恭喜你！猜对啦！正确数字是：{st.session_state.secret_num}")
            st.success(f"📝 你一共猜了 {st.session_state.count} 次！")
            st.session_state.win = True
        
        # 机会用完
        if st.session_state.chances_left == 0 and not st.session_state.win:
            st.error(f"💥 机会用完啦！游戏结束~ 正确数字是：{st.session_state.secret_num}")
            st.session_state.game_over = True

# 游戏结束状态
elif st.session_state.win:
    st.balloons()
    st.success("🎉 游戏胜利！点击「重新开局」再玩一局吧！")
elif st.session_state.game_over:
    st.error("💥 游戏结束！点击「重新开局」再挑战一次吧！")

# 项目说明
with st.expander("📝 项目说明"):
    st.markdown("""
    - 这是一个Python入门级猜数字小游戏，支持三档难度选择
    - 网页版基于Streamlit开发，可直接在线玩，无需安装环境
    - 源码已开源在GitHub，欢迎Star⭐
    """)

