from setuptools import setup
from tns import __version__

long_description = open('README.md').read()
desc = """Top News Selectors (tns): Top news parsing from select websites"""

setup(
    name='tns',
    version=__version__,
    url='https://github.com/oduwsdl/top-news-selectors',
    download_url="https://github.com/oduwsdl/top-news-selectors",
    author='Grant Atkins',
    author_email='gatkins@cs.odu.edu',
    description=desc,
    packages=['tns'],
    license='MIT',
    long_description=long_description,
    provides=[
        'tns'
    ],
    install_requires=[
        'beautifulsoup4',
    ],
    tests_require=[
        'pytest'
    ],
    keywords='html web tns odu memento',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)

# Publish to pypi:
#   rm -rf dist; python setup.py sdist bdist_wheel; twine upload dist/*
