from setuptools import setup, find_packages

setup(
    name="griffin-llm",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'transformers>=4.30.0',
        'torch>=2.0.0',
        'sentencepiece>=0.1.99'
    ],
    extras_require={
        'gpu': ['cuda-toolkit>=11.7']
    }
)
