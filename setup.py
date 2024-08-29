from setuptools import setup, find_packages

setup(
    name='imageProcessing',
    version='0.1.0',
    author='Emma Viani',
    author_email='emma.i.viani@gmail.com',
    description='A Python library for image processing, including filters, edge detection, and convolution operations. Mainly for my own education on the math behind image processing',
    url='https://github.com/emlambda/imageProcessing',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
