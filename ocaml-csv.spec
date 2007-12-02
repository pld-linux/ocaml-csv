%define		ocaml_ver	1:3.10.0
Summary:	A library managing dates and times
Summary(pl.UTF-8):	Biblioteka do obsługi daty i czasu
Name:		ocaml-csv
Version:	1.1.6
Release:	1
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
The Calendar library is a library providing a set of operations
over dates and times.

%package devel
Summary:	A library managing dates and times
Summary(pl.UTF-8):	Biblioteka do obsługi daty i czasu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
The Calendar library is a library providing a set of operations
over dates and times.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{csv,stublibs}}

install csvtool $RPM_BUILD_ROOT%{_bindir}
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/csv

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
%{_libdir}/ocaml/csv/*.cm[ixa]*
%{_libdir}/ocaml/csv/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/csv
