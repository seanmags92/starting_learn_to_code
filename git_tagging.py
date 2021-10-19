import subprocess
import sys


if len(sys.argv) == 3:
    tag = sys.argv[1]
    commit = sys.argv[2]
    command = f'git tag -a {tag} {commit} -m "{tag}"'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    subprocess.call(command, shell=True)
    subprocess.call('git push --tags', shell=True)
else:
    print('usage: tag.py TAG_NAME COMMIT')
    sys.exit(1)