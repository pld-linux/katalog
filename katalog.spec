
%define		_pre pre2
Summary:	Katalog is set of three bash scripts to manipulate CD catalogs
Summary(pl.UTF-8):	Katalog jest zbiorem trzech skryptów basha służących do manipulacji katalogami CD
Name:		katalog
Version:	1.10
Release:	0.%{_pre}.1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.ceti.pl/eaquer/%{name}/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	bd8f3ff80c7d512818340596a87665b2
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

%description -l pl.UTF-8
Katalog jest zbiorem trzech skryptów basha służących do manipulacji
katalogami CD:
 - katadd - Tworzy listę plików znajdujących się na CD i zapisuje ją do
   pliku
 - katsch - Jest używany do wyszukiwania wyrażeń regularnych w bazach
 - katls - Tworzy listę zainstalowanych baz danych

%prep
%setup  -q -n %{name}-%{version}%{_pre}

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
%doc README CHANGELOG katalogrc cgi/*
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/*
