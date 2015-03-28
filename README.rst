Op
==

Fast file finder and opener.


Examples
========

Open a deep file with a minimum of key words::

  ~/yourgitrepo$ op some buried file
  Loading:
  - ~/yourgitrepo/your/**some**/**file**/very/deep/and/**buried**/somewhere.txt


*Multiple* matching files are listed in reverse modification order. Nothing is opened::

  ~/yourgitrepo$ op buried file
  ./a/third/**file**/very/deep/and/**buried**/somewhere.txt
  ./a/second/**file**/very/deep/and/**buried**/somewhere.txt
  ./a/first/**file**/very/deep/and/**buried**/somewhere.txt


Add the number 1 at the end to load just the last modified matching file::

  ~/yourgitrepo$ op buried file 1
  Loading:
  - ./a/third/file/very/deep/and/buried/somewhere.txt)


Install
=======

$ sudo pip install op


Customize
=========

By default, op will invoke your system's default text editor when
opening files.

If you want to customize:

* What to use to open the files you find (e.g. your favorite text editor).
* Which files to ignore and when.
* Which group of files to go looking in.

Then you will want to put an op.yml in a directory that you want
to use it in.
