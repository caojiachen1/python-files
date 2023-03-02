import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.31.202' , username = 'root' , port = 8022 , password='    ')
ssh_stdin , ssh_stdout , ssh_stderr = ssh.exec_command('ifconfig')
print(ssh_stdout.read())
ssh.close()