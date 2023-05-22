import paramiko
import sys
from optparse import OptionParser

def run_ssh_command(hostname, username, password, command):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        client.connect(hostname, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Print the output
        print("Command output:")
        for line in stdout:
            print(line.strip())

        # Close the SSH connection
        client.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check the credentials.")
        sys.exit(1)
    except paramiko.SSHException as ssh_exception:
        print(f"Unable to establish SSH connection: {str(ssh_exception)}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-H", "--host", dest="hostname", help="Hostname for the SSH command")
    parser.add_option("-u", "--username", dest="username", help="Username for SSH command")
    parser.add_option("-p", "--password", dest="password", help="Password for SSH")
    parser.add_option("-c", "--command", dest="command", help="Command to run")

    (options, args) = parser.parse_args()

    if not options.hostname or not options.username or not options.password or not options.command:
        parser.error("Missing required arguments.")

    hostname = options.hostname
    username = options.username
    password = options.password
    command = options.command

    run_ssh_command(hostname, username, password, command)
