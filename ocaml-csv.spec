# TODO: optflags
#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	OCaml library for handling Comma Separated Value (CSV) File Format
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi plików CSV
Name:		ocaml-csv
Version:	2.4
Release:	1
License:	LGPL v2.1 + OCaml linking exception
Group:		Libraries
#Source0Download: https://github.com/Chris00/ocaml-csv/releases
Source0:	https://github.com/Chris00/ocaml-csv/releases/download/%{version}/csv-%{version}.tbz
# Source0-md5:	e3275233a8d5ad809062f3eead997b7b
URL:		https://github.com/Chris00/ocaml-csv
BuildRequires:	ocaml >= 1:4.03.0
BuildRequires:	ocaml-dune-devel
BuildRequires:	ocaml-lwt-devel
BuildRequires:	ocaml-uutf-devel
%requires_eq	ocaml-runtime
Conflicts:	ocaml-csv-devel < 2.4
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

Do biblioteki dołączone jest podręczne narzędzie działające z linii
poleceń o nazwie csvtool, służące do obsługi plików CSV ze skryptów
powłoki.

%package devel
Summary:	OCaml library for handling Comma Separated Value (CSV) File Format - development part
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi plików CSV - część programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using csv
library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki csv.

%package lwt
Summary:	OCaml library to read and write CSV files - LWT version
Summary(pl.UTF-8):	Biblioteka OCamla do odczytu i zapisu plików CSV - wersja LWT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-lwt

%description lwt
OCaml library to read and write CSV files - LWT version.

%description lwt -l pl.UTF-8
Biblioteka OCamla do odczytu i zapisu plików CSV - wersja LWT.

%package lwt-devel
Summary:	OCaml library to read and write CSV files - LWT version, development part
Summary(pl.UTF-8):	Biblioteka OCamla do odczytu i zapisu plików CSV - wersja LWT, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-lwt = %{version}-%{release}
Requires:	ocaml-lwt-devel

%description lwt-devel
This package contains files needed to develop OCaml programs using
csv-lwt library.

%description lwt-devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki csv-lwt.

%prep
%setup -q -n csv-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/{csv,csv-lwt}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/{csv,csv-lwt,csvtool}

# useless: just tool, not lib
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/ocaml/csvtool/{META,dune-package,opam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%attr(755,root,root) %{_bindir}/csvtool
%dir %{_libdir}/ocaml/csv
%{_libdir}/ocaml/csv/META
%{_libdir}/ocaml/csv/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/csv/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/csv/*.cmi
%{_libdir}/ocaml/csv/*.cmt
%{_libdir}/ocaml/csv/*.cmti
%{_libdir}/ocaml/csv/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/csv/*.a
%{_libdir}/ocaml/csv/*.cmx
%{_libdir}/ocaml/csv/*.cmxa
%endif
%{_libdir}/ocaml/csv/dune-package
%{_libdir}/ocaml/csv/opam
%{_examplesdir}/%{name}-%{version}

%files lwt
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/csv-lwt
%{_libdir}/ocaml/csv-lwt/META
%{_libdir}/ocaml/csv-lwt/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/csv-lwt/*.cmxs
%endif

%files lwt-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/csv-lwt/*.cmi
%{_libdir}/ocaml/csv-lwt/*.cmt
%{_libdir}/ocaml/csv-lwt/*.cmti
%{_libdir}/ocaml/csv-lwt/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/csv-lwt/*.a
%{_libdir}/ocaml/csv-lwt/*.cmx
%{_libdir}/ocaml/csv-lwt/*.cmxa
%endif
%{_libdir}/ocaml/csv-lwt/dune-package
%{_libdir}/ocaml/csv-lwt/opam
