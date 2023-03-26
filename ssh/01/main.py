import paramiko


def execute_ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    print(output)


hostname = '192.168.2.43'
username = 'ivan'
password = 'XXXXXXXXX'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, port, username, password)

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
