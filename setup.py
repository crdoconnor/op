import os, sys, re, codecs
from setuptools import setup, find_packages

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = "\n" + "\n".join([read('README.rst'), read('PROJECT.txt')])

setup(name="op",
      version="0.1",
      description="Fast file finder and opener.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
#          'Programming Language :: Python :: 3',
#          'Programming Language :: Python :: 3.1',
#          'Programming Language :: Python :: 3.2',
#          'Programming Language :: Python :: 3.3',
      ],
      keywords='development environment tool git find files editor',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      url='https://github.com/crdoconnor/op',
      license='MIT',
      install_requires=['pyyaml',],
      packages=find_packages(exclude=[]),
      package_data={},
      entry_points=dict(console_scripts=['op=op:cli',]),
      zip_safe=False,
)
