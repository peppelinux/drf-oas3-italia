from glob import glob
from setuptools import find_packages, setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='drf_italia',
      version='0.2.0',
      description=('Django Rest Framework italia OpenAPIv3'),
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
                  'Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: GNU Affero General Public License v3',
                  'Programming Language :: Python :: 3 :: Only',
                  'Operating System :: POSIX :: Linux'
                  ],
      url='https://github.com/peppelinux/drf-oas3-italia',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='AGPL-3.0',
      packages=find_packages(),
      #  package_data={'': ['*.html']},
      #  data_files=[
        #  ('', glob('somewhere/templates/*/*/*.html')),
      #  ],
      include_package_data=True,
      install_requires=[
                      'Django>3,<4',
                      'rest_framework',
                  ],
     )
