#!/usr/bin/env python3

import re

class Version:

    def __init__(self, nums: str):
        self.nums = nums
        m = re.search(r'^(\d+)\.(\d+)\.(\d+)$', nums)
        if m:
            self.major = int(m.group(1))
            self.minor = int(m.group(2))
            self.patch = int(m.group(3))
        else:
            raise ValueError('Your version number must consist of three numbers')

    def __str__(self):
        return self.nums

    def __gt__(self, other):
        '''Checks if an object has a newer version than its counterpart.
        Returns True or False'''
        if self.major > other.major:
            return True
        elif self.minor > other.minor:
            return True
        elif self.patch > other.patch:
            return True
        else:
            return False

    def __ge__(self, other):
        '''Checks if an object has a newer or the same version as
         its counterpart. Returns True or False'''
        if self.major == other.major and self.minor == other.minor \
        and self.patch == other.patch:
            return True
        elif self.major > other.major:
            return True
        elif self.minor > other.minor:
            return True
        elif self.patch > other.patch:
            return True
        else:
            return False

    def __lt__(self, other):
        '''Checks if an object has an older version than its counterpart.
        Returns True or False'''
        if self.major < other.major:
            return True
        elif self.minor < other.minor:
            return True
        elif self.patch < other.patch:
            return True
        else:
            return False

    def __le__(self, other):
        '''Checks if an object has an older or the same version as
         its counterpart. Returns True or False'''
        if self.major == other.major and self.minor == other.minor \
        and self.patch == other.patch:
            return True
        elif self.major < other.major:
            return True
        elif self.minor < other.minor:
            return True
        elif self.patch < other.patch:
            return True
        else:
            return False

    def __eq__(self, other):
        '''Checks if an object has the same version as its counterpart.
        Returns True or False'''
        if self.major == other.major and self.minor == other.minor \
        and self.patch == other.patch:
            return True
        else:
            return False

print(Version('1.1.3') < Version('2.2.3'))
print(Version('45.22.16') < Version('45.22.16'))
print(Version('10.10.3') <= Version('10.10.2'))
print(Version('100.10.3') >= Version('10.10.2'))
print(Version('1.1.3') == Version('1.1.3'))
print(Version('1.1.3') > Version('2.2.3'))
print(Version('cat') < Version('2.2.3'))
