import os
python 
m1 = Message(data = [0xaa, 0xdd, 3, 4, 5],arbitration_id = 547,is_extended_id=False)

rob = robotellBus("COM13")


dados = [1,3,5,7,8]
print("seta birate 500000")
rob.set_bitrate(500000)


print("set auto retransmit = 0")
rob.set_auto_retransmit(0)

print("auto mgmt")
rob.set_auto_bus_management(1)


print("le baud")
config = rob._readconfig(0x01FFFED0,2)

for i in config:
	print("{:02X}".format(i),end="-")

input()

cont = 0

while 1:
	#comandos()

	msg = rob._recv_internal(None)
	if msg != None:
		mostra = msg.data
		for i in mostra:
			#print(mostra)
			print("{:02X}".format(i),end="-")
		print("\n")	
	else:
		print("None")
		time.sleep(1)
print("Execução terminada. Aperte qualquer tecla para fechar...")
input()

os._exit(0)