#! usr/bin/env python3
#-*- coding:utf-8 -*-

import argparse, io, os, sys

parser = argparse.ArgumentParser()
# parser.add_argument('account', help='the account of GITHUB')
parser.add_argument('repository', help='name of the repository')
args = parser.parse_args()

cmd1 = 'git init'
cmd2 = 'git remote add origin git@github.com:xrun0213/{0}.git'.format(args.repository)

msg = '&'.join( (cmd1, cmd2) )
os.system(msg)


###
#git pull [remote] [branch]
#git push [remote] master:[branch]