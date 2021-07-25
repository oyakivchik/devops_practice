#!/bin/bash
rename=$(basename -- $1)
rename=$rename'-'$(date +%s)

`mkdir -p backup`
`tar -czf backup/$rename.tar.gz $1`