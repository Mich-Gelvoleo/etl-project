"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml

def main():
    """
        Entry Point to run the XETRA ETL job
    """

    #Parsing YAML file
    config_path = 'C:/Users/M-SP7/PycharmProjects/etl-project/etl-project/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    #Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()