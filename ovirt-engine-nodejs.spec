Name: ovirt-engine-nodejs
Version: 6.9.4
Release: 2%{?dist}
Summary: Node.js runtime for oVirt JavaScript applications
Group: Virtualization/Management
URL: https://nodejs.org
License: Multiple
Source: https://nodejs.org/dist/v%{version}/node-v%{version}-linux-x64.tar.xz

ExclusiveArch: x86_64

%description
Node.js runtime for oVirt JavaScript applications.

%install
mkdir -p %{buildroot}%{_datadir}
tar -xf %{SOURCE0} -C %{buildroot}%{_datadir}
mv %{buildroot}%{_datadir}/node-v%{version}-linux-x64 %{buildroot}%{_datadir}/%{name}

%files
%license %{_datadir}/%{name}/LICENSE
%{_datadir}

%changelog
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
