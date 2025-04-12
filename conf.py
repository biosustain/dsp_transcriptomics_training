# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Data Science Platform notes template"
copyright = "2024, DTU Biosustain, Informatics Platform, DSP"
author = "Henry Webel"


# -- General configuration ---------------------------------------------------


extensions = [
    "myst_nb",
    # "sphinx_design", # https://sphinx-design.readthedocs.io/en/sbt-theme/
    # "sphinx_copybutton", # https://sphinx-copybutton.readthedocs.io/
    "sphinx_new_tab_link",
]

templates_path = ["_templates"]
# As we can use percent notebooks and markdowns files, we need to exclude some files
# additinally to the default ones (add to the list if needed)
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    '.venv/*',
    "README.md",
    "**/.ipynb_checkpoints/*",
    "jupyter_execute",
    "conf.py",
]


# -- Notebook related settings -----------------------------------------------

# add notebooks
#  https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "auto"

myst_enable_extensions = ["dollarmath", "amsmath"]

# Plolty support through require javascript library
# https://myst-nb.readthedocs.io/en/latest/render/interactive.html#plotly
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
]

# https://myst-nb.readthedocs.io/en/latest/configuration.html
# Execution
nb_execution_raise_on_error = True
# Rendering
nb_merge_streams = True

# https://myst-nb.readthedocs.io/en/latest/authoring/custom-formats.html#write-custom-formats
nb_custom_formats = {
    ".py": ["jupytext.reads", {"fmt": "py:percent"}]
}


# -- Options for HTML output -------------------------------------------------

# 2. Select a tempalate
# ! you might need additional dependencies in requirements.txt
# browse available themes: https://sphinx-themes.org/


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# See:
# https://github.com/executablebooks/MyST-NB/blob/master/docs/conf.py
# html_title = ""
html_theme = "sphinx_book_theme"
# html_theme = "sphinx_book_theme" # alternative
# html_logo = "_static/logo-wide.svg"
# html_favicon = "_static/logo-square.svg"
html_theme_options = {
    "github_url": "https://github.com/enryh/",
    "repository_url": "https://github.com/enryh/notes_template",
    # "repository_branch": "main",
    # "home_page_in_toc": True,
    # "path_to_docs": "docs",
    "show_navbar_depth": 1,
    # "use_edit_page_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "launch_buttons": {
        "colab_url": "https://colab.research.google.com"
        #     "binderhub_url": "https://mybinder.org",
        #     "notebook_interface": "jupyterlab",
    },
    "navigation_with_keys": False,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
