# coding:utf8

"""
使用python dns模块
安装 easy_install dnspython
"""

import dns.resolver

def getipaddr():
    domain = raw_input('please input an domain:')
    A = dns.resolver.query(domain,'A')
    for i in A.response.answer:
        for j in i.items:
             if j.rdtype == 1:
                 print j.address
             else:
                 pass
if __name__ == '__main__':
    getipaddr()