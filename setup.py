from setuptools import setup, find_packages
from pathlib import Path

# Read README.md if present (won't crash if it's missing)
readme_path = Path(__file__).parent / "README.md"
long_desc = readme_path.read_text(encoding="utf-8") if readme_path.exists() else (
    "Inventory management library providing EOQ, ROP, Safety Stock, Total Cost, and Bulk-Discount EOQ."
)

setup(
    name="inventorylib",  # Change only if you pick a different package name for PyPI
    version="0.1.0",      # Use semantic versions: MAJOR.MINOR.PATCH
    description="Inventory management library (EOQ, ROP, Safety Stock, Total Cost, Bulk Discount EOQ)",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="Avni Gupta, Samruddhi Jain, Pranav Mantri",
    author_email="guptavni001@gmail.com, samruddhij1603@gmail.com, author3@example.com",
    url="",  # optional; add your GitHub repo URL later if you make one
    packages=find_packages(exclude=("tests", "docs", "examples")),
    install_requires=[],  # add deps here if you ever need them
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
