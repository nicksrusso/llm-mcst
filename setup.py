from setuptools import setup, find_packages

runtime_dependencies = ["ollama"]
test_dependencies = []

setup(
    name='llm-mcst',
    version='0.0.0',
    description='this is a python package',
    author='nick',
    author_email='your.email@example.com',
    install_requires=runtime_dependencies,
    test_requires=test_dependencies,
    packages=find_packages()
)