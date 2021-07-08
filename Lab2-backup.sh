#!/bin/bash
sudo mkdir -p /backup
DN=$(echo $1|tr / "\n"|tail -1)
sudo tar -czf /backup/$DN-$(date +%s).tar.gz $1