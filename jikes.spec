Summary:	Java source to bytecode compiler
Name:		jikes
Version:	1.23
Release:	0.20050308.15
License:	IBM Public License
Group:		Development/Java
Url:		http://sourceforge.net/projects/jikes
Source0:	%{name}-cvs.tar.bz2

%description
The Jikes compiler translates Java source files to bytecode.

While Jikes is obsolete and unmaintained upstream since 2005,
it is still needed to bootstrap modern versions of Java.

%prep
%autosetup -n %{name}

%build
%configure --enable-source15
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc


%files
%doc README AUTHORS ChangeLog NEWS TODO INSTALL
%doc doc/*.htm*
%doc %{_mandir}/man1/jikes.1*
%{_bindir}/jikes
%{_includedir}/jikesapi.h
