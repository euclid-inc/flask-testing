import unittest

from .test_utils import TestSetup, TestClientUtils, TestLiveServer


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    suite.addTest(unittest.makeSuite(TestClientUtils))
    suite.addTest(unittest.makeSuite(TestLiveServer))
    return suite
