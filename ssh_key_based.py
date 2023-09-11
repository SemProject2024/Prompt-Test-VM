def run(template):
    import paramiko

    # VM details
    ip_address = "35.211.137.172"
    username = "aashu"  # Replace with your VM's username
    private_key_path = "C:/Users/aashu/.ssh/gcp-user"  # Replace with your private key path
    file_content = template

    # Establish SSH connection
    try:
        private_key = paramiko.RSAKey(filename=private_key_path)
        
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh_client.connect(ip_address, username=username, pkey=private_key)
        
        print("Connected to VM via SSH")
        
        #DESTROYING RESOURCES
        stdin, stdout, stderr = ssh_client.exec_command("terraform destroy -auto-approve")
        print("Executing terraform destroy")
        output = stdout.read().decode("utf-8")
        print(output)
        
        
        # command = f'echo "{file_content}" > main.tf'
        # stdin, stdout, stderr = ssh_client.exec_command("echo '%s' > main.tf "%file_content)
        # print("Updated main.tf")
        # stdin, stdout, stderr = ssh_client.exec_command("terraform init")
        # output = stdout.read().decode("utf-8")
        # print("Executed terraform init")
        # stdin, stdout, stderr = ssh_client.exec_command("terraform plan -lock=false")
        # print("Executing terraform plan")
        # output = stdout.read().decode("utf-8")
        # stdin, stdout, stderr = ssh_client.exec_command("terraform apply -auto-approve")
        # print("Executing terraform apply")
        # output = stdout.read().decode("utf-8")
        # print(output)
        # stdin, stdout, stderr = ssh_client.exec_command("terraform output")
        # print("Getting output variables")
        # output = stdout.read().decode("utf-8")
        # print(output)
        
        # # Execute commands or perform operations on the VM if needed
        
        # ssh_client.close()
        # print("SSH connection closed")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
