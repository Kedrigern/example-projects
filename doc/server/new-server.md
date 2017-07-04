
# Nový server

CentOS 7

SSH s vynuceným heslem:

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@example.com
```

SSH bez hesla (hesla nepoužíváme):

```bash
visudo                 # Edit to stop ask for password
systemctl restart sshd # Restart sshd service
```

Nový user:
```bash
adduser username      # Create user
passwd username       # Set password for the user (can be omited when set the ssh key)
usermod -aG wheel username # Grant sudo to this user
```

SSH klíč:

a) `ssh-copy-id` snadno nahraje klíč pro lokálního uživatele. S parametrem `-i <key>` umožní nahrát i jiný klíč.
b) Ručně:
```bash
# /home/<user>
mkdir .ssh
chmod 700 .ssh
vim .ssh/authorized_keys
chmod 600 .ssh/authorized_keys
```

SSH zákaz nebezpečných přístupů:
```bash
vim /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no
systemctl restart sshd
```
