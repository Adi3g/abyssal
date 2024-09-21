from setuptools import setup, find_packages

setup(
    name='abyssal',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sympy',
        'scipy',
    ],
    test_suite='tests',
    description='A mathematical engine that parses LaTeX expressions and computes advanced mathematical operations such as limits, integrals, logarithms, and more.',
    author='Adib Grouz',
    author_email='contact@adib-grouz.com',
    url='https://github.com/Adi3g/abyssal',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
