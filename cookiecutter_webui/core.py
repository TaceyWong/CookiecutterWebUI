# coding:utf-8

"""
core.py
:
by tacey@AtomPai on 19-3-18
"""

from os import listdir,path
from cookiecutter.main import get_user_config



def get_templates():
    c_path = get_user_config().get('cookiecutters_dir')
    template_list = listdir(c_path)
    resutl = []
    for template in template_list:
        if "cookiecutter.json" in listdir(path.join(c_path,template)):
            resutl.append(template)

    return sorted(resutl)

