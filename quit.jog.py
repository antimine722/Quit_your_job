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

    function changeImage() {
        let newIndex = Math.floor(Math.random() * images.length);
        decoImage.src = images[newIndex];
        const randomDeg = Math.floor(Math.random() * 10) - 5;
        decoImage.parentElement.style.transform = `rotate(${randomDeg}deg) scale(1.05)`;
        setTimeout(() => {
            decoImage.parentElement.style.transform = `rotate(${randomDeg}deg) scale(1)`;
        }, 200);
    }

    // 核心修正：統一處理逃跑邏輯
    function handleEscape(e) {
        if (!hasStarted) return;
        
        // 防止手機點擊時的預設行為
        if (e.type === 'touchstart') e.preventDefault(); 
        
        moveButton();
        escapePhaseClicks++;
        
        if (escapePhaseClicks === 1) {
            questionText.innerText = "真的要離職了嗎？";
            btn.innerText = "是";
        } else if (escapePhaseClicks > 12) {
            endMischief();
        }
    }

    // 電腦版：滑鼠移入就跑
    btn.onmouseover = handleEscape;

    // 手機版：手指一碰就跑
    btn.ontouchstart = handleEscape;

    // 點擊事件：負責換圖與啟動
    btn.onclick = function() {
        changeImage();
        if (!hasStarted) {
            hasStarted = true;
            questionText.innerText = "想點？看妳有沒有那個手速！";
            moveButton();
        }
    };

    function moveButton() {
        const padding = 40; // 手機版邊距縮小一點
        const btnW = btn.offsetWidth;
        const btnH = btn.offsetHeight;
        const contW = container.clientWidth;
        const contH = container.clientHeight;

        const newX = Math.random() * (contW - btnW - padding * 2) + padding;
        const newY = Math.random() * (contH - btnH - 250) + 200;

        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
        btn.style.transform = 'translate(0, 0)';
    }

    function endMischief() {
        // 移除所有逃跑事件
        btn.onmouseover = null;
        btn.ontouchstart = null;
        
        btn.style.transition = "all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
        btn.style.left = "50%";
        btn.style.top = "75%";
        btn.style.transform = "translate(-50%, -50%) scale(1.1)";
        btn.innerText = "畢業快樂！Fifi";
        btn.style.backgroundColor = "#28a745";
        questionText.innerText = "祝妳前程似錦，有空回來看看！";
        questionText.style.color = "#28a745";
    }
</script>




