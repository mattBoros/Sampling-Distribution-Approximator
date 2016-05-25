import subprocess
import PATHS


def get_stack_heights(n):
    command = 'java -jar {0} {1} {2}'.format(PATHS.jar, n, PATHS.stack_heights)
    #print(command)
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    out = ''
    while True:
        try:
            out = float(p.stdout.readline())
            break
        except: pass
    return out
