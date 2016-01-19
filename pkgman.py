"""
    pkgman - a Python 3 package manager for Linux
    
    Copyright (C) 2016  Daniel Amdurer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import shutil
import os
import urllib
def inst_pkg(pkgname):
    shutil.unpack_archive(pkgname+".pkg.tgz")
    shutil.unpack_archive(pkgname+"_data.pkg.tgz",/)
    dep_fix(pkgname)
    shutil.move(pkgname+".files","/usr/share/packages/installed")
def dl_pkg(pkgname):
    urllib.urlretrieve("http://www.example.com/packages/"+pkgname+".pkg.tgz", pkgname+".pkg.tgz")
def dep_fix(pkgname):
    with open(pkgname+".deps") as deps:
        for dep in deps:
            install_pkg(dep)
def install_pkg(pkgname):
    try:
        inst_pkg(pkgname)
    except FileNotFoundError:
        dl_pkg(pkgname)
        inst_pkg(pkgname)
def del_pkg(pkgname):
    with open("/usr/share/packages/installed/"+pkgname+".files") as files:
        for file in files:
            os.remove(file)
    os.remove("/usr/share/packages/installed/"+pkgname+".files")
def cleanup(pkgname):
    os.remove(pkgname+".pkg.tgz")
    os.remove(pkgname+"_data.pkg.tgz")
    os.remove(pkgname+".deps")
    os.remove(pkgname+".files")
def is_installed(pkgname):
    if pkgname+".files" in os.listdir("/usr/share/packages/installed/"):
        print("Package is installed")
        return True
    else:
        print("Package is not installed")
        return False
def main():
    pkgname=input("What is the package name?" + chr(12))
    function=input("What do you want to do? 1 for install, 2 for remove, 3 for search and anything else to quit.")
    try:
        func=int(function)
    except ValueError:
        pass
    else:
        if func == 1:
            install_pkg(pkgname)
        elif func == 2:
            del_pkg(pkgname)
        elif func == 3:
            is_installed(pkgname)
if __name__ == "__main__":
    main()
