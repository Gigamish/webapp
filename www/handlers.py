#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    summary = '更多精彩，敬请期待！'
    blogs = [
        Blog(id='1', name='德意志夜游记', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='论页岩气的前生今世', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='东昌府区适龄妇女的婚姻诉求', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }