from netmiko import ConnectHandler

myserver = {
	'device_type': 'linux',
	'host': '192.168.56.103', #Your Server IP
	'username':'Server', #your Server Username
	'password': 'MakJemah', #your server password
	'port': 22,
	'secret':'',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('sudo apt-get update && apt-get -y install docker')
print(output)
myserver.exit_enable_mode()