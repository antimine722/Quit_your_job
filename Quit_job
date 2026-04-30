import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="別想點到我", layout="centered")

st.title("追逐按鈕大挑戰 🏃‍♂️")

# 使用 HTML/JS 實作核心邏輯
mischief_js = """
<div id="container" style="height: 400px; width: 100%; position: relative; border: 1px dashed #ccc; overflow: hidden;">
    <button id="catchMe" style="
        position: absolute; 
        top: 50%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        padding: 10px 20px;
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.1s ease;
    ">點我呀！</button>
</div>

<p id="status" style="margin-top: 10px; font-family: sans-serif;"></p>

<script>
    let clickCount = 0;
    let escapeCount = 0;
    const btn = document.getElementById('catchMe');
    const status = document.getElementById('status');
    const container = document.getElementById('container');

    btn.onclick = function() {
        clickCount++;
        
        if (clickCount < 3) {
            status.innerText = `普通點擊次數: ${clickCount}`;
            if (clickCount === 2) {
                status.innerText += " (準備好了嗎？下次不一樣了...)";
            }
        } else {
            // 進入飄移模式
            escapeCount++;
            moveButton();
            
            if (escapeCount < 5) {
                status.innerText = `捉弄模式！還需捕捉次數: ${5 - escapeCount}`;
            } else {
                status.innerText = "🎉 挑戰成功！你終於抓到我了！";
                btn.style.top = "50%";
                btn.style.left = "50%";
                btn.innerText = "被抓到了 T_T";
                btn.style.backgroundColor = "#28a745";
                btn.onclick = null; // 停止遊戲
            }
        }
    };

    function moveButton() {
        const padding = 50;
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * maxY + padding/2;
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    // 額外挑戰：當滑鼠快碰到時就閃開 (第三次之後開啟)
    btn.onmouseover = function() {
        if (clickCount >= 3 && escapeCount < 5) {
            moveButton();
        }
    };
</script>
"""

# 渲染組件
components.html(mischief_js, height=500)

st.info("這是一個結合 Streamlit 與自定義 JavaScript 的範例。前兩次可以正常點擊，之後按鈕會開始逃跑！")
