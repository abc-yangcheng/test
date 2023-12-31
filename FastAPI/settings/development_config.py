# -*- coding: utf-8 -*-

# @Project : fastapiDemo
# @File    : development_config.py.py
# @Date    : 2020-11-16
# @Author  : hutong
# @Describe: 微信公众： 大话性能


"""
开发环境配置
"""
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/shopdemo/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/shopdemo/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "172.16.137.129"
    MYSQL_DATABASE: str = 'Mall'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

#实例化的时候才会去验证数据类型
config = Config()

if __name__ == "__main__":
    pass
