from me_chain import app
import logging
import uvicorn
import os

def main():
    port = int(os.environ.get("UVICORN_PORT", 8004))
    uvicorn.run(app, port=port)


if __name__ == "__main__":
    main()
