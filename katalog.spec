Summary:	Katalog is set of three bash scripts to manipulate CD catalogs
Summary(pl):	Katalog jest zbiorem trzech skryptów basha s³u¿±cych do manipulacji katalogami CD	
Name:		katalog
Version:	1.05
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	http://linux.sky.pl/maciek/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-PLD.patch
URL:		http://www.linux.sky.pl/maciek	
Requires:	sed
Requires:	findutils
Requires:	grep
Requires:	gzip
Requires:	bash
Requires:	textutils
Requires:	sh-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Katalog is set of three bash scripts to manipulate CD catalogs:
 - katadd - It makes list of files at CD and writes it to a file
 - katsch - It is used to search for an regexp in bases
 - katls - It gives you a list of currently installed databases

%description -l pl
Katalog jest zbiorem trzech skryptów basha s³u¿±cych do manipulacji
katalogami CD:
 - katadd - Tworzy listê plików znajduj±cych siê na CD i zapisuje j± do
   pliku
 - katsch - Jest u¿ywany do wyszukiwania wyra¿eñ regularnych w bazach
 - katls - Tworzy listê zainstalowanych baz danych

%prep
%setup  -q -c %{name}-%{version}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_sysconfdir}}
install kat{add,ls,sch} $RPM_BUILD_ROOT%{_bindir}
install katalogrc $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*
%doc *gz
