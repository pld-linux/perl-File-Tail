%include	/usr/lib/rpm/macros.perl
Summary:	File-Tail perl module
Summary(pl):	Modu³ perla File-Tail
Name:		perl-File-Tail
Version:	0.95
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Tail-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Time-HiRes
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Tail - Perl tail.

%description -l pl
File-Tail - 'tail' dla Perla.

%prep
%setup -q -n File-Tail-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/Tail
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz logwatch select_demo

%{perl_sitelib}/File/Tail.pm
%{perl_sitelib}/auto/File/Tail
%{perl_sitearch}/auto/File/Tail

%{_mandir}/man3/*
