from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="swapnil sonawane",
    description="A small package for dvc dl pipline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/This-swapnil/DVC_DL_Tensorflow_demo",
    author_email="sswapnil0098@gmail.com",
    packages=["src"],
    license="GNU",
    python_requires=">=3.7",
    install_requires=['tensorflow','matplotlib','numpy', 'pandas','tqdm','PyYAML', 'dvc', 'boto3'])