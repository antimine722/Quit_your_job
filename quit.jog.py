# 先定義好變數，避免在字串內處理複雜邏輯
image_url_01 = GITHUB_BASE_URL + "ci01.jpg"
image_url_02 = GITHUB_BASE_URL + "ci02.jpg"
image_url_03 = GITHUB_BASE_URL + "ci03.jpg"

mischief_js = """
<div id="container" style="height: 500px; width: 100%; position: relative; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding-top: 40px; background-color: #ffffff;">
    <div style="width: 180px; height: 180px; border: 8px solid #fff; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.15); overflow: hidden; margin-bottom: 20px; transform: rotate(-3deg);">
        <img id="decoImage" src="IMG1" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <h2 id="question" style="margin-bottom: 30px; font-family: sans-serif; color: #333; text-align: center; padding: 0 40px; font-size: 24px;">要離職了嗎?</h2>
    <button id="catchMe" style="position: absolute; top: 75%; left: 50%; transform: translate(-50%, -50%); padding: 12px 35px; background-color: #FF4B4B; color: white; border: none; border-radius: 50px; cursor: pointer; font-size: 18px; font-weight: bold; z-index: 10;">確定</button>
</div>

<script>
    var escapePhaseClicks = 0;
    var hasStarted = false;
    var btn = document.getElementById('catchMe');
    var decoImage = document.getElementById('decoImage');
    var questionText = document.getElementById('question');
    var container = document.getElementById('container');

    var images = ["IMG1", "IMG2", "IMG3"];
    var lastImgIndex = 0;

    function changeImage() {
        var newIndex = Math.floor(Math.random() * images.length);
        if (newIndex === lastImgIndex) newIndex = (newIndex + 1) % images.length;
        lastImgIndex = newIndex;
        decoImage.src = images[newIndex];
    }

    function moveButton() {
        var padding = 50;
        var newX = Math.random() * (container.clientWidth - btn.offsetWidth - padding * 2) + padding;
        var newY = Math.random() * (container.clientHeight - btn.offsetHeight - 250) + 200;
        btn.style.left = newX + 'px';
        btn.style.top = newY + 'px';
        btn.style.transform = 'translate(0, 0)';
    }

    function handleEscape(e) {
        if (!hasStarted) return;
        if (e && e.type === 'touchstart') e.preventDefault();
        
        moveButton();
        escapePhaseClicks++;
        
        if (escapePhaseClicks === 1) {
            questionText.innerText = "真的要離職了嗎😭？";
            btn.innerText = "是";
        } else if (escapePhaseClicks > 10) {
            endMischief();
        }
    }

    // 點擊事件：負責「啟動」和「換圖」
    btn.onclick = function() {
        changeImage();
        if (!hasStarted) {
            hasStarted = true;
            questionText.innerText = "想點？看妳有沒有那個手速！";
            moveButton(); // 第一次點擊後立刻跑
        }
    };

    btn.onmouseover = handleEscape;
    btn.ontouchstart = handleEscape;

    function endMischief() {
        btn.onmouseover = null;
        btn.ontouchstart = null;
        btn.onclick = null;
        btn.style.left = "50%";
        btn.style.top = "75%";
        btn.style.transform = "translate(-50%, -50%)";
        btn.innerText = "畢業快樂！Fifi";
        btn.style.backgroundColor = "#28a745";
        questionText.innerText = "祝妳前程似錦！";
    }
</script>
""".replace("IMG1", image_url_01).replace("IMG2", image_url_02).replace("IMG3", image_url_03)

components.html(mischief_js, height=550)



