# -*-coding:utf-8 -*-
import asyncio,logging,aiomysql

#creat database connection pool
@asyncio.coroutine
def crate_pool(loop,**kw):
    looging.info('create database connection pool...')
    global _pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
	port=kw,get('port',3306),
