from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-CICD-CIRCLECI",
    version="0.1",
    author="Sfgrahman",
    packages=find_packages(),
    install_requires = requirements,
)