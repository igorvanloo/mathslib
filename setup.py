from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

requirements = ['math', ]

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name = "mathslib",  # Required
    version="1.0.0",  # Required
    description="Library of Mathematical functions and Algorithms",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    url="https://github.com/igorvanloo/mathslib",  # Optional
    author="Igor van Loo",  # Optional
    author_email="igorvanloo@gmail.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        # Pick your license as you wish
        "License :: Unlicense",
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords="numbertheory, maths, algorithms",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    install_requires=requirements,
    python_requires=">=3.7, <4",
    entry_points={  # Optional
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/igorvanloo/mathslib/issues",
        "Source": "https://github.com/igorvanloo/mathslib",
    },
)

