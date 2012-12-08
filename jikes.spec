%define name	jikes
%define version 1.23
%define release 0.20050308.6

Summary: 	Java source to bytecode compiler
Name: 		%{name}
Version:	%{version}
Release: 	%mkrel %{release}
License: 	IBM Public License
Group: 		Development/Java
Provides: 	guavac
Obsoletes: 	guavac
URL: 		http://ibm.com/developerworks/opensource/jikes/
Source0: 	http://oss.software.ibm.com/pub/jikes/%{version}/%{name}-cvs.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The IBM Jikes compiler translates Java source files to bytecode. It
also supports incremental compilation and automatic makefile generation,
and is maintained by the Jikes Project:
  http://ibm.com/developerworks/opensource
  
%prep
%setup -q -n %{name}

%build
%configure2_5x --enable-source15
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{_datadir}/doc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO INSTALL
%doc doc/*.htm*
%doc %{_mandir}/man1/jikes.1*
%{_bindir}/jikes
%{_includedir}/jikesapi.h



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.23-0.20050308.5mdv2011.0
+ Revision: 665828
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.23-0.20050308.4mdv2011.0
+ Revision: 606092
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.23-0.20050308.3mdv2010.1
+ Revision: 523085
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.23-0.20050308.2mdv2010.0
+ Revision: 425461
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.23-0.20050308.1mdv2008.1
+ Revision: 136504
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed May 24 2006 David Walluck <walluck@mandrake.org> 1.23-0.20050308.1mdk
- one-year rebuild
- use %%mkrel and %%configure_25x

* Fri Mar 25 2005 David Walluck <walluck@mandrake.org> 1.23-0.20041215.1mdk
- CVS 20041215
- fix doc removal

* Thu Feb 03 2005 Michael Scherer <misc@mandrake.org> 1.22-1mdk
- New release 1.22
- remove useless provides

* Fri Jun 04 2004 <lmontel@n2.mandrakesoft.com> 1.21-2mdk
- Rebuild

* Sat May 22 2004 Michael Scherer <misc@mandrake.org> 1.21-1mdk
- New release 1.21
- Remove Prefix
- better BuildRoot

* Mon May 10 2004 Damien Chaumette <dchaumette@mandrakesoft.com> 1.20-1mdk
- version 1.20

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.18-2mdk
- rebuild
- remove license.htm file in /usr/doc/, wrong location and it's already in %%doc

