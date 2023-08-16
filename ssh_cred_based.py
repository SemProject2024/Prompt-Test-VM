import paramiko

# VM information
host = '172.174.41.118'
port = 22
username = 'azureuser'
password = 'P@ssword!123'

# Create an SSH client
ssh_client = paramiko.SSHClient()

# Automatically add the server's host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the VM
    ssh_client.connect(host, port=port, username=username, password=password)
    
    # Execute a command on the VM (for example, listing files in the home directory)
    stdin, stdout, stderr = ssh_client.exec_command('echo "hello" > hi.txt')
    stdin, stdout, stderr = ssh_client.exec_command('ls')
    
    # Print the command output
    print(stdout.read().decode())
    
except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials.")
except paramiko.SSHException as e:
    print("Unable to establish SSH connection:", str(e))
finally:
    # Close the SSH connection
    ssh_client.close()
