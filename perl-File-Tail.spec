%include	/usr/lib/rpm/macros.perl
Summary:	File-Tail perl module
Summary(pl):	Modu³ perla File-Tail
Name:		perl-File-Tail
Version:	0.98
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Tail-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Time-HiRes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Tail - Perl tail.

%description -l pl
File-Tail - 'tail' dla Perla.

%prep
%setup -q -n File-Tail-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz logwatch select_demo
%{perl_sitelib}/File/Tail.pm
%{perl_sitelib}/auto/File/Tail
%{_mandir}/man3/*
