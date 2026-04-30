import streamlit as st
import streamlit.components.v1 as components

# ... 之前的程式碼 ...

# 核心：確保 mischief_js 變數開頭沒有多餘空格
mischief_js = """
<div id="container" style="height: 450px; width: 100%; position: relative; border: 1px solid #ddd; border-radius: 15px; overflow: hidden; background-color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #333; text-align: center; padding: 0 20px;">要離職了嗎?</h2>
    <button id="catchMe" style="position: absolute; top: 60%; left: 50%; transform: translate(-50%, -50%); padding: 15px 35px; background-color: #FF4B4B; color: white; border: none; border-radius: 50px; cursor: pointer; transition: all 0.1s ease; font-size: 18px; font-weight: bold; z-index: 10;">確定</button>
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
            questionText.innerText = "真的要離職了嗎?";
            btn.style.left = "25%";
            btn.style.top = "60%";
        } else if (totalClicks >= 2) {
            escapePhaseClicks++;
            if (escapePhaseClicks === 1) {
                questionText.innerText = "真的確定要離職了嗎?";
                btn.innerText = "是";
            }
            moveButton();
            if (escapePhaseClicks > 3) {
                questionText.innerText = "是";
                btn.style.top = "65%";
                btn.style.left = "50%";
                btn.innerText = "Fifi畢業快樂";
                btn.style.backgroundColor = "#28a745";
                btn.onclick = null;
            }
        }
    };

    function moveButton() {
        const padding = 80;
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * (maxY - 150) + 150;
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }
</script>
""" # 確保這三個引號的最前面沒有空格

components.html(mischief_js, height=550)



