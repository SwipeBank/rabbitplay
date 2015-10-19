"""
RabbitPlay
-------------
A simple abstraction on top of pika to deal with RabbitMQ
"""
from setuptools import setup
from pip.req import parse_requirements


reqs = parse_requirements('./requirements.txt', session=False)
requirements = [str(x.req) for x in reqs]

setup(
    name="RabbitPlay",
    version="0.5",
    url='https://github.com/SwipeBank/rabbitplay',
    author='Eugene <f0t0n> Naydenov',
    author_email='t.34.oxygen@gmail.com',
    description='A simple abstraction on top of pika to deal with RabbitMQ.',
    long_description=__doc__,
    py_modules=['rabbitplay'],
    install_requires=requirements,
)
