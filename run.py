"""
Running the Xetra ETL application.
"""
import logging
import logging.config

import yaml
from xetra.common.s3 import S3BucketConnector

def main():
    """
    Entry point to run the xetra ETL job
    """
    # Parsing YAML file
    config_path = '/Users/d_anderson/Desktop/xetra_project/xetra_ipynb/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()
