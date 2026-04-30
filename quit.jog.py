import streamlit as st
import streamlit.components.v1 as components

# 設定 GitHub 圖片基本路徑
GITHUB_BASE_URL = "https://raw.githubusercontent.com/antimine722/Quit_your_job/main/" 

# 核心：確保 mischief_js 變數開頭沒有多餘空格
mischief_js = f"""
<div id="container" style="height: 500px; width: 100%; position: relative; border: 1px solid #eee; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding-top: 40px; background-color: #ffffff; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    
    <div style="width: 180px; height: 180px; border: 8px solid #fff; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.15); overflow: hidden; margin-bottom: 20px; transform: rotate(-3deg); transition: transform 0.3s;">
        <img id="decoImage" src="{GITHUB_BASE_URL}ci01.jpg" style="width: 100%; height: 100%; object-fit: cover;">
    </div>

    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #333; text-align: center; padding: 0 40px; transition: all 0.3s; font-size: 24px;">Fifi要離職了嗎?</h2>
    
    <button id="catchMe" style="position: absolute; top: 75%; left: 50%; transform: translate(-50%, -50%); padding: 12px 35px; background-color: #FF4B4B; color: white; border: none; border-radius: 50px; cursor: pointer; transition: left 0.15s ease-out, top 0.15s ease-out; font-size: 18px; font-weight: bold; z-index: 10; box-shadow: 0 5px 15px rgba(255,75,75,0.3);">確定</button>
</div>

<script>
    let escapePhaseClicks = 0;
    let hasStarted = false;
    const btn = document.getElementById('catchMe');
    const decoImage = document.getElementById('decoImage');
    const questionText = document.getElementById('question');
    const container = document.getElementById('container');

    const images = [
        "{GITHUB_BASE_URL}ci01.jpg",
        "{GITHUB_BASE_URL}ci02.jpg",
        "{GITHUB_BASE_URL}ci03.jpg"
    ];

    function changeImage() {{
        let newIndex = Math.floor(Math.random() * images.length);
        decoImage.src = images[newIndex];
        const randomDeg = Math.floor(Math.random() * 10) - 5;
        decoImage.parentElement.style.transform = `rotate(${{randomDeg}}deg) scale(1.05)`;
        setTimeout(() => {{
            decoImage.parentElement.style.transform = `rotate(${{randomDeg}}deg) scale(1)`;
        }}, 200);
    }}

    function handleEscape(e) {{
        if (!hasStarted) return;
        if (e.type === 'touchstart') e.preventDefault(); 
        
        const padding = 40;
        const btnW = btn.offsetWidth;
        const btnH = btn.offsetHeight;
        const contW = container.clientWidth;
        const contH = container.clientHeight;

        const newX = Math.random() * (contW - btnW - padding * 2) + padding;
        const newY = Math.random() * (contH - btnH - 250) + 200;

        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
        btn.style.transform = 'translate(0, 0)';

        escapePhaseClicks++;
        if (escapePhaseClicks === 1) {{
            questionText.innerText = "你捨得走嗎😭？";
            btn.innerText = "是";
        }} else if (escapePhaseClicks > 12) {{
            endMischief();
        }}
    }}

    btn.onmouseover = handleEscape;
    btn.ontouchstart = handleEscape;

    btn.onclick = function() {{
        changeImage();
        if (!hasStarted) {{
            hasStarted = true;
            questionText.innerText = "真的要離職了嗎😭？";
            handleEscape(new Event('click'));
        }}
    }};

    function endMischief() {{
        btn.onmouseover = null;
        btn.ontouchstart = null;
        btn.style.transition = "all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
        btn.style.left = "50%";
        btn.style.top = "75%";
        btn.style.transform = "translate(-50%, -50%) scale(1.1)";
        btn.innerText = "祝妳未來順利！";
        btn.style.backgroundColor = "#28a745";
        questionText.innerText = "Fifi畢業快樂🥹";
        questionText.style.color = "#28a745";
    }}
</script>
"""

components.html(mischief_js, height=550)

