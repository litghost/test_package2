import setuptools

setuptools.setup(
    name="test_package2",
    version="0.0.1",
    author="litghost",
    description="",
    url="https://github.com/litghost/test_package2",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
