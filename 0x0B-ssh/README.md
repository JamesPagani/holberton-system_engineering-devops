# SSH

This project covers some basic usage of the **S**ecure **Sh**ell (SSH) protocol,
used to gain access to a remote machine and give it commands via a Command Line
shell. While it is possible to connect via password, SSH main strength lies in
using a pair of keys in order to safely encrypt the communication and save the
need to use a password.

## Project files
0. **0-use_a_private_key**: Connect to a remote server via private key (the
remote server already has the public key).
1. **1-create_ssh_key_pair**: Creates a new 4096 bit RSA key pair, protected by
a passphrase.
2. **2-ssh_config**: Sets the SSH config file so that the `ssh` command takes,
by deafult, a specific private key file and refuses to authenticate via password
.

**Random info:** Before *SSH*, there was *Telnet*. In essence, they acomplished
the same thing: access (and use) a remote machine. However, being developed
during the dawn of the internet, there wasn't any security features at all.
This means that someone with the know-how can intercept the *telnet*
communication and fetch confidential information.

*SSH* was the answer to these security issues, and while it is the most used way
to communicate with remote servers, *telnet* is still used, mainly on older
machines uncapable of implementing the newer protocols.

*Made by: Jaime Andrés Gálvez Villamarin*
