
def convert_ip(ip_address):
    """
    Convert IP address to binary
    """
    ip_bin = []
    ip_list = ip_address.split('.')
    for each in ip_list:
        num = int(each)
        ip_byte = bin(num)[2:].zfill(8)
        ip_bin.append(''.join(ip_byte))
    return '.'.join(ip_bin)


def convert_bin_ip(bin_ip):
    """
    Convert a binary IP address to a decimal IP address
    """
    ip_bin = []
    ip_bin_list = bin_ip.split('.')
    for each in ip_bin_list:
        ip_byte = int(each, 2)
        ip_byte = str(ip_byte)
        ip_bin.append(''.join(ip_byte))

    return '.'.join(ip_bin)


def convert_bin_ip_hex(ip_address):
    # ip_bin_list = ip_address.split('.')
    # hex_ip = []
    # for octet in ip_bin_list:
    #     hex_ip.append(bin_to_hex(octet))
    #     print "octet", hex_ip
    # hex_ip_str = ''
    # for item in hex_ip:
    #     hex_ip_str = hex_ip_str + item[0] + item[1]
    # return hex_ip_str
    pass


def get_class(ip_address):
    """
    Returns the class for a given IP address
    """
    ip_list = ip_address.split('.')
    ip_num = int(ip_list[0])
    if ip_num < 128:
        ip_class = "A"
    elif ip_num < 192:
        ip_class = "B"
    elif ip_num < 224:
        ip_class = "C"
    elif ip_num < 240:
        ip_class = "D"
    elif ip_num < 256:
        ip_class = "E"
    else:
        ip_class = "Invalid IP Address"
    return ip_class


def get_subnet_mask(ip_address):
    """
    Retrns the default subnet mask for an IP address
    """
    ip_class = get_class(ip_address)
    if ip_class == "A":
        subnet_mask = '255.0.0.0'
        subnet_mask_short = '/8'
    elif ip_class == 'B':
        subnet_mask = '255.255.0.0'
        subnet_mask_short = '/16'
    elif ip_class == 'C':
        subnet_mask = '255.255.255.0'
        subnet_mask_short = '/24'
    else:
        subnet_mask = "N/A"
    return subnet_mask, subnet_mask_short


def private_space_check(ip_address):
    """
    Checks if an IP address is reserved as a private address space
    """
    ip_list = ip_address.split('.')
    ip_num_1 = int(ip_list[0])
    ip_num_2 = int(ip_list[1])

    if ip_num_1 == 10:
        private_space = 'Yes'
    elif (ip_num_1 == 172) and ((ip_num_2 > 15) and (ip_num_2 < 32)):
        private_space = 'Yes'
    elif (ip_num_1 == 192) and (ip_num_2 == 168):
        private_space = 'Yes'
    else:
        private_space = 'No'

    return private_space


def get_custom_subnet(ip_class, num_subnets):
    if ip_class == 'A':
        default_subnet_short = 8
    if ip_class == 'B':
        default_subnet_short = 16
    if ip_class == 'C':
        default_subnet_short = 24
    bits_borrowed = 0
    subnets = 0
    while subnets < num_subnets:
        bits_borrowed += 1
        subnets = 2**bits_borrowed
    custom_subnet_mask_short = int(default_subnet_short) + bits_borrowed
    octet_counter = 0
    bits_left = custom_subnet_mask_short
    if bits_left > 8:
        octet_counter = bits_left/8
        bits_left = bits_left % 8
    else:
        octet_counter = 1
    subnet_mask_full = []
    i = 0
    while i < octet_counter:
        subnet_mask_full.append(255)
        i += 1
    subnet_mask_full.append(256 - (2**(8 - bits_left)))
    if len(subnet_mask_full) < 4:
        while len(subnet_mask_full) < 4:
            subnet_mask_full.append(0)
    subnet_mask_str = '.'.join(str(e) for e in subnet_mask_full)
    hosts = 2**(32 - custom_subnet_mask_short)
    return custom_subnet_mask_short, subnet_mask_str, hosts, subnets


def get_num_subnets():
    pass


def get_num_hosts():
    pass


def main():
    exit_check = "y"
    while exit_check != 'n':
        get_ip = raw_input('Please enter an IP address: ')
        # raw_input('Create subnets using subnets or hosts (s or h)? ')
        get_subnets = raw_input('How many subnets do you need? ')
        print '\n-------------------------------------------------------\n'
        ip_address = get_ip
        ip_class = get_class(ip_address)
        default_subnet_mask = get_subnet_mask(get_ip)
        subnets = int(get_subnets)
        custom_subnet_mask = get_custom_subnet(ip_class, subnets)
        private_space = private_space_check(ip_address)
        hosts = custom_subnet_mask[2]
        subnets_actual = custom_subnet_mask[3]
        print 'IP Address: ', ip_address
        print 'Class: ', ip_class
        print 'Default Subnet Mask', default_subnet_mask[0], \
            default_subnet_mask[1]
        print 'Custom Subnet Mask: ', custom_subnet_mask[1], \
            '/' + str(custom_subnet_mask[0])
        print 'Private Space: ', private_space
        print 'Subnets: %d       Hosts: %d' % (subnets_actual, hosts)
        print 'Binary IP: ', convert_ip(get_ip)
        print '\n-------------------------------------------------------'
        exit_check = raw_input('Would you like to do another (y/n)? ')

if __name__ == '__main__':
    main()
