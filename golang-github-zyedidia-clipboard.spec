# Run tests in check section
%bcond_without check

%global goipath         github.com/zyedidia/clipboard
%global commit          4611e809d8b1a3051c11d11f4b610c44df73fa38

%global common_description %{expand:
Clipboard for golang.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Clipboard for golang
License: BSD
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4611e80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git4611e80
- Update with the new Go packaging
- Upstream GIT revision 4611e80

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161226gitadacf41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20161226gitadacf41
- First package for Fedora

