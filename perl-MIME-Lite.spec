%include	/usr/lib/rpm/macros.perl
Summary:	MIME-Lite perl module
Summary(pl):	Modu³ perla MIME-Lite
Name:		perl-MIME-Lite
Version:	2.102
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/MIME-Lite-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libnet
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME-Lite is a simple, standalone module for generating MIME messages.

%description -l pl
MIME-Lite jest prostym, samodzielnym modu³em s³u¿±cym do generowania
wiadomo¶ci w formacie MIME.

%prep
%setup -q -n MIME-Lite-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MIME/Lite
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz docs/MIME/*

%{perl_sitelib}/MIME/Lite.pm
%{perl_sitearch}/auto/MIME/Lite

%{_mandir}/man3/*
