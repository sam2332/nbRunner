import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nbRunner',  
     version='0.6',
     scripts=['nbRunner'] ,
     author="Sam Rudloff",
     author_email="sam.rudloff@gmail.com",
     description="Simple jupyter Notebook Runner that shows cell output",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sam2332",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
