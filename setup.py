from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mkdocs-audiotag',
    version='0.0.1',
    author='Anders Eskildsen',
    author_email='dev@anderseskildsen.eu',
    url='https://github.com/aeskildsen/mkdocs-audiotag',
    description='MkDocs plugin for simple audio file embedding',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.6.1'
    ],
    include_package_data=True,
    python_requires='>=3.7',
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-audiotag = mkdocs_audiotag.plugin:AudioTag'
        ]
    }
)