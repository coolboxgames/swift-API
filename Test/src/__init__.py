"""
StackSync API WEB module for OpenStack Swift
"""

__all__ = ['version_info', 'version']

#: Version information ``(major, minor, revision)``.
version_info = (2, 0, 0)
#: Version string ``'major.minor.revision'``.
version = '.'.join(map(str, version_info))