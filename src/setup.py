from setuptools import setup, setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

import STOC

setup(name='STOC',
      description='code for the BAMS STOC',
      url='https://github.com/nicolasfauchereau/BAMS_STOC_2022',
      author='Nicolas Fauchereau',
      author_email='Nicolas.Fauchereau@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["tests", "docs"]),
      version=STOC.__version__, 
      zip_safe=False)


