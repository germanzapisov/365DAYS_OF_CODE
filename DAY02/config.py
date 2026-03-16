import logging
from pathlib import Path


# paths
creation_logs_dir = Path(__file__).parent / "logs"
creation_logs_dir.mkdir(exist_ok=True)

# logging config
logger = logging.getLogger("game")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()

handler_debug = logging.FileHandler(filename=creation_logs_dir / "all_logs.log")
handler_debug.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
handler_debug.setFormatter(formatter)

logger.addHandler(handler_debug)
logger.addHandler(console)
