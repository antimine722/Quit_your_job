import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題
st.set_page_config(page_title="離職確認系統", layout="centered")

st.title("職涯發展確認系統 💼")

mischief_js = """
<div id="container" style="height: 450px; width: 100%; position: relative; border: 1px solid #ddd; border-radius: 15px; overflow: hidden; background-color: #ffffff; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center; justify-content: center;">
    
    <!-- 問題顯示區域 -->
    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #333; text-align: center; padding: 0 20px;">要離職了嗎?</h2>
    
    <!-- 按鈕 -->
    <button id="catchMe" style="
        position: absolute; 
        top: 60%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        padding: 15px 35px;
        background-color: #FF4B4B;
        color: white;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        white-space: nowrap;
        z-index: 10;
    ">確定</button>
</div>

<script>
    let totalClicks = 0;
    let escapePhaseClicks = 0;
    const btn = document.getElementById('catchMe');
    const questionText = document.getElementById('question');
    const container = document.getElementById('container');

    btn.onclick = function() {
        totalClicks++;
        
        if (totalClicks === 1) {
            // 點第一次：換問題 + 換位置（偏左）
            questionText.innerText = "真的要離職了嗎?";
            btn.style.left = "25%";
            btn.style.top = "60%";
            btn.style.backgroundColor = "#E63946";
        } 
        else if (totalClicks >= 2) {
            // 點第二次開始觸發追擊邏輯
            escapePhaseClicks++;
            
            if (escapePhaseClicks === 1) {
                // 剛進入追擊模式：換成第三個問題
                questionText.innerText = "真的確定要離職了嗎?";
                questionText.style.color = "#d90429";
                btn.innerText = "不要跑！";
            }
            
            // 執行位移
            moveButton();
            
            // 追擊成功三次後過關 (第2次點擊後的第3次追擊成功，共點擊5次)
            if (escapePhaseClicks > 3) {
                questionText.innerText = "🎉 畢業快樂！";
                questionText.style.color = "#28a745";
                questionText.style.fontSize = "40px";
                
                // 恢復按鈕到中間
                btn.style.top = "65%";
                btn.style.left = "50%";
                btn.style.transform = "translate(-50%, -50%)";
                btn.innerText = "祝前程似錦";
                btn.style.backgroundColor = "#28a745";
                btn.style.boxShadow = "0 4px 15px rgba(40, 167, 69, 0.3)";
                btn.onclick = null; 
                btn.onmouseover = null;
                btn.style.cursor = "default";
            }
        }
    };

    function moveButton() {
        const padding = 80;
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        
        // 限制按鈕不要擋到上面的問題文字
        const safeTopMargin = 150; 
        
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * (maxY - safeTopMargin) + safeTopMargin;
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    btn.onmouseover = function() {
        // 第二次點擊後且尚未完成時，滑鼠靠近有 40% 機率閃避
        if (totalClicks >= 2 && escapePhaseClicks <= 3) {
            if (Math.random() > 0.6) {
                moveButton();
            }
        }
    };
</script>
"""

components.html(mischief_js, height=550)

st.write("---")
st.caption("這是一個有趣的離職確認流程。請依序點擊按鈕來完成您的申請。")
    };
</script>
"""

components.html(mischief_js, height=520)

st.info("規則更新：第一次點擊後按鈕會左移，第二次點擊後開啟追逐模式，再抓到 3 次即可！")
