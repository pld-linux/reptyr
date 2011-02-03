
%define	rel	0.1
%define	subver	2011.02.03

Summary:	A tool for "re-ptying" programs
Summary(pl.UTF-8):	Narzędzie do "re-ptyjowania" programów
Name:		reptyr
Version:	0
Release:	0.%{subver}.%{rel}
License:	BSD-like
Group:		Applications
Source0:	https://github.com/nelhage/reptyr/tarball/master/%{name}-%{subver}.tar.gz
# Source0-md5:	2b48b412a654e8c22ad53a6349c6b0a1
URL:		https://github.com/nelhage/reptyr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal. Started a long-running process over
ssh, but have to leave and don't want to interrupt it? Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%prep
%setup -q -c -n %{name}-%{subver}
mv nelhage-reptyr-*/* .

%build
%{__make} \
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
%doc BUGS NOTES README
%attr(755,root,root) %{_bindir}/reptyr
