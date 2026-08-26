## Project requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A sample `pygame-ce` (or `pygame`) project to include the library in

## Build

To build a dev version of the library, run:

```bash
uv build
```

## Install dev build to a local project

Once you have created a dev build containing your own changes for the library,
you can install it to a local project for verifying the changes using:

```bash
# uv project
uv pip install --reinstall ./pygame_popup-<version>-py3-none-any.whl

# pip project
python -m pip install ./pygame_popup-<version>-py3-none-any.whl
```

Where `pygame_popup-<version>-py3-none-any.whl` is the file extracted 
from the `dist` folder generated as part of the build.

You may have to uninstall the existing version of the library before installing the dev build.

## Execute tests

After making your changes, it's always nice to verify the existing test suite is still green.
You can do so by running the following command:

```bash
uv run pytest
```

## Generate docs

A local version of the Sphinx documentation can be generated to verify your changes are properly reflected 
on the library documentation (if applicable):

```bash
uv run --group docs sphinx-build -M html docs/source docs/build
```

Documentation files will be generated under `docs/build` as specified in the command.
Open `docs/build/html/index.html` file in your favorite browser to explore the new version.