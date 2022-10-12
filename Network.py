import socket
import logging

def checkInternetConnection(host="8.8.8.8", port=53, timeout=10):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)

    This attmepts to connect to googles servers to check if the device has internet. 
    Google is used because google is basically never down and a reliable way to check. 

    Returns:
    True -> We have internet
    False -> No internet 
    """
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except socket.error as ex:
        logging.info("No internet")
        return False