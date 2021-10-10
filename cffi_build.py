# -- coding:utf-8
import subprocess
import os
from gitdb import *

def runcmd(command):
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)


def git(*args):
    return subprocess.check_call(['git'] + list(args))

# examples
# git("status")
# git("clone", "git://git.xyz.com/platform/manifest.git", "-b", "jb_2.5")




def get_git_url(url):
    ret = ""
    i = url.find("/blob")
    if i != -1:
        ret = url[0:i]
    return ret


def mkdir_if_need(path):
    if not os.path.exists(path):
        os.makedirs(path)

# setup.py: cffi_modules = ['iwlib/_iwlib_build.py:ffibuilder']
# return "iwlib/_iwlib_build.py"
def get_cffi_modules(setup):
    with open(setup, 'r', encoding='utf-8') as fp:
        for line in fp.readlines():  # 依次读取每行
            line = line.strip()  # 去掉每行头尾空白
            # iS = line.find()
            # iE = line.find(":ffibuilder")


    return ""

if __name__ == '__main__':
    repo_info = []

    db = DB('github', 'setuprepo')
    ret = db.get({},{'repository.full_name':1, 'repository.html_url':1 })

    for item in ret:
        try:
            full_name = item["repository"]["full_name"]
            html_url = item["repository"]["html_url"]
            full_name = full_name.replace('/','_')
            repo_info.append({"full_name": full_name, "html_url": html_url})
        except:
            pass

    for item in repo_info:
        full_name = item["full_name"]
        html_url = item["html_url"]
        folder = os.path.join("gitrepos", full_name)
        mkdir_if_need(folder)
        try:
            git("clone", html_url, folder)
        except:
            pass
