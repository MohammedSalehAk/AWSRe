import subprocess
import os
os.system("ls")
print("--------------------------------------------------------------")
subprocess.run(["ls"])
print("--------------------------------------------------------------")
subprocess.run(["ls","-l"])
print("--------------------------------------------------------------")
subprocess.run(["ls","-l","README.md"])
print("--------------------------------------------------------------")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("--------------------------------------------------------------")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])