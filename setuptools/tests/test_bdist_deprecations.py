"""develop tests
"""
import mock

import pytest

from setuptools.dist import Distribution
from setuptools import SetuptoolsDeprecationWarning


class Test:
    @mock.patch("distutils.command.bdist_rpm.bdist_rpm")
    def test_bdist_rpm_warning(self, user_override):
        dist = Distribution(dict(
            script_name='setup.py',
            script_args=['bdist_rpm'],
            name='foo',
            py_modules=['hi'],
        ))
        dist.parse_command_line()
        with pytest.warns(SetuptoolsDeprecationWarning):
            dist.run_commands()

    @mock.patch("distutils.command.bdist_wininst.bdist_wininst")
    def test_bdist_wininst_warning(self, user_override):
        dist = Distribution(dict(
            script_name='setup.py',
            script_args=['bdist_wininst'],
            name='foo',
            py_modules=['hi'],
        ))
        dist.parse_command_line()
        with pytest.warns(SetuptoolsDeprecationWarning):
            dist.run_commands()
