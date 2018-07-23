# git-herd

A simple command line tool written in Python that lets you clone and pull forks from multiple users.

## Installation
Clone this repo to a location of your choice.

## Setup
Create a `config.py` file with the required variables in the same folder as `git-herd.py`. See `example-config.py` for details.  

_Optional:_ Create an alias in your shell configuration file for convenience.  
For example, add the following to your `.zshrc` or `.bashrc` to run git-herd when typing `herd` into your terminal:
```
alias herd="python3 /your/path/to/git-herd.py"
```

## Usage
Run the `git-herd.py` file (or the command you set up as an alias) and follow the menu prompt.
Make sure you enter any repo names correctly or it won't work.
Assuming the member didn't rename their fork to deviate from the repo name entered (and the other variables in config.py are correct) it should work.
