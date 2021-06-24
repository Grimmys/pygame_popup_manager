import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygamepopup",
    version="0.0.1",
    author="Grimmys",
    author_email="grimmys.programming@gmail.com",
    description="A popup manager for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Grimmys/pygame_popup_manager",
    project_urls={
        "Issue Tracker": "https://github.com/Grimmys/pygame_popup_manager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
    install_requires=["<pygame>"]
)
