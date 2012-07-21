Name:		etc-update
Version:	20020731
Release:	12
Summary:	Mergemaster for Linux
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.1
Patch0:		etc-update-foo.patch.bz2
URL:		http://www.xs4all.nl/~hanb/software
License:	GPLv2+
Group:		System/Configuration/Packaging
BuildArch:	noarch

%description
After an update with urpmi rpm makes .rpmnew  copies  of  all  files  it
knows it should not overwrite. Of course you have to look at  all  those
files and merge any changes. A tedious and much forgotten job.


%prep
%setup -q
%patch0 -p1 -b .foo

%build

%install
install -m 755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m 644 %{name}rc -D %{buildroot}%{_sysconfdir}/%{name}rc
install -m 644 %{SOURCE1} -D %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc CHANGES
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
