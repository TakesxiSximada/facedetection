import os
import re

from setuptools import setup, find_packages


def here(name):
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        name)


def read(name, mode='rb', encoding='utf8'):
    with open(here(name), mode) as fp:
        return fp.read().decode(encoding)


def get_version_str(file_path):
    version_file = read(file_path)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise ValueError("Unable to find version string.")


def find_version(path, pattern='.*\.py$'):
    regx = re.compile(pattern)
    for root, dirs, files in os.walk(path):  # 3.5... orz
        for filename in files:
            filepath = os.path.join(root, filename)
            if regx.match(filepath):
                try:
                    return get_version_str(filepath)
                except ValueError:
                    pass  # next
    else:
        raise ValueError('Version file not found: {}'.format(path))


setup(
    name='facedetection',
    version=find_version('src'),
    license='Apache License 2.0',
    description='The facial recognition',
    long_description=read('README.rst'),
    url='https://github.com/TakesxiSximada/facedetection',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
    author='TakesxiSximada',
    author_email='sximada+facedetection@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'furl',
        'requests',
        'zope.interface',
        'oauth2client',
        'google-api-python-client',
        'pillow',
    ],
    entry_points="""\
    [console_scripts]
    """,
)
