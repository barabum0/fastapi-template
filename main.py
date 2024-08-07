import uvicorn
from loguru import logger

from src.services.logs import configure_logger, get_uvicorn_log_config


def main() -> None:
    configure_logger()
    logger.info("Starting app...")

    uvicorn.run("src.app:app", log_config=get_uvicorn_log_config(), port=8080, host="0.0.0.0")


if __name__ == "__main__":
    main()
