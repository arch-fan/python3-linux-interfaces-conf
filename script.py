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
allow-hotplug {}
iface {} inet dhcp
            """).format(interface, interface))

            redmass()

        if (dhorst == 'dhcp'):
            dhcpconf2()

        address = input('Direccion IP del equipo: ')
        netmask = input('Introduce la mascara: ')
        gateway = input('Introduce puerta de enlace: ')
        network = input('Introduce la red: ')
        broadcast = input('Introduce el broadcast: ')

        interfacesfilea.write(("""

allow-hotplug {}
iface {} inet static
    address {}
    netmask {}
    gateway {}
    network {}
    broadcast {}

        """).format(str(interface), str(interface), str(address), str(netmask), str(gateway), str(network), str(broadcast)))

        redmass()
    else:
        exit()

def dhcpconf():

    interfacesfile.write(("""

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

allow-hotplug {}
iface {} inet dhcp


    """).format(interface, interface))

    redmass()

if (dhorst == 'dhcp'):
    dhcpconf()


address = input('Direccion IP del equipo: ')
netmask = input('Introduce la mascara: ')
gateway = input('Introduce puerta de enlace: ')
network = input('Introduce la red: ')
broadcast = input('Introduce el broadcast: ')

interfacesfile.write(("""

source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

allow-hotplug {}
iface {} inet static
    address {}
    netmask {}
    gateway {}
    network {}
    broadcast {}

""").format(str(interface), str(interface), str(address), str(netmask), str(gateway), str(network), str(broadcast)))

redmass()
