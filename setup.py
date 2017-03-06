"""
Setup module.
"""
import re
from os.path import join as pjoin
from setuptools import setup


with open(pjoin('markdownreveal', '__init__.py')) as f:
    line = next(l for l in f if l.startswith('__version__'))
    version = re.match('__version__ = [\'"]([^\'"]+)[\'"]', line).group(1)

setup(
    name='markdownreveal',
    version=version,
    description='TODO',  # TODO
    long_description='''TODO.''',  # TODO
    url='https://github.com/peque/markdownreveal',
    author='Miguel Sánchez de León Peque',
    author_email='peeque@neosit.es',
    license='BSD License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='markdown reveal reveal.js presentation',
    scripts=['bin/markdownreveal'],
    packages=['markdownreveal'],
    package_data={'markdownreveal': ['config.template.yaml']},
    install_requires=[
        'PyYAML',
        'requests',
        'pypandoc',
        'livereload',
        'watchdog'],
    extras_require={
        'dev': [],
        'test': ['tox'],
        'docs': ['sphinx', 'numpydoc', 'sphinx_rtd_theme'],  # TODO
    },
)
