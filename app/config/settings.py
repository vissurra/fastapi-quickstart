import os

import toml
from loguru import logger

active = os.getenv('CONFIG', 'local')
logger.info(f'Active env: {active}')

path = f'app/config/config_{active}.toml'
if not os.path.exists(path):
    raise Exception(f'No config found: {active=}')

CONFIG = toml.load(path)
