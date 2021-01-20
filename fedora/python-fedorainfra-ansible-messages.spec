%global srcname python-fedorainfra-ansible-messages

Name:           python-fedorainfra-ansible-messages
Version:        1.0.0
Release:        0.20210120083652209045.git.receive%{?dist}
Summary:        Message schemas for fedorainfra messages produced by ansible 

License:        MIT
URL:            https://github.com/fedora-infra/fedorainfra-ansible-messages
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools-scm-git-archive)

%description
Message schemas for fedorainfra messages produced by ansible 

# package the library

%package -n python3-%{srcname}
Summary:        %{summary}

%if 0%{?fedora} < 33
%{?python_provide:%python_provide python3-%{srcname}}
%endif

%description -n python3-%{srcname}
Message schemas for fedorainfra messages produced by ansible 

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/

#--------------------------------------------------------

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest

%changelog
* Wed Jan 20 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210120083652209045.git.receive
- Development snapshot (dafb7c5e)

* Tue Jan 19 2021 Adam Saleh <asaleh@redhat.com> - 1.0.0-0.20210119131915851563.git.receive
- Development snapshot (dafb7c5e)

* Wed Mar 18 2020  Adam Saleh <asaleh@redhat.com> - 0.0.1-1
- initial package for EPEL

