import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name='procyon',
      version='0.0',
      description='procyon is a lightweight framework for pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Nozomu Kaneko',
      author_email='nozom.kaneko@gmail.com',
      url='',
      keywords='web pyramid pylons',
      package_dir={"": "src"},
      packages=find_packages("src"),
      include_package_data=True,
      zip_safe=False,
      install_requires=["pyramid"],
      test_suite="procyon",
      )
