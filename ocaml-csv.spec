%define		ocaml_ver	1:3.10.0
Summary:	A library for handling Comma Separated Value (CSV) File Format
Summary(pl.UTF-8):	Biblioteka do obsługi plików CSV
Name:		ocaml-csv
Version:	1.1.6
Release:	3
License:	LGPL + OCaml linking exception
Group:		Libraries
URL:		http://merjis.com/developers/csv
Source0:	http://merjis.com/_file/%{name}-%{version}.tar.gz
# Source0-md5:	a91851438f9540b1a445087a4d409507
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library can read and write CSV files, including all extensions
used by Excel - eg. quotes, newlines, 8 bit characters in fields,
"0 etc.
The library comes with a handy command line tool called csvtool
for handling CSV files from shell scripts.

%package devel
Summary:	A library for handling Comma Separated Value (CSV) File Format
Summary(pl.UTF-8):	Biblioteka do obsługi plików CSV
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
This library can read and write CSV files, including all extensions
used by Excel - eg. quotes, newlines, 8 bit characters in fields,
"0 etc.
The library comes with a handy command line tool called csvtool
for handling CSV files from shell scripts.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{csv,stublibs}}

install csvtool $RPM_BUILD_ROOT%{_bindir}
install csv.cm[ixa]* csv.a $RPM_BUILD_ROOT%{_libdir}/ocaml/csv

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r test* example.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/csv
echo 'version="%{version}"' >> META
echo 'archive(byte)="csv.cma"' >> META
echo 'archive(native)="csv.cmxa"' >> META
echo 'directory = "+csv"' >> META
install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/csv

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc *.mli
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ocaml/csv
%{_libdir}/ocaml/csv/*.cm[ixa]*
%{_libdir}/ocaml/csv/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/csv
