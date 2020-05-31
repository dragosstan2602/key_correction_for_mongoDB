from pprint import pprint as pp


def correct_dict(old_dict, old_string, new_string):
    pp(old_dict)
    new_dict = {}
    new_key = None

    for key in old_dict.keys():
        if "." in key:
            new_key = key.replace(old_string, new_string)
            new_dict[new_key] = old_dict[key]
        else:
            new_dict[key] = old_dict[key]

    pp(new_dict)


def main():
    d = {"ge0/1.100": {"description": "N/A", "ip": "1.1.1.1"},
         "le1/1/1.1234": {"description": "other interface", "ip": "2.1.1.1"},
         "ve1.200": {"description": "vlan iface", "ip": "3.1.1.1"},
         "ge1": {"description": "good interface", "ip": "N/A"},
         "vlan100": {"description": "good interface", "ip": "N/A"}}

    correct_dict(d, ".", "[dot]")


if __name__ == '__main__':
    main()
