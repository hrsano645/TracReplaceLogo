# coding: utf-8

from setuptools import find_packages, setup

# name can be any name.  This name will be used to create .egg file.
# name that is used in packages is the one that is used in the trac.ini file.
# use package name as entry_points
setup(
    name='ReplaceLogo',
    version='0.1',
    description = 'Replace the project name with Trac logo',
    license = 'BSD',
    url = 'http://hr-sano.net/blog/',
    author = 'hiroshi sano',
    author_email = 'hrs.sano645@gmail.com',

    packages=find_packages(exclude=['*.tests*']),
    entry_points = """
        [trac.plugins]
        replacelogo = replacelogo
    """,
    package_data={'replacelogo': [
                                'htdocs/js/*'
                                ]},
)
