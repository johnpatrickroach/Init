#!/usr/bin/env python3

import sys
import ConfigParser


def initiate(configfile, *args):
    dictlist = []
    try:
        parser = ConfigParser.ConfigParser()
        parser.read(configfile)
        for arg in args:
            if parser.has_section(arg):
                params = parser.items(arg)
                gendict = {}
                for param in params:
                    if param[1].isdigit():
                        gendict[param[0]] = parser.getint(arg, param[0])
                    elif isinstance(param[1], bool):
                        gendict[param[0]] = parser.getboolean(arg, param[0])
                    else:
                        gendict[param[0]] = param[1]
                dictlist.append(gendict)
            else:
                raise Exception('Section {0} not found in the {1} file'.format(arg, configfile))
        return dictlist
    except Exception as err:
        print("FATAL ERROR! Failed to get config info: %s" % (str(err)))
        print("Config file: %s" % str(configfile))
        print("Arg: %s" % str(arg) for arg in args)
        sys.exit(1)
