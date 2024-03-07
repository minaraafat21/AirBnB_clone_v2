#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import run, env, lcd, cd, local
import os


env.hosts = ['34.224.15.155', '	100.25.165.235']


def do_clean(number=0):
    """
    Deletes unnecessary archives
    """
    try:
        number = int(number)
        if number < 0:
            return
        elif number == 0 or number == 1:
            number = 1
        else:
            number += 1

        with lcd('versions'):
            local("ls -t | tail -n +{} | xargs rm -rf".format(number))

        with cd('/data/web_static/releases'):
            run("ls -t | tail -n +{} | xargs rm -rf".format(number))
    except:
        pass
