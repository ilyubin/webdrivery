from setuptools import setup

setup(
    name='webdrivery',
    version='0.1',
    description='Python + Webdriver + StructLog',
    url='http://github.com/ilyubin/webdrivery',
    author='Igor Lyubin',
    author_email='igor.lyubin@outlook.com',
    license='MIT',
    packages=[
        'webdrivery'
    ],
    install_requires=[
        'selenium',
        'structlog',
    ],
    tests_require=[
        'pytest'
    ],
    keywords=[
        'selenium',
        'webdriver',
        'structlog'
    ]
)
