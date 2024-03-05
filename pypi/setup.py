from setuptools import setup, find_packages
import io

with io.open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()
    

# py -m build
# py -m twine upload --config-file .pypirc  --repository testpypi dist/*

setup(
    name='higher_institutions_ng',
    version='0.0.3',
    packages=find_packages(where='src', exclude=['tests']),
    package_dir={'': 'src'},
    package_data={
        'higher_institutions_ng': ['*.json'],
    },
    include_package_data=True,
    exclude=[".pre-commit-config.yaml", "mypy.ini", "tests"],
    author='Awesome Goodman',
    author_email='goodman.awesome@gmail.com',
    description='Information about Nigerian higher institutions.',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    keywords=[
    "Nigerian School List",
    "Nigerian Schools",
    "Nigerian Colleges",
    "Nigerian Universities",
    "Nigerian Polytechnics",
    "Nigerian Higher Institutions",
    "State", 
    "Federal",
    "Nigeria"
  ],
    url='https://github.com/awesomegoodman/higher-institutions-ng/tree/main/pypi',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        'Operating System :: OS Independent',
    ],
    install_requires=[]
)
