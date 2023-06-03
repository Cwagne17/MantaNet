# native imports
import logging
import threading

# library imports
import docker
import inquirer
import psutil
from scapy.all import sniff, wrpcap

# global variables
client = docker.from_env()
logger = logging.getLogger(__name__)

def packet_callback(packet, network, interface):
    """Callback function for scapy sniff function. Writes packet to pcap file and logs packet summary.

    Args:
        packet (Packet): packet received by scapy sniff function
        network (str): name of the docker network
        interface (str): host interface name for docker network
    """
    wrpcap(f"../outputs/{network}-{interface}.pcap", packet, append=True)
    logger.info(f"Network: {network}, {packet.summary()}")

def get_interface(network_name: str):
    """Identifies the interface for a given docker network

    Args:
        network_name (str): name of the docker network

    Returns:
        str: name of the interface
    """
    
    if network_name == "none":
        logger.info("'none' network selected, skipping...")
    
    network_info = client.networks.get(network_name)

    if network_info.attrs["Driver"] == "bridge":
        for interface, addresses in psutil.net_if_addrs().items():
            for address in addresses:
                if address.address == network_info.attrs["IPAM"]["Config"][0]["Gateway"]:
                    return interface
    
    # TODO: add support for other network drivers
    elif network_info.attrs["Driver"] == "overlay":
        logger.debug("overlay not supported yet")
        
    elif network_info.attrs["Driver"] == "host":
        logger.debug("host not supported yet")
    
    elif network_info.attrs["Driver"] == "ipvlan":
        logger.debug("ipvlan not supported yet")
    
    elif network_info.attrs["Driver"] == "macvlan":
        logger.debug("macvlan not supported yet")

def thread_target(network, interface):
    """Target function for packet sniffing threads. Calls scapy sniff function with packet_callback function.

    Args:
        network (str): name of the docker network
        interface (str): host interface name for docker network
    """
    sniff(iface=interface, prn= lambda pkt: packet_callback(pkt, network, interface))

def main():
    logging.basicConfig(   
        level=logging.INFO,
        format='[%(levelname)s] %(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    docker_networks = [network.name for network in client.networks.list()]
    selected_networks = inquirer.checkbox("Select docker networks for packet capture.", choices=docker_networks)
        
    threads = []     
    for network in selected_networks:
        interface = get_interface(network)
        logger.info(f"Setting up packet sniffer for {network} on {interface}")
        threads.append(threading.Thread(target=thread_target, args=(network, interface)))
    
    # start packet sniffing threads
    for thread in threads:
        logger.info(f"Starting thread {thread}")
        thread.start()
        
    # wait for threads to finish
    for thread in threads:
        logger.info(f"Waiting for thread {thread}")
        thread.join()
    
if __name__ == "__main__":
    main()