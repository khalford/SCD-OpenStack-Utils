from sys import stdout
from pynetbox_query.top_level_methods import TopLevelMethods
from pynetbox_query.argparser import arg_parser


def do_netbox_check(args):
    """
    This method will iterate through a csv and check that each device exists in netbox and return the devices that do and don't exist in a readable format.
    :param args: The arguments, url, token, file path
    """
    methods = TopLevelMethods(args.url, args.token)
    methods.check_file_path(args.file_path)
    devices = methods.read_csv(args.file_path)
    existence = {}
    for device in devices:
        exist = methods.check_device_exist(device)
        if exist:
            existence[device.name] = True
        else:
            existence[device.name] = False
    for name in existence:
        stdout.write(f"Device {name} exists in netbox: {existence[name]}\n")


def main():
    """
    This function calls argparse and the logic function do_netbox_check.
    """
    arguments = arg_parser()
    do_netbox_check(arguments)


if __name__ == "__main__":
    main()
