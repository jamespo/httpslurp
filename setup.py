"""
Dump HTTP requests to filesystem
"""
from setuptools import find_packages, setup
from httpslurp.version import __version__

dependencies = ['sanic', 'pyxdg', 'aiohttp']

setup(
    name='httpslurp',
    version=__version__,
    url='https://github.com/jamespo/httpslurp',
    license='MIT',
    author='James Powell',
    author_email='jamespo@gmail.com',
    description='Dump HTTP requests to filesystem',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    # scripts=['scripts/httpslurp'],
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'httpslurp = httpslurp.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
