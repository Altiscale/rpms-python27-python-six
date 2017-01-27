# python27-python-six

This builds the python-six package for python27 scl.  Rebuilding is not straight forward.  Set these
parametes in the build job:

> RPM = python-six
>
> DEFINES = build_number $BUILD_NUMBER,dist .alti6,scl_prefix python27-,scl python27
>
> ROOT = centos6.7-python27-x86_64
>
> REPO_NAME = rpms-python27-python-six

All other parameters can use defaults.
