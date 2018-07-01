make changes to `/etc/security/limits.conf`

before `# End of file` add:  
```
* hard nofile 20000
* soft nofile 20000
```