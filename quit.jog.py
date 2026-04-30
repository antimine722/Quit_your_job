import streamlit as st
import streamlit.components.v1 as components

st.title("按鈕挑戰：精準位移版 🎯")

mischief_js = """
<div id="container" style="height: 450px; width: 100%; position: relative; border: 1px dashed #ccc; border-radius: 12px; overflow: hidden; background-color: #f0f2f6;">
    <button id="catchMe" style="
        position: absolute; 
        top: 50%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        padding: 12px 24px;
        background-color: #FF4B4B;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 16px;
        white-space: nowrap;
    ">點我開始</button>
</div>

<p id="status" style="margin-top: 15px; font-family: sans-serif; font-weight: bold;"></p>

<script>
    let totalClicks = 0;
    let escapePhaseClicks = 0;
    const btn = document.getElementById('catchMe');
    const status = document.getElementById('status');
    const container = document.getElementById('container');

    btn.onclick = function() {
        totalClicks++;
        
        if (totalClicks === 1) {
            // 第一次點完：移到偏左位置 (例如 25% 的寬度)
            btn.style.left = "25%";
            btn.style.top = "50%";
            btn.innerText = "再點一次";
            status.innerText = "第一步完成，它往左移了！";
        } 
        else if (totalClicks >= 2) {
            // 第二次點擊的瞬間：觸發飄移
            escapePhaseClicks++;
            moveButton();
            
            if (escapePhaseClicks <= 3) {
                status.innerText = `進入追逐！還需抓到 ${4 - escapePhaseClicks} 次！`;
                btn.innerText = "抓不到吧！";
                btn.style.backgroundColor = "#FFA500";
            } else {
                // 結束遊戲
                status.innerText = "🎉 恭喜過關！你贏了！";
                btn.style.top = "50%";
                btn.style.left = "50%";
                btn.innerText = "挑戰成功";
                btn.style.backgroundColor = "#28a745";
                btn.onclick = null; 
                btn.onmouseover = null;
            }
        }
    };

    function moveButton() {
        const padding = 60;
        // 確保按鈕不會跑出容器外
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * maxY + padding/2;
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    // 增加一點點滑鼠靠近就閃開的趣味性
    btn.onmouseover = function() {
        if (totalClicks >= 2 && escapePhaseClicks <= 3) {
            // 40% 的機率閃開
            if (Math.random() > 0.6) {
                moveButton();
            }
        }
    };
</script>
"""

components.html(mischief_js, height=520)

st.info("規則更新：第一次點擊後按鈕會左移，第二次點擊後開啟追逐模式，再抓到 3 次即可！")
