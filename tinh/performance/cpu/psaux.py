import pandas as pd
import sys

f = sys.argv[1]

def psaux(f):
    with open(f, 'r+') as myfile:
        #df_psaux = pd.read_csv(f, names=['USER', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TTY', 'STAT', 'START','TIME', 'COMMAND'], sep=' ')
        df_psaux = pd.read_csv(f)
        print(df_psaux)

def main():
    psaux(f)

if __name__ == '__main__':
    main()
