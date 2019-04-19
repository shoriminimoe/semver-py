#!/usr/bin/env python

import re
import sys

class SemVer():
    """Semantic Versioning Class"""

    semverRE = re.compile(
            r"""
            ^(?P<prefix>(?:.*))? #TODO This pattern is ambiguous. It needs to check that the first field is not all digits
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
        versionString = '.'.join([str(self.major), str(self.minor), str(self.patch)])
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
        self.major = int(reMatch.group('major'))
        self.minor = int(reMatch.group('minor'))
        self.patch = int(reMatch.group('patch'))
        self.prerelease = reMatch.group('prerelease')
        self.build = reMatch.group('build')

    def __lt__(self, other):
        if self.major < other.major:
            return True
        elif other.major < self.major:
            return False
        elif self.minor < other.minor:
            return True
        elif other.minor < self.minor:
            return False
        elif self.patch < other.patch:
            return True
        elif other.patch < self.patch:
            return False
        elif self.prerelease is None and other.prerelease is not None:
            #TODO This prerelease comparison is not correct.
            #TODO It needs to account for the possible dot-separated 
            #TODO list of fields and also mark letters higher than numbers
            return False
        elif self.prerelease is not None and other.prerelease is None:
            return True
        elif self.prerelease < other.prerelease:
            return True
        elif other.prerelease < self.prerelease:
            return False
        else:
            return False
    
    def __eq__(self, other):
        if self.major == other.major \
                and self.minor == other.minor \
                and self.patch == other.patch \
                and self.prerelease == other.prerelease:
            return True
        else:
            return False
        
    def bump(self, partString):
        if partString == 'major':
            self.major += 1
            self.minor = 0
            self.patch = 0
            self.prerelease = None
            self.build = None
        elif partString == 'minor':
            self.minor += 1
            self.patch = 0
            self.prerelease = None
            self.build = None
        elif partString == 'patch':
            self.patch += 1
            self.prerelease = None
            self.build = None
        elif partString == 'prerelease' or partString == 'build':
            return NotImplemented
        else:
            raise

