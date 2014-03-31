# ! /usr/bin/env python
# \Dropbox\Reasearch_Nguyen\Dummy\tests
# Hoang Long Nguyen (hn269@cornell.edu)
# 2014/03/28
#
# 

#def dummy(n1,n2):
#    dummy = n1+n2
#    return dummy

import dummy

def test_add():
    n1 = dummy.add(1,2)
    assert n1 == 3
    
def test_sub():
    n1 = dummy.sub(3,5)
    assert n1 == -2
    