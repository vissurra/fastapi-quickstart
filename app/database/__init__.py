import pymysql
from loguru import logger

logger.info(f'{pymysql.version_info=}')
