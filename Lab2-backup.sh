sudo mkdir -p /backup
name=`basename $1`
sudo tar -czf /backup/$name-`date +%s`.tar.gz $1
