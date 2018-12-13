"""Main script for Sandbox."""

from app import app
from config import ACCESS_LOG, APP_PORT, DEBUG


def main():
    app.run(
        host='0.0.0.0',
        port=APP_PORT,
        access_log=ACCESS_LOG,
        debug=DEBUG,
    )


if __name__ == '__main__':
    main()
