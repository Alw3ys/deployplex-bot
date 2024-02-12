from dosei_sdk import Dosei

port = 8080
dosei = Dosei(
    name="dosei-bot",
    port=port,
    run=f"uvicorn bot.main:app --host 0.0.0.0 --port {port}"
)
