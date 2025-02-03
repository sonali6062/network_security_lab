import socket
import TerminalMessage as TM 
from aes import aes

# TODO: Create Socket.
client = socket.socket()

# Server configuration.
config = {
    "ip": "localhost",
    "port": 8087
}
serverConfig = (config["ip"], config["port"])

# TODO: Create object for AES.
AES = aes()

# TODO: Connect to server.
try:
    client.connect(serverConfig)
    
    # TODO: Receive the connection successfull message.
    connectionSuccessfulMessage = client.recv(1024)
    
    # TODO: Decrypt the message and print.
    decryptedConnectionSuccessfulMessage = AES.decrypt(connectionSuccessfulMessage)
    print(decryptedConnectionSuccessfulMessage)
    TM.PrintTry(True, decryptedConnectionSuccessfulMessage)
except:
    TM.PrintTry(False, "Unable to connect to server.")
    exit()

# TODO: Receive the ask name message.
nameMessage = client.recv(1024)

# TODO: Decrypt the message and print.
decryptedNameMessage = AES.decrypt(nameMessage)
TM.PrintMessage(decryptedNameMessage)

# TODO: Take name input and encrypt the name.
TM.PrintMessage("Your Name Please: ")
name = input()
encryptedName = AES.encrypt(name)
print(encryptedName)

# TODO: Send encrypted name to the server.
client.send(encryptedName)

# TODO: Receive the welcome message.
welcomeMessage = client.recv(1024)

# TODO: Decrypt the message and print.
decryptedWelcomeMessage = AES.decrypt(welcomeMessage)
TM.PrintMessage(decryptedWelcomeMessage)

# TODO: Terminate the connection.
client.close()