from fastapi import FastAPI

app = FastAPI(name="Docker ASM")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
