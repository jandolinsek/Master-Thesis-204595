import paramiko
from scp import SCPClient
import getpass

# --- Configuration ---
hostname = "i121srv03.vu-wien.ac.at"                        # Replace with server IP if hostname fails
port = 12121                                     # Replace if your server uses a different port (e.g. 2222)
username = "dolinsek"
private_key_path = r"D:\FHWN\VetMed\id_rsa" # Keep the 'r' before the string for Windows paths

# remote_directory = "/home/dolinsek/SO4_mgenomics/07_assembly_metaspades_single/01_binning/checkm"
# local_download_path = r"D:\FHWN\M.BDSC.B.23.AA Masterarbeit\metagenomes_stats\checkm\SO4_metaspades_single" # Keep the 'r' before the string

remote_directory = "/home/dolinsek/SO4_mgenomics/08_skani/01_clusters/reassembly/quast"
local_download_path = r"D:\FHWN\M.BDSC.B.23.AA Masterarbeit\metagenomes_stats\quast\SO4_cl1_re" # Keep the 'r' before the string


def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Prompt you to type your passphrase securely (it won't echo characters to the screen)
    passphrase = getpass.getpass("Enter your SSH key passphrase: ")
    
    print(f"Connecting to {username}@{hostname}:{port}...")

    try:
        # Pass the password to the key loader!
        key = paramiko.RSAKey.from_private_key_file(private_key_path, password=passphrase)
        
        # Connect to the server
        ssh.connect(hostname, port=port, username=username, pkey=key)
        print("Connected successfully!")

        # Open an SCP channel
        with SCPClient(ssh.get_transport()) as scp:
            print(f"Downloading {remote_directory}...")
            # Set recursive=True to download the whole directory
            scp.get(remote_directory, local_path=local_download_path, recursive=True)
            print(f"Download complete! Saved to {local_download_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()