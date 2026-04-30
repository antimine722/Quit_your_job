import streamlit as st
import streamlit.components.v1 as components

mischief_js = """
<div id="container" style="height: 450px; width: 100%; position: relative; border: 1px solid #ddd; border-radius: 15px; overflow: hidden; background-color: #f8f9fa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <h2 id="question" style="margin-bottom: 30px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; text-align: center; padding: 0 20px; transition: all 0.3s;">要離職了嗎?</h2>
    <button id="catchMe" style="position: absolute; top: 60%; left: 50%; transform: translate(-50%, -50%); padding: 12px 30px; background-color: #FF4B4B; color: white; border: none; border-radius: 50px; cursor: pointer; transition: left 0.15s ease-out, top 0.15s ease-out; font-size: 18px; font-weight: bold; z-index: 10; box-shadow: 0 4px 15px rgba(255,75,75,0.3);">確定</button>
</div>

<script>
    let escapePhaseClicks = 0;
    let hasStarted = false;
    const btn = document.getElementById('catchMe');
    const questionText = document.getElementById('question');
    const container = document.getElementById('container');

    // 核心邏輯：滑鼠一靠近就逃跑
    btn.onmouseover = function() {
        if (!hasStarted) return; // 第一次點擊前不逃跑
        
        moveButton();
        escapePhaseClicks++;
        
        if (escapePhaseClicks === 1) {
            questionText.innerText = "真的要離職了嗎？";
            btn.innerText = "是";
        } else if (escapePhaseClicks === 5) {
            questionText.innerText = "真的真的真的確定要離職了嗎？";
            questionText.style.color = "#FF4B4B";
        } else if (escapePhaseClicks > 12) {
            // 結束惡作劇
            endMischief();
        }
    };

    // 第一次必須點擊才開始遊戲
    btn.onclick = function() {
        if (!hasStarted) {
            hasStarted = true;
            questionText.innerText = "想點？沒那麼容易！";
            moveButton();
        }
    };

    function moveButton() {
        const btnWidth = btn.offsetWidth;
        const btnHeight = btn.offsetHeight;
        const contWidth = container.clientWidth;
        const contHeight = container.clientHeight;

        // 計算安全邊距，避免按鈕跑出框外或貼邊
        const padding = 50;
        
        // 隨機生成新座標
        const newX = Math.random() * (contWidth - btnWidth - padding * 2) + padding;
        const newY = Math.random() * (contHeight - btnHeight - padding * 2) + padding;

        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
        btn.style.transform = 'translate(0, 0)'; // 取消原本的中心對齊偏移
    }

    function endMischief() {
        btn.onmouseover = null;
        btn.style.transition = "all 0.5s ease";
        btn.style.left = "50%";
        btn.style.top = "65%";
        btn.style.transform = "translate(-50%, -50%)";
        btn.innerText = "畢業快樂";
        btn.style.backgroundColor = "#28a745";
        btn.style.boxShadow = "0 4px 15px rgba(40,167,69,0.3)";
        questionText.innerText = "好啦，祝 Fifi 未來順利！";
        questionText.style.color = "#28a745";
    }
</script>
"""

components.html(mischief_js, height=550)





