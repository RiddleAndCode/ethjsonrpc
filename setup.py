try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ethjsonrpc',
    version='0.3.1',
    description='Ethereum JSON-RPC client',
    long_description=open('README.rst').read(),
    author='ConsenSys',
    author_email='support@riddleandcode.com',
    url='https://github.com/riddleandcode/ethjsonrpc',
    packages=['ethjsonrpc'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires=[
        'ethereum==1.3.6',
        'requests>=2.9.1',
    ],
)
