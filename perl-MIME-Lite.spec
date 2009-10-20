#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Lite
Summary:	MIME::Lite - low-calorie MIME generator
Summary(pl.UTF-8):	MIME::Lite - niskokaloryczny generator MIME
Name:		perl-MIME-Lite
Version:	3.027
Release:	1
# same as perl
License:	GPL v1+ or Artisric
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e857febd66c45f2a5919b031fbe70aa7
URL:		http://search.cpan.org/dist/MIME-Lite/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Email-Date-Format
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Email-Date-Format
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# package it or not?
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/changes.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README contrib
%{perl_vendorlib}/MIME/Lite.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
