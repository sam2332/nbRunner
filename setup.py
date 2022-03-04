import setuptools
from setuptools.command.install import install
from subprocess import getoutput

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    long_license = fh.read()

class PostInstall(install):
    pkgs = 'git+https://github.com/sam2332/nbparameterise.git'
    def run(self):
        install.run(self)
        print(getoutput('pip uninstall nbparameterise -y'))
        try:
            print(getoutput('pip install '+self.pkgs))
        except Exception as e:
            print(getoutput('pip install nbparameterise'))

setuptools.setup(
    name='nbRunner',  
    version='0.9.6',
    scripts=['nbRunner'] ,
    author="Sam Rudloff",
    author_email="sam.rudloff@gmail.com",
    description="Simple jupyter Notebook Runner that shows cell output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sam2332/nbRunner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    License=long_license,
    install_requires=[
        'argparse',
        'nbformat',
        'nbclient'
    ],
    cmdclass={'install': PostInstall}
)
