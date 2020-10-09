# Import the module
import subprocess
# Ask the user for input
host ="127.0.0.1"
# Set up the echo command and direct the output to a pipe
#p1 = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
# Run the command
"""
outputs = p1.communicate()
print(outputs)
print("===========")
output=outputs[0]
output1=outputs[1]
print(type(output),output)
print("===========")
print("error: ",output1)
print("===========")
print(output.decode('gb18030'))
print("===========")
"""
p1 = commands.getstatusoutput('ping %s'%(host))