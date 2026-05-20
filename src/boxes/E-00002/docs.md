# E-00002 Binary is jacked 

## Summary

Uh oh, looks like a backup script used to run via a path variable. Except, it was deleted and some misconfiguration happened : / 

## Vuln

1. tmp in path
2. relative binary path 

## Chain

1. create malicious compress binary in /tmp/compress
2. check for /tmp/flag.txt after every run
