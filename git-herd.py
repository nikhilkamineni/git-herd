import subprocess
import sys
from config import MEMBERS, BASE_URL, ROOT_DIR

arguments = sys.argv[1:]
running = True
history = []


def clone_repos(repo_name):
    add_to_history(repo_name)

    commands = []
    for member in MEMBERS:
        repo_url = f'{BASE_URL}/{MEMBERS[member]}/{repo_name}.git'
        repo_dest = f'{ROOT_DIR}/{member}/{repo_name}'
        commands.append(f'git clone {repo_url} {repo_dest}')
    command = ';'.join(commands)
    subprocess.call(command, shell=True)


def pull_repos(repo_name):
    add_to_history(repo_name)

    commands = []
    for member in MEMBERS:
        sub_dir = f'{ROOT_DIR}/{member}/{repo_name}'
        commands.append(f'cd {sub_dir}')
    command = ';git pull;'.join(commands) + ';git pull'
    subprocess.call(command, shell=True)


def add_to_history(repo_name):
    """Add repo_name to history and limit to 5 items"""
    if repo_name in history:
        history.remove(repo_name)

    history.insert(0, repo_name)

    if (len(history) == 11):
        del history[19]


if len(arguments) is 0:
    while running:
        print('')
        print('  # # # # # # # # # # # # # # # #')
        print('  #                             #')
        print('  #  c: clone a projects repos  #')
        print('  #  p: pull all repos          #')
        print('  #                             #')
        print('  #  m: view members            #')
        print('  #  r: view root directory     #')
        print('  #                             #')
        print('  #  q: quit                    #')
        print('  #                             #')
        print('  # # # # # # # # # # # # # # # #')
        print('')
        choice = input('>>> ')

        """Clone all repos"""
        if choice == 'c':
            repo_name = input('enter repo name: ')

            if repo_name == 'q':
                running = False

            if repo_name == 'b':
                continue

            clone_repos(repo_name)

        """Pull all repos"""
        if choice == 'p':
            print('')
            print('  History:')
            if history:
                for i, item in enumerate(history):
                    print(f'    {i}: {item}')
            else:
                print('    empty history')
            print('')

            if history:
                print('    0-9: pull repo from history list')
            print('    b: back')
            print('    q: quit\n')

            repo_name = input('enter repo name: ')

            # If input is a digit use corresponding item in history
            if repo_name.isdigit():
                if int(repo_name) > 9:
                    print('')
                    print('Invalid input')
                else:
                    pull_repos(history[int(repo_name)])
            else:
                if repo_name == 'q':
                    running = False
                elif repo_name == 'b':
                    continue
                else:
                    pull_repos(repo_name)

        """View Members"""
        if choice == 'm':
            print('')
            print('  Members: ')
            for i, member in enumerate(MEMBERS):
                print(f'    {i}: {member}')
            print('')

        """View root directory"""
        if choice == 'r':
            print('')
            print('Root directory: ', ROOT_DIR)
            print('')
        if choice == 'q':
            running = False

