# FTP

## vsftpd

Config: `/etc/vsftpd.conf`

### Own users
Use own (apache like) user instead of unix user.

Package: `libpam-pwdfile`

In `/etc/vsftpd.conf`:
```
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
anon_upload_enable=NO
anon_mkdir_write_enable=NO
dirmessage_enable=YES
connect_from_port_20=YES
xferlog_enable=YES
xferlog_std_format=YES
xferlog_file=/var/log/xferlog
nopriv_user=ftp
check_shell=NO
chroot_local_user=YES
dual_log_enable=YES
# Pri background=yes nelze resetovat daemona pres initscript
background=NO
listen=YES
text_userdb_names=YES
use_localtime=YES
userlist_enable=YES
userlist_file=/etc/vsftpd.banned
banner_file=/etc/ftpbanner
pam_service_name=vsftpd
guest_enable=YES
guest_username=www-data
virtual_use_local_privs=YES
user_config_dir=/etc/vsftpd/users
force_dot_files=YES
tcp_wrappers=YES
```

Password is set by: 
```
htpasswd -d /etc/vsftpd/passwd [username]
```

And you need user list or banned user list: `touch /etc/vsftpd.banned`

Users config in dir: `/etc/vsftpd`, passwords `/etc/vsftpd/passwd` (http auth format). In `/etc/vsftpd/users/[name]` is config for given user. For example:
```
cat /etc/vsftpd/users/joe
local_root=/var/ftp/joeplace
```


### Links
http://howto.gumph.org/content/setup-virtual-users-and-directories-in-vsftpd/
