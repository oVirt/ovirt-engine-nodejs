Name: ovirt-engine-nodejs
Version: 6.9.4
Release: 4%{?dist}
Summary: Node.js runtime for oVirt JavaScript applications
Group: Virtualization/Management
URL: https://nodejs.org
License: MIT
Source: https://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: python

%description
Node.js runtime for oVirt JavaScript applications.

%prep
%setup -q -n node-v%{version}

%build

# Do not generate debuginfo packages, as that doesn't work when using
# short build directories, like '/b':
%define debug_package %{nil}

# Perform the build:
./configure --prefix=%{_datadir}/%{name}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{_datadir}/%{name}/

%changelog
* Wed Feb 22 2017 Juan Hernandez <juan.hernandez@redhat.com> - 6.9.4-4
- Use a short build directory to avoid build issues.

* Wed Feb 15 2017 Juan Hernandez <juan.hernandez@redhat.com> - 6.9.4-3
- Build from source.

* Wed Feb 1 2017 Greg Sheremeta <gshereme@redhat.com> - 6.9.4-2
- Utilize oVirt standard CI while using non-templated .spec

* Mon Jan 23 2017 Vojtech Szocs <vszocs@redhat.com> - 6.9.4-1
- Bump Node.js version to 6.9.4.

* Fri Nov 18 2016 Vojtech Szocs <vszocs@redhat.com> - 6.9.1-1
- Bump Node.js version to 6.9.1.

* Tue Jun 28 2016 Vojtech Szocs <vszocs@redhat.com> - 4.4.6-1
- Bump Node.js version to 4.4.6.

* Thu Mar 31 2016 Juan Hernandez <juan.hernandez@redhat.com> - 4.3.2-1
- Build only for x86_64.

* Fri Mar 4 2016 Juan Hernandez <juan.hernandez@redhat.com> - 4.3.2
- Initial packaging.
