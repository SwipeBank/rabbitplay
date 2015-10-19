from setuptools import setup
from pip.req import parse_requirements


reqs = parse_requirements('./requirements.txt', session=False)
requirements = [str(x.req) for x in reqs]

setup(
    name="RabbitPlay",
    version="0.4",
    description='A simple abstraction on top of python pika to deal with RabbitMQ.',
    author='Eugene <f0t0n> Naydenov',
    author_email='t.34.oxygen@gmail.com',
    url='https://github.com/TouchBank/rabbitplay',
    install_requires=requirements,
)
