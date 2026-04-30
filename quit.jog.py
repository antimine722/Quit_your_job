# 核心：調整 transition 速度與隨機閃避機率
mischief_js = """
<div id="container" style="height: 450px; width: 100%; position: relative; border: 1px solid #ddd; border-radius: 15px; overflow: hidden; background-color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    
    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #333; text-align: center; padding: 0 20px;">要離職了嗎?</h2>
    
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
        transition: all 0.08s ease; /* 縮短時間讓移動變快 */
        font-size: 18px;
        font-weight: bold;
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
            questionText.innerText = "真的要離職了嗎?";
            btn.style.left = "25%";
            btn.style.top = "60%";
        } 
        else if (totalClicks >= 2) {
            escapePhaseClicks++;
            
            if (escapePhaseClicks === 1) {
                questionText.innerText = "真的確定要離職了嗎?";
                btn.innerText = "不要跑！";
            }
            
            moveButton();
            
            if (escapePhaseClicks > 3) {
                questionText.innerText = "🎉 畢業快樂！";
                btn.style.top = "65%";
                btn.style.left = "50%";
                btn.style.transform = "translate(-50%, -50%)";
                btn.innerText = "祝前程似錦";
                btn.style.backgroundColor = "#28a745";
                btn.onclick = null; 
                btn.onmouseover = null;
            }
        }
    };

    function moveButton() {
        const padding = 80;
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        const safeTopMargin = 150; 
        
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * (maxY - safeTopMargin) + safeTopMargin;
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }

    btn.onmouseover = function() {
        // 設定 40% 的機率閃開 (Math.random() 小於 0.4)
        if (totalClicks >= 2 && escapePhaseClicks <= 3) {
            if (Math.random() < 0.4) {
                moveButton();
            }
        }
    };
</script>
"""
