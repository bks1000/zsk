# coding:utf8

import json

def dump(dic):
    """
        将字典编码为JSON串
    """
    return json.dumps(dic)

def load(jsonstr):
    '''
        将JSON串转为字典对象
    '''
    return json.loads(jsonstr)
    