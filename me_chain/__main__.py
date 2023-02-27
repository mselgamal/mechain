from me_chain import app
import logging
import uvicorn
import os

def main():
    port = int(os.environ.get("UVICORN_PORT", 8004))
    uvicorn.run("me_chain:app", port=port, reload=True, workers=1)


main()
