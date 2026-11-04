from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from pathlib import Path

app = FastAPI()

LOG_FILE = Path(__file__).parent / "log.txt"

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <pre id="logs"></pre>

        <script>
            async function update() {
                const response = await fetch("/logs");
                const text = await response.text();
                document.getElementById("logs").textContent = text;
            }

            update();
            setInterval(update, 1000);
        </script>
    </body>
    </html>
    """

@app.get("/logs", response_class=PlainTextResponse)
def get_logs():
    if not LOG_FILE.exists():
        return "log.txt not found"

    return LOG_FILE.read_text(encoding="utf-8")

