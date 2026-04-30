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
        /* 極速位移：0.05s 幾乎就是瞬移感 */
        transition: all 0.05s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
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
        } else if (totalClicks >= 2) {
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
                btn.innerText = "祝前程似錦";
                btn.style.backgroundColor = "#28a745";
                btn.onclick = null;
                btn.onmouseover = null; // 結束後停止閃避
            }
        }
    };

    // 核心：滑鼠一靠近就飛走 (真正的追擊感)
    btn.onmouseover = function() {
        if (totalClicks >= 2 && escapePhaseClicks <= 3) {
            moveButton();
        }
    };

    function moveButton() {
        const padding = 80;
        const maxX = container.clientWidth - btn.clientWidth - padding;
        const maxY = container.clientHeight - btn.clientHeight - padding;
        // 避開標題文字區域
        const safeTopMargin = 150; 
        
        const newX = Math.random() * maxX + padding/2;
        const newY = Math.random() * (maxY - safeTopMargin) + safeTopMargin;
        
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
    }
</script>
"""



