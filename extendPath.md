# the PATH env variable is extended in the file ~/.profile and not in .zshrc so it is not only available in the zsh

# add ~/.local/bin to PATH so pylint and autopep8 for vs code is usable
# in ~/.local/bin all pip packages which are installed with the --user flag for 'pip install' are installed
export PATH=$PATH:~/.local/bin
