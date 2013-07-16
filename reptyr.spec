Summary:	A tool for "re-ptying" programs
Summary(pl.UTF-8):	Narzędzie do "re-ptyjowania" programów
Name:		reptyr
Version:	0.5
Release:	1
License:	BSD-like
Group:		Applications
Source0:	https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
# Source0-md5:	92307c20bbcfad83eff4a369bc7f41d1
URL:		https://github.com/nelhage/reptyr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal. Started a long-running process over
ssh, but have to leave and don't want to interrupt it? Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%prep
%setup -q -n %{name}-%{name}-%{version}

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
