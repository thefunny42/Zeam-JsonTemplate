from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '0.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('src', 'zeam', 'jsontemplate', 'test_jsontemplate.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='zeam.jsontemplate',
    version=version,
    description="Fanstatic packaging of json template",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic jsontemplate',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    package_dir={'': 'src'},
    namespace_packages=['zeam'],
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jsontemplate = zeam.jsontemplate:library',
            ],
        },
    )
