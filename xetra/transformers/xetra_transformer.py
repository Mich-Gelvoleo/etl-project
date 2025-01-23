"""Xetra ETL Component"""
import logging

from typing import NamedTuple

from xetra.common.s3 import S3BucketConnector

class XetraSourceConfig(NamedTuple):
    """
    Class for source configuration data

    src_first_extract_date: Determines the date for extracting the source
    src_columns: Source column names
    src_col_date: Column name for date in source
    src_col_isin: Column name for isin in source
    src_col_time: Column name for time in source
    src_col_start_price: Column name for starting price in source
    src_col_min_price: Column name for minimum price in source
    src_col_max_price: Column name for maximum price in source
    src_col_traded_vol: Column name for traded volume in source
    """

    src_first_extract_dates: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class XetraTargetConfig(NamedTuple):
    """
    Class for target configuration data

    trg_col_isin: Column name for isin in target
    trg_col_date: Column name for date in target
    trg_col_op_price: Column name for opening price in target
    trg_col_close_price: Column name for closing price in target
    trg_col_min_price: Column name for minimum price in target
    trg_col_max_price: Column name for maximum price in target
    trg_col_daily_trad_vol: Column name for daily traded volume in target
    trg_col_ch_prev_close: Column for change in previous day's closing price in target
    trg_key: Basic key of target file
    trg_key_date_format: Date format of target file key
    trg_format: File format of the target file
    """

    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_close_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_daily_trad_vol: str
    trg_col_ch_prev_close: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class XetraETL():
    """
    Reads  the Xetra data, transforms and writes the transformed to target
    """

    def __init__(self, s3_bucket_src: S3BucketConnector,
                 s3_bucket_trg: S3BucketConnector, meta_key: str,
                 src_args: XetraSourceConfig, trg_args: XetraTargetConfig):
        """
        Constructor for XetraTransformer

        :param s3_bucket_src: Connection to source S3 bucket
        :param s3_bucket_trg: Connection to target S3 bucket
        :param meta_key: Used as self.meta_key -> Key of meta file
        :param src_args: NamedTuple class with source config data
        :param trg_args: NamedTuple class with target config data
        """

        self._logger = logging.getLogger(__name__)
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date = ""
        self.extract_date_list = ""
        self.meta_update_list = ""
        
    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        pass




