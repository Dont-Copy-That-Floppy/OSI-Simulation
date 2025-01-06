def generate_mac():
    from random import randint
    return ":".join(f"{randint(0, 255):02x}" for _ in range(6))

def generate_ip():
    from random import randint
    return f"192.168.{randint(0, 255)}.{randint(1, 254)}"
