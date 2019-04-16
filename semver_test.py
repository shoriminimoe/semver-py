#!/usr/bin/env python
import semver
import unittest

class SemVerTest(unittest.TestCase):
    """Semantic Versioning Module Test Class"""

    def setUp(self):
        self.sv1Str = 'v1.2.3-alpha.0+build123-42-g123abcd'
        self.sv1 = semver.SemVer(self.sv1Str)
        self.sv2Str = 'v1.2.3'
        self.sv2 = semver.SemVer(self.sv2Str)
        self.sv3Str = 'v1.2.3-alpha.0+11-gabcd123'
        self.sv3 = semver.SemVer(self.sv3Str)
        self.sv4Str = 'v1.2.3-rc.1.0'
        self.sv4 = semver.SemVer(self.sv4Str)
        self.sv5Str = 'v1.2.3-rc.2.1'
        self.sv5 = semver.SemVer(self.sv5Str)

    def testStr(self):
        self.assertEqual(str(self.sv1), self.sv1Str.lstrip('v'))
        self.assertEqual(str(self.sv2), self.sv2Str.lstrip('v'))
    
    def testTag(self):
        self.assertEqual(self.sv1.tag(), self.sv1Str)
        self.assertEqual(self.sv2.tag(), self.sv2Str)
    
    def testPrefix(self):
        self.assertEqual(self.sv1.prefix, 'v')
        self.assertEqual(self.sv2.prefix, 'v')
    
    def testMajor(self):
        self.assertEqual(self.sv1.major, 1)
        self.assertEqual(self.sv2.major, 1)
    
    def testMinor(self):
        self.assertEqual(self.sv1.minor, 2)
        self.assertEqual(self.sv2.minor, 2)
    
    def testPatch(self):
        self.assertEqual(self.sv1.patch, 3)
        self.assertEqual(self.sv2.patch, 3)
    
    def testPrerelease(self):
        self.assertEqual(self.sv1.prerelease, 'alpha.0')
        self.assertIsNone(self.sv2.prerelease)
    
    def testBuild(self):
        self.assertEqual(self.sv1.build, 'build123-42-g123abcd')
        self.assertIsNone(self.sv2.build)
    
    def testLT(self):
        self.assertTrue(self.sv1 < self.sv2)
        self.assertFalse(self.sv1 < self.sv3)
        self.assertTrue(self.sv1 < self.sv4)
        self.assertTrue(self.sv1 < self.sv5)
        self.assertTrue(self.sv4 < self.sv5)
    
    def testEQ(self):
        self.assertTrue(self.sv1 == self.sv3)
        self.assertFalse(self.sv1 == self.sv2)
    
    def testBump(self):
        self.sv1.bump('major')
        self.assertTrue(str(self.sv1), 'v2.0.0')
        self.sv1.bump('minor')
        self.assertTrue(str(self.sv1), 'v2.1.0')
        self.sv1.bump('patch')
        self.assertTrue(str(self.sv1), 'v2.1.1')

if __name__ == '__main__':
    unittest.main()
