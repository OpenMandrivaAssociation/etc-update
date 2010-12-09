Name:		etc-update
Version: 20020731
Release: %mkrel 11
Summary:	Mergemaster for Linux
Source:		%name-%version.tar.bz2
Patch:		etc-update-foo.patch.bz2
URL:		http://www.xs4all.nl/~hanb/software
License:	GPL
Group:		System/Configuration/Packaging
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-buildroot

%description
After an update with urpmi rpm makes .rpmnew  copies  of  all  files  it
knows it should not overwrite. Of course you have to look at  all  those
files and merge any changes. A tedious and much forgotten job.

On FreeBSD there is mergemaster to do the job. It recently got ported to
OpenBSD and also to Gentoo. Now there is also a  Linux  version  (not  a
port) :)

%prep
%setup -q
%patch -p1 -b .foo

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_sysconfdir,%_bindir}
install -m 755 %name $RPM_BUILD_ROOT%_bindir
install -m 644 %{name}rc $RPM_BUILD_ROOT%_sysconfdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL CHANGES
%config(noreplace) %_sysconfdir/%{name}rc
%_bindir/%name
