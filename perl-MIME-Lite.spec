#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Lite
Summary:	MIME::Lite perl module
Summary(pl.UTF-8):	Moduł perla MIME::Lite
Name:		perl-MIME-Lite
Version:	3.021
Release:	1
# same as perl
License:	GPL v1+ or Artisric
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b3f4b9b3f8a0023dbc62859ef9a775f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Lite is a simple, standalone module for generating MIME messages.

%description -l pl.UTF-8
MIME::Lite jest prostym, samodzielnym modułem służącym do generowania
wiadomości w formacie MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples
%{perl_vendorlib}/MIME/Lite.pm
%{_mandir}/man3/*
