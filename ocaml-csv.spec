# TODO: optflags
#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	OCaml library for handling Comma Separated Value (CSV) File Format
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi plików CSV
Name:		ocaml-csv
Version:	1.1.7
Release:	7
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://merjis.com/_file/%{name}-%{version}.tar.gz
# Source0-md5:	3d0b5711c10b966686be1e1ee84e4aba
Patch0:		byte-only.patch
URL:		http://merjis.com/developers/csv
BuildRequires:	ocaml >= 1:3.10.0
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, "0 etc.

The library comes with a handy command line tool called csvtool
for handling CSV files from shell scripts.

%description -l pl.UTF-8
Ta biblioteka OCamla odczytuje i zapisuje pliki CSV, wraz ze
wszystkimi rozszerzeniami wykorzystywanymi przez Excela: cudzysłowami,
znakami 8-bitowymi w polach, "0 itp.

Do biblioteka załączone jest podręczne narzędzie działające z linii
poleceń o nazwie csvtool, służące do obsługi plików CSV ze skryptów
powłoki.

%package devel
Summary:	OCaml library for handling Comma Separated Value (CSV) File Format
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi plików CSV
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, "0 etc.

The library comes with a handy command line tool called csvtool
for handling CSV files from shell scripts.

%description devel -l pl.UTF-8
Ta biblioteka OCamla odczytuje i zapisuje pliki CSV, wraz ze
wszystkimi rozszerzeniami wykorzystywanymi przez Excela: cudzysłowami,
znakami 8-bitowymi w polach, "0 itp.

Do biblioteka załączone jest podręczne narzędzie działające z linii
poleceń o nazwie csvtool, służące do obsługi plików CSV ze skryptów
powłoki.

%prep
%setup -q
%if %{without ocaml_opt}
%patch0 -p1
%endif

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{csv,stublibs}}

install csvtool $RPM_BUILD_ROOT%{_bindir}
install csv.cm[ixa]* %{?with_ocaml_opt:csv.a} $RPM_BUILD_ROOT%{_libdir}/ocaml/csv

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r test* example.ml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/csv
echo 'directory = "+csv"' >> META
install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/csv

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc *.mli
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ocaml/csv
%{_libdir}/ocaml/csv/*.cma
%{_libdir}/ocaml/csv/*.cm[ix]
%if %{with ocaml_opt}
%{_libdir}/ocaml/csv/*.a
%{_libdir}/ocaml/csv/*.cmxa
%endif
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/csv
