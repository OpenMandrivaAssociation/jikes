Summary:	Java source to bytecode compiler
Name:		jikes
Version:	1.23
Release:	0.20050308.6
License:	IBM Public License
Group:		Development/Java
Url:		http://ibm.com/developerworks/opensource/jikes/
Source0:	http://oss.software.ibm.com/pub/jikes/%{version}/%{name}-cvs.tar.bz2
%rename		guavac

%description
The IBM Jikes compiler translates Java source files to bytecode. It
also supports incremental compilation and automatic makefile generation,
and is maintained by the Jikes Project:
  http://ibm.com/developerworks/opensource
  
%prep
%setup -qn %{name}

%build
%configure2_5x --enable-source15
%make

%install
%makeinstall
rm -rf %{buildroot}%{_datadir}/doc


%files
%doc README AUTHORS ChangeLog NEWS TODO INSTALL
%doc doc/*.htm*
%doc %{_mandir}/man1/jikes.1*
%{_bindir}/jikes
%{_includedir}/jikesapi.h

