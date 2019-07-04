import configparser
import os.path
import xdg.BaseDirectory as xdgbasedir


class Config():
    '''store httpslurp config'''

    def __init__(self):
        resource = 'httpslurp'
        confpath = self.getconfpath(resource)
        self.conf = self.loadconfig(confpath, resource)

    @staticmethod
    def getconfpath(resource):
        '''get conf path or create as required'''
        confpath = xdgbasedir.load_first_config(resource)
        if confpath is None:
            confpath = xdgbasedir.save_config_path(resource)
        # put filename on
        return confpath

    @staticmethod
    def loadconfig(confpath, resource):
        '''load conf or create default if it doesn't exist'''
        conffile = resource + '.ini'
        fullconfpath = os.path.join(confpath, conffile)
        cfg = configparser.ConfigParser()
        if len(cfg.read(fullconfpath)) == 0:
            # empty or non-existent conf file, create default
            cfg['base'] = {'dumpdir': xdgbasedir.save_data_path(resource),
                           'port': '7777'}
            with open(fullconfpath, 'w') as configfile:
                cfg.write(configfile)
        return cfg
