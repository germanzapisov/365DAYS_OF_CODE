from pathlib import Path
import logging


# paths
path_logs = Path.cwd() / "logs"
path_logs.mkdir(exist_ok=True)
path_logs_file = path_logs / "logs.log"

# logging
logger = logging.Logger(__name__)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(filename=path_logs_file)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel = logging.DEBUG
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)
