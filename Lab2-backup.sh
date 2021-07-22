#!/bin/bash
url=$1
# What to backup. 
backup_files='/'$url

# Where to backup to.
dest="/home/oleh/backup"

# Create archive filename.

timestamp=$(date +%s)
archive_file="url-$timestamp.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls -lh $dest
