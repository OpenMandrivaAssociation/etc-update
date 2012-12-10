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


%changelog
* Sat Jul 21 2012 Johnny A. Solbu <solbu@mandriva.org> 20020731-12
+ Revision: 810556
- Spec cleanup
- Fix Licence tag
- Add manpage, from Gentoo

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20020731-11mdv2011.0
+ Revision: 618238
- the mass rebuild of 2010.0 packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 20020731-10mdv2010.0
+ Revision: 435901
- rebuild
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 20020731-7mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 24 2007 Thierry Vignaud <tv@mandriva.org> 20020731-7mdv2008.0
+ Revision: 70941
- use %%mkrel
- Import etc-update



* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 20020731-6mdk
- Nonbirthday Rebuild
- spec files fixes

* Tue Oct 28 2003 Götz Waschk <waschk@linux-mandrake.com> 20020731-5mdk
- rebuild to fix broken changelog

* Sun Sep 07 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 20020731-3mdk
- add fixes from Luca Berra <bluca@vodka.it>

* Thu Aug 22 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 20020731-2mdk
- some %%instal simplification

* Wed Jul 31 2002 Han Boetes <han@linux-mandrake.com> 20020731-1mdk
- Bump to updated version from the maintainer. lol
- Removed obsoleted patch

* Tue May 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 20020214-2mdk
- rpmlint fixes
- force mv and cp by default [Patch0]
- gcc-3.1 build :-)

* Sat Feb 16 2002 Guillaume Rousse <g.rousse@linux-mandrake.org> 20020214-1mdk
- first mdk release
