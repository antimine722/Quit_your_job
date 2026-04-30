import streamlit as st
import streamlit.components.v1 as components

# --- 設定 GitHub 圖片基本路徑 ---
# 指向 antimine722 的 Quit_your_job 儲存庫
GITHUB_BASE_URL = "https://raw.githubusercontent.com/antimine722/Quit_your_job/main/" 

mischief_js = f"""
<div id="container" style="height: 500px; width: 100%; position: relative; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: background-image 0.5s ease-in-out; background-size: cover; background-position: center; background-image: url('{GITHUB_BASE_URL}ci01.jpg');">
    
    <!-- 遮罩層：確保文字跟按鈕在背景圖上都能看清楚 -->
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(255, 255, 255, 0.45); z-index: 1;"></div>

    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #111; text-align: center; padding: 0 40px; transition: all 0.3s; z-index: 2; text-shadow: 2px 2px 4px rgba(255,255,255,0.9); font-size: 28px;">要離職了嗎?</h2>
    
    <button id="catchMe" style="position: absolute; top: 60%; left: 50%; transform: translate(-50%, -50%); padding: 15px 40px; background-color: #FF4B4B; color: white; border: none; border-radius: 50px; cursor: pointer; transition: left 0.15s ease-out, top 0.15s ease-out, transform 0.1s; font-size: 20px; font-weight: bold; z-index: 10; box-shadow: 0 6px 20px rgba(255,75,75,0.4);">確定</button>
</div>

<script>
    let escapePhaseClicks = 0;
    let hasStarted = false;
    const btn = document.getElementById('catchMe');
    const questionText = document.getElementById('question');
    const container = document.getElementById('container');

    // 圖片清單
    const images = [
        "{GITHUB_BASE_URL}ci01.jpg",
        "{GITHUB_BASE_URL}ci02.jpg",
        "{GITHUB_BASE_URL}ci03.jpg"
    ];

    let lastImgIndex = 0;

    function changeBackground() {{
        // 隨機選一個跟上次不一樣的 index
        let newIndex;
        do {{
            newIndex = Math.floor(Math.random() * images.length);
        }} while (newIndex === lastImgIndex);
        
        lastImgIndex = newIndex;
        container.style.backgroundImage = `url('${{images[newIndex]}}')`;
    }}

    // 滑鼠移入：逃跑
    btn.onmouseover = function() {{
        if (!hasStarted) return;
        
        moveButton();
        escapePhaseClicks++;
        
        if (escapePhaseClicks === 1) {{
            questionText.innerText = "真的要離職了嗎？";
            btn.innerText = "是";
        }} else if (escapePhaseClicks === 5) {{
            questionText.innerText = "妳看這照片，捨得走嗎？";
        }} else if (escapePhaseClicks > 12) {{
            endMischief();
        }}
    }};

    // 點擊按鈕：換背景
    btn.onclick = function() {{
        changeBackground();

        if (!hasStarted) {{
            hasStarted = true;
            questionText.innerText = "想點？看妳有沒有那個手速！";
            moveButton();
        }}
    }};

    function moveButton() {{
        const padding = 70;
        const btnW = btn.offsetWidth;
        const btnH = btn.offsetHeight;
        const contW = container.clientWidth;
        const contH = container.clientHeight;

        const newX = Math.random() * (contW - btnW - padding * 2) + padding;
        const newY = Math.random() * (contH - btnH - padding * 2) + padding;

        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
        btn.style.transform = 'translate(0, 0)';
    }}

    function endMischief() {{
        btn.onmouseover = null;
        btn.style.transition = "all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
        btn.style.left = "50%";
        btn.style.top = "70%";
        btn.style.transform = "translate(-50%, -50%) scale(1.1)";
        
        btn.innerText = "畢業快樂！Fifi";
        btn.style.backgroundColor = "#28a745";
        btn.style.boxShadow = "0 6px 20px rgba(40,167,69,0.5)";
        
        questionText.innerText = "好啦，不鬧了，祝妳未來一帆風順！";
        questionText.style.color = "#155724";
        questionText.style.fontSize = "26px";
    }}
</script>
"""

components.html(mischief_js, height=550)





