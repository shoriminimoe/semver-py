#!/usr/bin/env python

import re
import sys

class SemVer():
    """Semantic Versioning Class"""

    semverRE = re.compile(
            r"""
            ^(?P<prefix>(?:.*))
            (?P<major>(?:0|[1-9]\d*))\.
            (?P<minor>(?:0|[1-9]\d*))\.
            (?P<patch>(?:0|[1-9]\d*))
            (\-(?P<prerelease>
                (?:0|[0-9A-Za-z-][0-9A-Za-z-]*)
                (\.(?:0|[0-9A-Za-z-][0-9A-Za-z-]*))*
            ))?
            (\+(?P<build>[0-9A-Za-z-]+(\.[0-9A-Za-z]+)*))?
            """, re.VERBOSE)

    def __init__(self, instr=None):
        self.parse(instr)

    def __str__(self):
        versionString = '.'.join([self.major, self.minor, self.patch])
        if self.prerelease:
            versionString += '-' + self.prerelease
        if self.build:
            versionString += '+' + self.build
        return versionString

    def tag(self):
        return self.prefix + str(self)

    def parse(self, instr):
        reMatch = self.semverRE.match(instr)
        self.prefix = reMatch.group('prefix')
        self.major = reMatch.group('major')
        self.minor = reMatch.group('minor')
        self.patch = reMatch.group('patch')
        self.prerelease = reMatch.group('prerelease')
        self.build = reMatch.group('build')

    #TODO 
    #def __lt__(self, other):
    #def __eq__(self, other):
    #def __hash__(self):
        #return hash((
            #self.prefix,
            #self.major,
            #self.minor,
            #self.patch,
            #self.prerelease,
            #self.build))
