__author__ = 'daotuanvu'
create_date = '1/29/2015'

import logging
import os
import yaml
import logging.config


def setup_logging(
        default_path='logging.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        print config
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == "__main__":
    # from config import config
    # logging.config.dictConfig(config)
    setup_logging()

    logger = logging.getLogger()
    logger.info("abc")