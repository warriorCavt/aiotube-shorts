from setuptools import setup


with open('README.md') as f:
    readme = f.read()


setup(
    name='aiotube-shorts',
    version='1.7.3b',
    description='A library to access YouTube Public Data without YouTubeAPI',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/warriorCavt/aiotube-shorts',
    author='Sougata Jana; forked by warriorCavt',
    author_email='jnsougata@gmail.com; forked by miscwindows@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=['aiotube-shorts'],
    keywords='youtube, youtube-data, youtube-api, youtube-data-api-v3',
    python_requires='>=3.8.0',
    install_requires=['urllib3'],
    project_urls={
        'Documentation': 'https://aiotube.readthedocs.io/en/latest/',
        'Source': 'https://github.com/warriorCavt/aiotube-shorts'
    },
)
