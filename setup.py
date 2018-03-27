import setuptools

import pynucamino

setuptools.setup(
    name="pynucamino",
    version=pynucamino.__version__,
    packages=setuptools.find_packages(),
    author="Nathaniel Knight",
    author_email="nknight@cfenet.ubc.ca",
    description=(
        "Python bindings to nucamino, A nucleotide to amino acid alignment "
        "program optimized for virus gene sequences."
    ),
    license="MIT",
    url="https://github.com/hcv-shared/pynucamino",
    python_requires=">=2.7,<3.7",
    test_suite="test",
    zip_safe=False,
)
