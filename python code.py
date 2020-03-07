import sys
import time
import paramiko
import getpass
 
my_id = 'johnsmith'
my_password = getpass.getpass('Password:')
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
out_file = open('connection_results.txt','w')
in_file = open('list_of_servers.txt', 'r') 
for host in in_file: 
      host=host.strip()
      print ("Checking server",host)
      
      try:
            ssh.connect(host, username=my_id, password=my_password)
            terminal = ssh.invoke_shell()
            terminal.send('junk')
            terminal.send('\n')
            time.sleep(5)
            print (terminal.recv(9999).decode('utf-8'))
      
            command = 'hostname'
            (stdin, stdout, stderr) = ssh.exec_command(command)
            for line in stdout.readlines():
                  print ("Connected to",line)
                  out_file.write("connected to " + line + "\n")
    
            terminal.send('exit')
            terminal.send('\n')
            time.sleep(5)
      
            ssh.close()
 
      except:
            out_file.write("Could not connect to " + host + "\n")
            
 
in_file.close()
out_file.close()

===============================================================================================================
import paramiko

hostname = "192.168.1.101"
username = "test"
password = "abc123"

commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
]

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# execute the commands
for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)
    

client.close()

o/p:-

================================================== pwd ==================================================
/home/test

================================================== id ==================================================
uid=1000(test) gid=0(root) groups=0(root),27(sudo)

================================================== uname -a ==================================================
Linux rockikz 4.17.0-kali1-amd64 #1 SMP Debian 4.17.8-1kali1 (2018-07-24) x86_64 GNU/Linux

================================================== df -h ==================================================
Filesystem      Size  Used Avail Use% Mounted on
udev            1.9G     0  1.9G   0% /dev
tmpfs           392M  6.2M  386M   2% /run
/dev/sda1       452G  410G   19G  96% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           2.0G     0  2.0G   0% /sys/fs/cgroup
tmpfs           392M   12K  392M   1% /run/user/131
tmpfs           392M     0  392M   0% /run/user/1000
===============================================================================================================
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.10.10', username='ubuntu', key_filename='/home/ubuntu/.ssh/mykey.pem')

stdin, stdout, stderr = ssh.exec_command('lsb_release -a')

for line in stdout.read().splitlines():
    print(line)

ssh.close()

o/p:-
-------------------------
$ python execute.py

Distributor ID:   Ubuntu
Description:  Ubuntu 16.04.4 LTS
Release:  16.04
Codename: xenial
===============================================================================================================




