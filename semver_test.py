#!/usr/bin/env python
import semver
import unittest

class TestSemVer(unittest.TestCase):
    """Semantic Versioning Module Test Class"""

    def setUp(self):
        self.sv1Str = 'v1.2.3-alpha.0+build123-42-g123abcd'
        self.sv1 = semver.SemVer(self.sv1Str)
        self.sv2Str = 'v1.2.3'
        self.sv2 = semver.SemVer(self.sv2Str)
        self.sv3Str = 'v1.2.3-alpha.0+11-gabcd123'
        self.sv3 = semver.SemVer(self.sv3Str)
        self.svMajorBig = semver.SemVer('12.4.2')
        self.svMajorSmall = semver.SemVer('1.5.8')
        self.svMinorBig = semver.SemVer('1.9.4')
        self.svMinorSmall = semver.SemVer('1.4.8')
        self.svPatchBig = semver.SemVer('1.9.13')
        self.svPatchSmall = semver.SemVer('1.9.5')
        self.svPrerelBig = semver.SemVer('2.3.4-beta.2')
        self.svPrerelSmall = semver.SemVer('2.3.4-alpha.0')

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
    
    def testLTMajor(self):
        self.assertTrue(self.svMajorSmall < self.svMajorBig, str(self.svMajorSmall)+" is not smaller than "+str(self.svMajorBig))
        self.assertFalse(self.svMajorBig < self.svMajorSmall, str(self.svMajorBig)+" is less than "+str(self.svMajorSmall))

    def testLTMinor(self):
        self.assertTrue(self.svMinorSmall < self.svMinorBig)
    
    def testLTPatch(self):
        self.assertTrue(self.svPatchSmall < self.svPatchBig)

    def testLTPrerelease(self):
        self.assertTrue(self.svPrerelSmall < self.svPrerelBig)
        self.assertTrue(self.sv3 < self.sv2)
        self.assertFalse(self.sv2 < self.sv3)

    def testEQ(self):
        self.assertTrue(self.sv1 == self.sv3)
        self.assertFalse(self.sv1 == self.sv2)
    
    def testBumpMajor(self):
        self.sv1.bump('major')
        self.assertTrue(str(self.sv1), 'v2.0.0')

    def testBumpMinor(self):
        self.sv1.bump('minor')
        self.assertTrue(str(self.sv1), 'v2.1.0')

    def testBumpPatch(self):
        self.sv1.bump('patch')
        self.assertTrue(str(self.sv1), 'v2.1.1')

    def testBumpPrerel(self):
        self.assertTrue(self.sv1.bump('prerelease'), NotImplemented)

    def testBumpBuild(self):
        self.assertTrue(self.sv1.bump('build'), NotImplemented)

if __name__ == '__main__':
    unittest.main()
