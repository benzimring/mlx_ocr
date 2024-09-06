from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlx_ocr",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "mlx",
        "numpy",
        "pillow",
        "requests",
        "transformers"
    ],
    entry_points={
        "console_scripts": [
            "mlx_ocr=ocr.cli:main",
        ],
    },
    python_requires=">=3.6",
)