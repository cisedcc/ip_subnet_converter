#!/usr/bin/python -tt
# Copyright Austin Ellis

# Binary/Decimal Converter. Convers both ways
"""
Converts binary to decimal or decmial to binary
"""
import sys

binary_values = [128, 64, 32, 16, 8, 4, 2, 1]


def menu():
    """
    Function to print menu
    """
    print "1) Convert decimal IP"
    print "2) Convert Binary IP"
    print "3) Convert HEX IP"
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
    for item in ip_address:
        try:
            int(ip_address)
            return True
        except:
            return False


def ip_not_large(ip_address):
    for item in ip_address:
        num = int(item)
        if num > 255:
            print "num check"
            return False

        else:
            print "num check"
            return True


def ip_not_zero(ip_address):
    if ip_address == 0:
        return False
    else:
        return True


def dec_to_bin(num):
    """Convert decimal to binary with dec_to_bin() function """
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
    """Convert binary to decimal with bin_to_dec() function"""
    i = 0
    dec_converted = 0
    for item in num:
        if num[i] == "1":
            dec_converted = dec_converted + binary_values[i]
        i += 1
    return dec_converted


def convert_ip(ip_address):
    ip_bin = []
    ip_list = ip_address.split('.')
    for each in ip_list:
        ip_byte = dec_to_bin(int(each))
        ip_bin.append(''.join(ip_byte))

    return '.'.join(ip_bin)


def convert_bin_ip(bin_ip):
    ip_bin = []
    ip_bin_list = bin_ip.split('.')
    print ip_bin_list
    for each in ip_bin_list:
        ip_byte = bin_to_dec(str(each))
        ip_byte = str(ip_byte)
        ip_bin.append(''.join(ip_byte))

    print '.'.join(ip_bin)
    return '.'.join(ip_bin)
    # return "127.0.0.1"


def get_class(ip_address):
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
    elif ip_num < 255:
        ip_class = "E"
    else:
        ip_class = "Invalid IP Address"
    return ip_class


def get_subnet_mask(ip_address):
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
    #    if len(sys.argv[1]) > 1:
    #        convert = sys.argv[1]
    #        if (len(convert) < 4) and (int(convert) < 256):
    #            converted = dec_to_bin(int(convert))
    #            print '  '.join(converted)
    #
    #        elif len(convert) == 8:
    #          print bin_to_dec(convert)

    #        else:
    #            print "Invalid format"
    #
    #    else:
    #        print "entering menu"

    choice = 0
    while choice != "4":
        choice = menu()
        if choice == "1":
            get_ip = raw_input('Please enter an IP address: ')
            #valid_ip = check_ip_format(get_ip)
            # if valid_ip == True:
            ip_binary = convert_ip(get_ip)
            ip_class = get_class(get_ip)
#              ip_default_mask = get_subnet_mask(get_ip)
            print "\n"
            print "IP Address: ", get_ip
            print "Class: ", ip_class
            print "Default Subnet Mask: ", get_subnet_mask(get_ip)
            print "Private Space: ", private_space_check(get_ip)
            print "Binary: ", ip_binary

            print "\n"

            # else:
            # print "Invalid IP Address"

        elif choice == "2":
            get_binary_ip = raw_input('Please enter a binary IP address: ')
#            print type(get_binary_ip)
#            new_num = bin_to_dec(get_binary_ip)
#            print type(new_num)
#            print new_num
            ip_decimal = convert_bin_ip(get_binary_ip)
            ip_class = get_class(ip_decimal)
            print "\n"
            print "IP Address: ", ip_decimal
            print "Class: ", ip_class
            print "Binary: ", get_binary_ip
            print "\n"

        elif choice == "3":
            print "3"

        elif choice == "4":
            exit()

        else:
            print "\n invalid selection. \n"

if __name__ == '__main__':
    main()
