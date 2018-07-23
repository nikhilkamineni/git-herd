import subprocess
import sys
from config import *

arguments = sys.argv[1:]
running = True


def add_member(name, username):
    members[name] = username


def clone_repos(repo_name):
    commands = []
    for member in MEMBERS:
        repo_url = f'{BASE_URL}/{MEMBERS[member]}/{repo_name}.git'
        repo_dest = f'{ROOT_DIR}/{member}/{repo_name}'
        commands.append(f'git clone {repo_url} {repo_dest}')
    command =';'.join(commands)
    subprocess.call(command, shell=True)


def pull_repos(repo_name):
    commands = []
    for member in MEMBERS:
        sub_dir = f'{ROOT_DIR}/{member}/{repo_name}'
        commands.append(f'cd {sub_dir}')
    command = ';git pull;'.join(commands)
    subprocess.call(command, shell=True)


if len(arguments) is 0:
    while running:
        print('')
        print('  c: clone a projects repos')
        print('  p: pull all repos')
        print('')
        print('  m: view members')
        print('  r: view root directory')
        print('')
        print('  q: quit')
        print('')
        choice = input('>>> ')

        if choice == 'c':
            repo_name = input('enter repo name: ')
            clone_repos(repo_name)
        if choice == 'p':
            repo_name = input('enter repo name: ')
            pull_repos(repo_name)
        if choice == 'm':
            print('')
            print('Members: ', MEMBERS)
            print('')
        if choice == 'r':
            print('')
            print('Root directory: ', ROOT_DIR)
            print('')
        if choice == 'q':
            running = False

