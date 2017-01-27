%{?scl:%scl_package python-six}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-six
Version:        1.10.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  scl-utils-build %{?scl_prefix}python-devel

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 2 build of the module.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{python27__python2} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{python27__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:EOF}

%files
%doc LICENSE README documentation/index.rst
%{python_sitelib}/*


%changelog
* Wed Jan 25 2017 Tucker <tucker@altiscale.com> - 1.10.0-1
- Update to version 1.10.0

* Tue Nov 19 2013 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-4
- bump release to be greater than build in RHEL-7

* Wed Nov 13 2013 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-2
- RHSCL-1.1 build

* Thu Mar 21 2013 David Malcolm <dmalcolm@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.0-1
- 1.2.0 (rhbz#852658)
- add %%check section

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Conditionalized python3-six, allowing an el6 build.

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging


