%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Lite
Summary:	MIME::Lite perl module
Summary(pl):	Modu³ perla MIME::Lite
Name:		perl-MIME-Lite
Version:	2.117
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Lite is a simple, standalone module for generating MIME messages.

%description -l pl
MIME::Lite jest prostym, samodzielnym modu³em s³u¿±cym do generowania
wiadomo¶ci w formacie MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/MIME/*
%{perl_vendorlib}/MIME/Lite.pm
%{_mandir}/man3/*
