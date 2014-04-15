These scripts allow a samba share to be used as a Time Machine volume.

1. Create the samba share
2. Mount the share from the client mac
3. Make sure that you have write access
4. Run `ls /Volumes` to get the mounted share's path
5. Run `makeImage.sh <sizeInGB> <mountedsharepath>`
6. Double click the spare bundle in your mounted network share (this mounts the bundle)
7. Run `useImage.sh` to set the network shared bundle as the active Time Machine store

This information was collected from various blog posts, most of which referenced [this forum](http://www.insanelymac.com/forum/topic/184462-guide-106-snow-leopard-time-machine-backup-to-network-share/) (the original source of the script). I didn't like that the files are behind a registration wall, and the risk of link-rot. The first updated post of that thread is also preserved here as a complete webpage.
