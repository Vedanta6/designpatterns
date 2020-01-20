from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='designpatterns',
    version='1.0.1',
    description='design patterns',
    url='https://github.com/Vedanta6/designpatterns',
    author='Vedanta6',
    author_email='',
    package_dir={'': 'patterns/strategy'},
    packages=find_packages(where='patterns/strategy'),
    install_requires=requirements,
    scripts=[
        'patterns/strategy',
    ]
)
