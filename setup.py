from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(name='python-openpose',
      version='1.0.0',
      description='OpenPose for Pypi',
      author='Whitey',
      url='https://www.python.org/',
      license='MIT',
      keywords='openpose',
      packages=['openpose'],
      install_requires=[],
    include_package_data=True,
    package_data={'openpose':['*.pyd']},
      python_requires='>=3'
     )
