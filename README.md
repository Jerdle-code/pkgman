# pkgman
A package manager, coded in Python 3.
It only works on Un*x and has not been tested. A malicious package could destroy your system.
## Technical details
This program untars a .pkg.tgz file and untars a _data.pkg.tgz to /.
A list of the files is added to a directory (/usr/share/pkgman/installed/), so that the package can be removed.
The removal part removes every file in the list.
