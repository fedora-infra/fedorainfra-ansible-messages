%global srcname fedorainfra_ansible_messages

Name:           python-fedorainfra_ansible_messages
Version:        0.0.1
Release:        0.20210125114029911485.packit_support.1.g44da197%{?dist}
Summary:        Message schemas for fedorainfra messages produced by ansible 

License:        MIT
URL:            https://github.com/fedora-infra/fedorainfra-ansible-messages
Source0: fedorainfra_ansible-messages-0.0.1.tar.gz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-cov
BuildRequires:  python%{python3_pkgversion}-fedora-messaging

%description
Message schemas for fedorainfra messages produced by ansible 

# package the library

%package -n python3-%{srcname}
Summary:        %{summary}

Requires:  python%{python3_pkgversion}-fedora-messaging
%if 0%{?fedora} < 33
%{?python_provide:%python_provide python3-%{srcname}}
%endif

%description -n python3-%{srcname}
Message schemas for fedorainfra messages produced by ansible 

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/

#--------------------------------------------------------

%prep
%autosetup -n fedorainfra_ansible-messages-0.0.1
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

%check
%{__python3} -m pytest

%install
%py3_install


%changelog
* Mon Jan 25 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210125114029911485.packit_support.1.g44da197
- Builds localy, fails in copr (Adam Saleh)

* Mon Jan 25 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210125112938233856.packit_support.1.g44da197
- Builds localy, fails in copr (Adam Saleh)

* Mon Jan 25 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210125112920274931.packit_support.1.g44da197
- Builds localy, fails in copr (Adam Saleh)

* Fri Jan 22 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210122111554358806.packit_support.1.g44da197
- Builds localy, fails in copr (Adam Saleh)

* Fri Jan 22 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210122105910630767.packit_support.1.g44da197
- Builds localy, fails in copr (Adam Saleh)

* Fri Jan 22 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210122105014987741.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Fri Jan 22 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210122104824062495.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Fri Jan 22 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210122102242124904.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Thu Jan 21 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210121205822927991.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Thu Jan 21 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210121205704261270.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Thu Jan 21 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210121113922193408.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Thu Jan 21 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210121113309222085.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Thu Jan 21 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210121110536587288.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 0.0.1-0.20210120133759819590.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120133718369411.packit_support.0.gbef3cd8
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120133610948574.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120132809627754.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120131523376392.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120131440385288.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120131408385285.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120130537464476.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120102837948955.packit_support
- Development snapshot (bef3cd88)

* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120083652209045.git.receive
- Development snapshot (dafb7c5e)

* Tue Jan 19 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210119131915851563.git.receive
- Development snapshot (dafb7c5e)

* Wed Mar 18 2020  Adam Saleh <asaleh@redhat.com> - 0.0.1-1
- initial package for EPEL

