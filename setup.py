from setuptools import setup

setup(name='pytest-html',
      version='1.7.1',
      description='pytest plugin for generating HTML reports',
      long_description=open('README.rst').read(),
      author='Dave Hunt',
      author_email='dhunt@mozilla.com',
      url='https://github.com/davehunt/pytest-html',
      packages=['pytest_html'],
      package_data={'pytest_html': ['resources/*']},
      entry_points={'pytest11': ['html = pytest_html.plugin']},
      install_requires=['pytest>=2.3'],
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest html report',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'])
