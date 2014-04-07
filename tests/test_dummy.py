# ! /usr/bin/env python
# \Dropbox\Reasearch_Nguyen\Dummy\tests
# Hoang Long Nguyen (hn269@cornell.edu)
# 2014/03/28
#
# 

#def dummy(n1,n2):
#    dummy = n1+n2
#    return dummy

from dummy import calc

def test_add():
    n1 = calc(1,'+',2)
    assert n1 == 3
    
def test_sub():
    n1 = calc(3,'-',5)
    assert n1 == -2
    
def test_mul():
    n1 = calc(3,'x',7)
    assert n1 == 21
    