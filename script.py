import os

interfacesfile = open(r"/etc/network/interfaces", "w")
interfacesfilea = open(r"/etc/network/interfaces", "a")

interfacesfile.write("")

interface = input('Introduce el interfaz: ')
dhorst = input('dhcp o static: ')

def redmass():

    redmas = input('Quieres una red mas?(Y/N): ')

    if (redmas == 'Y'):

        interface = input('Introduce el interfaz: ')
        dhorst = input('dhcp o estatic: ')

        def dhcpconf2():

            interfacesfilea.write(("""
auto {}
iface {} inet dhcp

            """).format(interface, interface))

            redmass()

        if (dhorst == 'dhcp'):
            dhcpconf2()

        address = input('Direccion IP del equipo: ')
        netmask = input('Introduce la máscara: ')
        gateway = input('Introduce puerta de enlace: ')
        network = input('Introduce la red: ')
        broadcast = input('Introduce el broadcast: ')

        interfacesfilea.write(("""
auto {}
iface {} inet static
    address {}
    netmask {}
    gateway {}
    network {}
    broadcast {}

        """).format(str(interface), str(interface), str(address), str(netmask), str(gateway), str(network), str(broadcast)))

        redmass()
    else:
        os.system('systemctl restart networking')
        os.system('ifup -a')
        exit()


def dhcpconf():

    interfacesfile.write(("""

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

auto {}
iface {} inet dhcp

    """).format(interface, interface))

    redmass()


if (dhorst == 'dhcp'):
    dhcpconf()


address = input('Direccion IP del equipo: ')
netmask = input('Introduce la máscara: ')
gateway = input('Introduce puerta de enlace: ')
network = input('Introduce la red: ')
broadcast = input('Introduce el broadcast: ')

interfacesfile.write(("""

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

auto {}
iface {} inet static
    address {}
    netmask {}
    gateway {}
    network {}
    broadcast {}

""").format(str(interface), str(interface), str(address), str(netmask), str(gateway), str(network), str(broadcast)))

redmass()
