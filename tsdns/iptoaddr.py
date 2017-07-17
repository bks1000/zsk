# coding:utf8
"""
根据IP获取主机名
"""
import sys, socket
 
try:
    result = socket.gethostbyaddr("127.0.0.1")
    print "Primary hostname:"
    print "  " + result[0]
 
    # Display the list of available addresses that is also returned
    print "\nAddresses:"
    for item in result[2]:
        print "  " + item
except socket.herror, e:
    print "Couldn't look up name:", e
