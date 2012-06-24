%include	/usr/lib/rpm/macros.perl
Summary:	MIME-Lite perl module
Summary(pl):	Modu� perla MIME-Lite
Name:		perl-MIME-Lite
Version:	2.117
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME/MIME-Lite-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME-Lite is a simple, standalone module for generating MIME messages.

%description -l pl
MIME-Lite jest prostym, samodzielnym modu�em s�u��cym do generowania
wiadomo�ci w formacie MIME.

%prep
%setup -q -n MIME-Lite-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/MIME/*
%{perl_sitelib}/MIME/Lite.pm
%{_mandir}/man3/*
