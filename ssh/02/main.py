import paramiko


def execute_ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    print(output)


hostname = '192.168.2.43'
username = 'ivan'
port = 22

key_file = '/home/ivan/.ssh/id_rsa_dev'
key = paramiko.RSAKey.from_private_key_file(key_file)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, port, username, pkey=key)

    commands = [
        'pwd',
        'ls',
        'gcc -v'
    ]

    for command in commands:
        print(f"\nExecuting '{command}' command:")
        execute_ssh_command(ssh, command)

finally:
    ssh.close()
