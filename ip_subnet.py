#!/usr/bin/python -tt

# Converts IP Addresses between binary, decimal, and hex and displays
# various subnet information
"""
Converts binary to decimal or decmial to binary
"""

binary_values = [128, 64, 32, 16, 8, 4, 2, 1]


def menu():
    """
    Function to print menu
    """
    print "1) Convert decimal IP"
    print "2) Convert Binary IP"
    print "3) Convert Binary to HEX IP"
    print "4) Exit"

    choice = raw_input('What would you like to do? ')

    return choice


def check_ip_format(ip_address):
    """
    Returns "T" if IP address is in the correct format and "F" if it is invalid.
    """
    ip_list = ip_address.split('.')
    valid = False
    if ip_not_letter(ip_list) == True:
        valid = True
    else:
        return False

    if ip_not_large(ip_list) == True:
        valid = True
    else:
        valid = False

    if ip_not_zero(int(ip_list[0])) == True:
        valid = True
    else:
        valid = False

    return valid


def ip_not_letter(ip_address):
    """
    checks to verify that the IP address doesn't containa letter
    """
    for item in ip_address:
        try:
            int(ip_address)
            return True
        except:
            return False


def ip_not_large(ip_address):
    """
    Checks to make sure the IP address isn't larger than 255
    """
    for item in ip_address:
        num = int(item)
        if num > 255:
            print "num check"
            return False

        else:
            print "num check"
            return True


def ip_not_zero(ip_address):
    """
    Checks to make sure the IP address doesn't start with 0
    """
    if ip_address == 0:
        return False
    else:
        return True


def dec_to_bin(num):
    """
    Convert decimal to binary with dec_to_bin() function
    """
    bin_converted = []
    i = 0
    while i < 8:
        bin_item = binary_values[i]
        if num >= bin_item:
            bin_converted.append("1")
            num = num - bin_item
            i += 1

        elif num < bin_item:
            bin_converted.append("0")
            i += 1

    return bin_converted


def bin_to_dec(num):
    """
    Convert binary to decimal with bin_to_dec() function
    """
    i = 0
    dec_converted = 0
    for item in num:
        if num[i] == "1":
            dec_converted = dec_converted + binary_values[i]
        i += 1
    return dec_converted


def bin_to_hex(num):
    """
    Convert byte (8 digit binary) to hex
    """
    nibble_1 = num[0:4]
    nibble_2 = num[4:9]
    dec_1 = bin_to_dec("0000" + nibble_1)
    dec_2 = bin_to_dec("0000" + nibble_2)
    hex_1 = hex_table(int(dec_1))
    hex_2 = hex_table(int(dec_2))
    hex_combined = str(hex_1), str(hex_2)
    return hex_combined


def hex_table(num):
    if num < 10:
        hex = num
    elif num == 10:
        hex = "A"
    elif num == 11:
        hex = "B"
    elif num == 12:
        hex = "C"
    elif num == 13:
        hex = "D"
    elif num == 14:
        hex = "E"
    elif num == 15:
        hex = "F"
    else:
        hex = "invalid"

    return hex


def convert_ip(ip_address):
    """
    Convert IP address to binary
    """
    ip_bin = []
    ip_list = ip_address.split('.')
    for each in ip_list:
        ip_byte = dec_to_bin(int(each))
        ip_bin.append(''.join(ip_byte))

    return '.'.join(ip_bin)


def convert_bin_ip(bin_ip):
    """
    Convert a binary IP address to a decimal IP address
    """
    ip_bin = []
    ip_bin_list = bin_ip.split('.')
    for each in ip_bin_list:
        ip_byte = bin_to_dec(str(each))
        ip_byte = str(ip_byte)
        ip_bin.append(''.join(ip_byte))

    return '.'.join(ip_bin)


def convert_bin_ip_hex(ip_address):
    ip_bin_list = ip_address.split('.')
    hex_ip = []
    for octet in ip_bin_list:
        hex_ip.append(bin_to_hex(octet))
    hex_ip_str = ''
    for item in hex_ip:
        hex_ip_str = hex_ip_str + item[0] + item[1]
    return hex_ip_str


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
        subnet_mask = "255.0.0.0"
    elif ip_class == "B":
        subnet_mask = "255.255.0.0"
    elif ip_class == "C":
        subnet_mask = "255.255.255.0"
    else:
        subnet_mask = "N/A"
    return subnet_mask


def private_space_check(ip_address):
    """
    Checks if an IP address is reserved as a private address space
    """
    ip_list = ip_address.split('.')
    ip_num_1 = int(ip_list[0])
    ip_num_2 = int(ip_list[1])

    if ip_num_1 == 10:
        private_space = 'Y'
    elif (ip_num_1 == 172) and ((ip_num_2 > 15) and (ip_num_2 < 32)):
        private_space = 'Y'
    elif (ip_num_1 == 192) and (ip_num_2 == 168):
        private_space = 'Y'
    else:
        private_space = 'N'

    return private_space


def main():
    choice = 0
    while choice != "4":
        choice = menu()
        if choice == "1":
            get_ip = raw_input('Please enter an IP address: ')
            ip_binary = convert_ip(get_ip)
            ip_class = get_class(get_ip)
            print "\n"
            print "IP Address: ", get_ip
            print "Class: ", ip_class
            print "Default Subnet Mask: ", get_subnet_mask(get_ip)
            print "Private Space: ", private_space_check(get_ip)
            print "Binary: ", ip_binary
            print "\n"

        elif choice == "2":
            get_binary_ip = raw_input('Please enter a binary IP address: ')
            ip_decimal = convert_bin_ip(get_binary_ip)
            ip_class = get_class(ip_decimal)
            print "\n"
            print "IP Address: ", ip_decimal
            print "Class: ", ip_class
            print "Default Subnet Mask: ", get_subnet_mask(ip_decimal)
            print "Private Space: ", private_space_check(ip_decimal)
            print "Binary: ", get_binary_ip
            print "\n"

        elif choice == "3":
            get_binary_ip = raw_input('Please enter a binary IP address: ')
            ip_decimal = convert_bin_ip(get_binary_ip)
            ip_hex = convert_bin_ip_hex(get_binary_ip)
            ip_decimal = convert_bin_ip(get_binary_ip)
            ip_class = get_class(ip_decimal)
            print "\n"
            print "IP Address: ", ip_decimal
            print "Class: ", ip_class
            print "Default Subnet Mask: ", get_subnet_mask(ip_decimal)
            print "Private Space: ", private_space_check(ip_decimal)
            print "Binary: ", get_binary_ip
            print "HEX Value: ", ip_hex
            print "\n"

        elif choice == "4":
            exit()

        else:
            print "\n invalid selection. \n"

if __name__ == '__main__':
    main()
