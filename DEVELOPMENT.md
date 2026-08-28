## Project requirements

- Python 3.14 or above
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A sample `pygame-ce` (or `pygame`) project to include the library in

## Use the development version in a local project

For ongoing development, install the source tree as an editable dependency in
the consuming project:

```bash
# uv project (run this from the consuming project's directory)
uv add --editable /path/to/pygame_popup_manager

# pip project
python -m pip install ./pygame_popup-<version>-py3-none-any.whl
```

The editable uv dependency records the local source in the consuming project's
`pyproject.toml` and remains installed after syncing or restarting the project, 
by handling the build of the library automatically.

To switch back to the production version afterwards, run this from the consuming
project's directory:

```bash
uv remove pygame-popup
uv add pygame-popup
```

For pip projects, build the wheel first with `uv build`; the wheel is generated
in the `dist` folder.

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
Open `docs/build/html/index.html` file in your favorite browser to explore this documentation.
