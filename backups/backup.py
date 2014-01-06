from subprocess import call
from sys import argv
from sys import exit

u=open('user').read().strip()

syncs={}
for line in open('syncs').readlines():
    l,r = line.split(':::')
    syncs[l]=r



def backup(user,local,remote):
    call(["sudo","-H","rsync","-arz",local,"bup@archer:/bup/"+user+"/"+remote])

def restore(user,local,remote):
    call(["sudo","-H","rsync","-arz","bup@archer:/bup/"+user+"/"+remote,local])

def cleanremote(user,local,remote):
    call(["sudo","-H","rsync","-arz","--del",local,"bup@archer:/bup/"+user+"/"+remote])

def cleanlocal(user,local,remote):
    call(["sudo","-H","rsync","-arz","--del","bup@archer:/bup/"+user+"/"+remote,local])

def usage():    
    print "Usage: python backup.py <mode>"
    print "<mode>: The operation to perform, valid inputs:"
    print "\tb - Copy files from local syncs to remotes"
    print "\tr - Copy files from remote syncs to local"
    print "\tb-c - Copy files from local to remote, delete remote files that no longer exist on local"
    print "\tr-c - Copy files from remote to local, delete local files that no longer exist on remote."

if len(argv) == 1:
    usage()
    exit()

mode = argv[1]
failed = False
for sync in syncs:
    l = sync
    r = syncs[sync]
    if mode == "b":
        backup(u,l,r)
    elif mode == "r":
        restore(u,l,r)
    elif mode == "b-c":
        cleanremote(u,l,r)
    elif mode == "r-c":
        cleanlocal(u,l,r)
    else:
        failed = True

if failed:
    usage()
