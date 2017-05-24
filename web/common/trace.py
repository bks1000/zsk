# coding:utf8
'''
python装饰器 实现日志记录
'''

def trace_func(func):
    '''
    A decorate function to track all function invoke information with DEBUG level
    Usage:
    @trace_func
    def any_function(any parametet)
    '''
    def tmp(*args, **kargs):
        print 'Start %s(%s, %s)...' % (func.__name__, args, kargs)
        return func(*args, **kargs)
    return tmp
