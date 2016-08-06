import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

requires = [
'setuptools'
]
version = "0.5"

setup(name='core.jet',
      version=version,
      description="some desc",
      license='MIT',
      keywords='extension versions',
      author='wooz',
      classifiers = [
       'Framework :: Buildout',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2.7',
       ],
      packages = find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['core'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires
,entry_points="""
[console_scripts]
myscript = core.jet.somes:say
"""
      )
