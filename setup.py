from setuptools import setup

__version__ = '3.1.5'

setup(
    name='pytify',
    version=__version__,
    description='Spotify remote. Search, start and navigate through songs.',
    long_description='https://github.com/bjarneo/pytify',
    url='https://github.com/bjarneo/pytify',
    download_url='https://pypi.python.org/pypi/pytify',
    author='Bjarne Oeverli',
    author_email='bjarne.oeverli@gmail.com',
    license='MIT',
    keywords='spotify pytify song search curses',
    packages=['pytify'],
    install_requires=[
        'requests>=2.4.3',
        'prompt-toolkit==1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'pytify=pytify.cli:main'
        ]
    },
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Terminals',
    ],
)
