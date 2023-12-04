import re
import yaml


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    dct = {}
    for files in list_of_files:
        host = files.split("_")[-1].split(".")[0]
        with open(files, "r") as f1:
            for data in f1:
                res = re.findall("(\w+) +(\w+ \d+/\d+) +(\d+) +(\w+ \w+) +(\S+) +(\w+ \d+/\d+)", data)
                if res:
                    for lst in res:
                        lst = list(lst)
                        if not dct.get(host):
                            dct.update({host: {lst[1]: {lst[0]: lst[-1]}}})
                        else:
                            dct[host].update({lst[1]: {lst[0]: lst[-1]}})

    if save_to_filename:
        with open(save_to_filename, "w") as f2:
            yaml.dump([dct], f2)

if __name__ == "__main__":
    lst = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"]
    generate_topology_from_cdp(lst, "topology.yaml")