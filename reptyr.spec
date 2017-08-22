# TODO
# - package /usr/share/bash-completion/completions/reptyr
Summary:	A tool for "re-ptying" programs
Summary(pl.UTF-8):	Narzędzie do przepinania programów do nowego terminala (re-pty)
Name:		reptyr
Version:	0.6.2
Release:	1
License:	BSD-like
Group:		Applications
Source0:	https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
# Source0-md5:	9beb26462407f229c9e900466dc25b56
Patch0:		https://github.com/nelhage/reptyr/compare/%{name}-%{version}...master.diff
# Patch0-md5:	a8fba19745c20d18de4802001c15dfbd
URL:		https://github.com/nelhage/reptyr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal. Started a long-running process over
ssh, but have to leave and don't want to interrupt it? Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%description -l pl.UTF-8
reptyr to narzędzie służące do podłączania już działającego programu
do nowego terminala. Jest to pomocne szczególnie w przypadku
uruchomienia długo trwającego procesu po ssh, kiedy zachodzi potrzeba
rozłączenia się bez przerywania programu - wystarczy uruchomić
screena, użyć reptyra do przechwycenia programu, a następnie zabić
sesję ssh.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NOTES README.md
%attr(755,root,root) %{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*
%lang(fr) %{_mandir}/fr/man1/reptyr.1*
