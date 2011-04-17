try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='webunit2',
    version='0.1',
    description='Eases the testing of web services.',
    author='Andrew McFague',
    author_email='amcfague@wgen.net',
    url='http://pypi.python.org/pypi/webtest2',
    zip_safe=True,
    packages=find_packages(exclude=["ez_setup", "tests"]),
    test_suite='nose.collector',
    install_requires=[
        "httplib2",
        "poster",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
    ],
)
