Summary:	Katalog is set of three bash scripts to manipulate CD catalogs
Summary(pl):	Katalog jest zbiorem trzech skryptów basha s³u¿±cych do manipulacji katalogami CD
Name:		katalog
Version:	1.8b
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.ceti.pl/eaquer/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.ceti.pl/eaquer/
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
%setup  -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_sysconfdir}}

install kat{add,ls,sch} $RPM_BUILD_ROOT%{_bindir}
install katalogrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/*
