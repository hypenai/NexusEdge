from setuptools import setup, find_packages
setup(
    name='nexusedge',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow-federated'
    ],
)
