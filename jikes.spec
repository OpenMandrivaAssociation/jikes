%define name	jikes
%define version 1.23
%define release 0.20050308.5

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

