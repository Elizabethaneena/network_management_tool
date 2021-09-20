#!/usr/bin/python3
import os

def assign_ip():
	ip = input('Enter ip address to add on interface : ')
	interface=os.popen('ip l').read()
	print('__Interface__')
	print(interface)
	interface_choice=input("Choose the interface : ") 
	command = f'ip address add {ip} dev {interface_choice}'
	result = os.popen(command).read()
	print(' Ip address assigned successfully ')


def delete_ip():
	ip = input('Enter ip address to delete from interface : ')
	interface = os.popen('ip l').read()
	print('__Interface__') 
	print(interface)
	interface_choice=input("Choose the interface : ") 
	command = f'sudo ip address del {ip} dev {interface_choice}'
	result = os.popen(command).read()
	print(' Ip address Deleted successfully ')


def display_ip():
	command = f'ip -c -br address'
	result = os.popen(command).read()
	print('  IP address of all interfaces  ')
	print(result)

def display_all_interface():
	interface = 'ip l'
	result = os.popen(interface).read()
	print('   Interface   ')
	print(result)

def configure_routing():
	network_addr = input('Enter network address/mask : ')
	gateway_ip = input('Enter gateway ip address : ')
	cmd = f'ip r add {network_addr} via {gateway_ip}'
	result = os.popen(cmd).read()
	print(result)
	print('Routing configured')

def On_Off_interface():
	print('1.Turned off interface')
	print('2.Turned on interface')
	choice = int(input("Enter the choice : "))
	interface = os.popen('ip l').read()
	print('  Interface  ')
	print(interface)
	interface_choice = input("Choose the interface : ")
	
	if choice == 1:
		cmd = f'ip link set dev {interface_choice}  down'
		result = os.popen(cmd).read()
		print(f'{interface_choice} Turned off | Details : {result}')

	elif choice == 2:
		cmd = f'ip link set dev {interface_choice}  up'
		result = os.popen(cmd).read()
		print(f'{interface_choice} Turned on | Details : {result}')

	else:
		print('Invalid choice')


def add_arp_entry():
	ip = input('Enter ip address  : ')
	interface = os.popen('ip l').read()
	print('  Interface  ')
	print(interface)
	interface_choice = input("Choose the interface : ")
	arp_cache = os.popen('ip n show').read()
	cmd = f'ip n add {ip} lladdr {arp_cache} dev {interface_choice} nud permanent'
	result = os.popen(cmd).read()
	print('ARP entry added successfully ')


def del_arp_entry():
	ip = input('Enter ip address : ')
	interface = os.popen('ip l').read()
	print('  Interface  ')
	print(interface)
	interface_choice = input("Choose the interface : ")
	cmd = f'ip n del {ip} dev {interface_choice}'
	result = os.popen(cmd).read()
	print('ARP Entry deleted successfully ')


def restart_network():
	cmd1 = 'sudo systemctl restart networking'
	cmd2 = 'sudo systemctl status networking'
	os.popen(cmd1).read()
	print('Network services restarted ')
	print(os.popen(cmd2).read())


def change_host_name():
	host_name = input("Enter new host name :")
	cmd = f'hostnamectl set-hostname {host_name}'
	os.popen(cmd).read()
	print(f'new host name {host_name} set successfully ')


def add_dns_server():
	#nameserver 8.8.8.8 write in this format
	# ctrl + d  to exit
	cmd = 'sudo cat  >> /etc/resolv.conf'
	print(os.popen(cmd).read())
	print('Nameserver added successfully  ')

def main_menu():
	print('1.Assign ip address')
	print('2.Delete ip address')
	print('3.Display ip address')
	print('4.Display all interfaces')
	print('5.Configure Routing')
	print('6.Turn On/Off interface')
	print('7.Add ARP entry')
	print('8.Delete ARP Entry')
	print('9.Restart Network')
	print('10.Change hostname')
	print('11.Add DNS server entry')
	print('12.Exit')
    
while True:
	main_menu()
	ch = int(input('Enter choice : '))
	if ch == 1:
		assign_ip()
	elif ch == 2:
        	delete_ip()
	elif ch == 3:
		display_ip()
	elif ch == 4:
		display_all_interface()
	elif ch == 5:
		configure_routing()
	elif ch == 6:
		On_Off_interface()
	elif ch == 7:
		add_arp_entry()
	elif ch == 8:
		del_arp_entry()
	elif ch == 9:
		restart_network()
	elif ch == 10:
		change_host_name()
	elif ch == 11:
		add_dns_server()
	elif ch == 12:
		break
	else:
		print('Invalid choice!Choose the correct')
