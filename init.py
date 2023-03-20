#!/usr/bin/env python3

import sys
import ConfigParser
import numbers


def initiate(configfile, *args):
    dictlist = []
    try:
        parser = ConfigParser.ConfigParser()
        parser.read(configfile)
        for arg in args:
            if not parser.has_section(arg):
                raise Exception('Section {0} not found in the {1} file'.format(arg, configfile))
            params = parser.items(arg)
            gendict = {}
            for param in params:
                if isinstance(param[1], numbers.Integral):
                    gendict[param[0]] = parser.getint(arg, param[0])
                elif isinstance(param[1], float):
                    gendict[param[0]] = parser.getfloat(arg, param[0])
                elif isinstance(param[1], bool):
                    gendict[param[0]] = parser.getboolean(arg, param[0])
                else:
                    gendict[param[0]] = param[1]
            dictlist.append(gendict)
        return dictlist
    except Exception as err:
        print(f"FATAL ERROR! Failed to get config info: {str(err)}")
        print(f"Config file: {str(configfile)}")
        print(f"Arg: {str(arg)}" for arg in args)
        sys.exit(1)
