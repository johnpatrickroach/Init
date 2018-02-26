# Init
This module is meant to interact with ConfigParser and dynamically initialize class instances.
In python apps that utilize many classes, instances of classes, and configuration parameters,
this script can vastly shorten code length and time spent coding.

# Example Usage
```angular2html
import init
 
 
class Class(object):
    def __init__(self, configfile, *args):
        try:
            dictlist = init.initiate(configfile, *args)
            for dictionary in dictlist:
                for key, value in dictionary.iteritems():
                    setattr(self, key, value)
        except Exception as err:
            print("Failed to get config file info: %s" % (str(err)))
            sys.exit(1)
```