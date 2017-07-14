from nose.tools import with_setup

def setup_func():
    print "set up test fixtures"

def teardown_func():
    print "tear down test fixtures"

@with_setup(setup_func, teardown_func)
def sample_test():
     assert 1 == 1