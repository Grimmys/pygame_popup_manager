import setuptools

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="pygame_popup",
    version="0.11.2",
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
        "Operating System :: OS Independent",
    ],
    license="GPL-3.0-or-later",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={"": ["images/*.png"]},
    python_requires=">=3.12",
    install_requires=["pygame-ce>=2.0.0"],
)
