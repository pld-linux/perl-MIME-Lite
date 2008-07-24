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
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-Email-Date-Format}
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	perl-MailTools
Suggests:	perl-MIME-Base64
Suggests:	perl-MIME-Types
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
PERL_MM_USE_DEFAULT=yes \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

# package it or not?
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/changes.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README contrib
%{perl_vendorlib}/MIME/Lite.pm
%{_examplesdir}/%{name}
%{_mandir}/man3/*
