import pickle

no_match_dict = {}

with open("netab.txt") as f:
    for line in f:
        linesplit = line.split("|")
        ip = linesplit[0]
        ip_parts = ip.split(".")
        owner = linesplit[1]
        if int(ip_parts[0]) > 127 and owner == "No match\n":
            if int(ip_parts[0]) not in no_match_dict:
                no_match_curr = [int(ip_parts[1])]
                no_match_dict[(int(ip_parts[0]))] = no_match_curr
            else:
                no_match_dict[int(ip_parts[0])].append(int(ip_parts[1]))
        else:
            if owner == "No match\n":
                no_match_dict[int(ip_parts[0])] = 1

with open("nomatch.p", "wb") as fp:
    pickle.dump(no_match_dict, fp, pickle.HIGHEST_PROTOCOL)

with open("nomatch.p", "rb") as fp:
    test = pickle.load(fp)
    print(test)
