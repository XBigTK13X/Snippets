##Purpose
This python script wraps rsync and makes it easy to add backup targets.
It is by no means a secure setup or backup, but it is very simple to configure and restore backups.
Only 1 backup is taken per sync, and it is an uncompressed 1 to 1 file copy.
This script assumes the hostname of the backup server is 'archer'.


## Configuring Backups
Setup is as follows:
####Client
1) Install Python 2.7+ and rsync on client
2) Run sudo su - to become root
3) Generate a passwordless RSA keypair for the root user
4) ssh-copy-id -i ~/.ssh/id_rsa.pub bup@archer
5) Enter password for bup to confirm the copy
6) Copy the files backup.py, syncs, and user to '''/usr/local/bin/bup'''
7) Edit syncs to contain any directories you want backed up '''/client/path:::/server-backup-name'''
8) Edit user to be your user's id
9) Edit the root user's crontab '''sudo crontab -e'''
10) Add this line '''@hourly cd /usr/local/bin/bup; python backup.py b'''

From time to time, manually run python backup.py b-c to remove files that were previously backed up, but you don't want kept on the server

###Server
1) Install an SSH server on a computer that will host the backups
2) Create a new user, 'bup'
3) Give the user a password
4) Create a /home/bup directory for the user
5) Create a directory '/bup'
6) Give bup ownership of /bup

## Restoring Backups
1) Run python backup.py r to retrieve any missing files
2) Run python backup.py r-c to retrieve any missing files and delete local files not present on the server
