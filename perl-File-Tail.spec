#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Tail
Summary:	File::Tail Perl module
Summary(cs):	Modul File::Tail pro Perl
Summary(da):	Perlmodul File::Tail
Summary(de):	File::Tail Perl Modul
Summary(es):	Módulo de Perl File::Tail
Summary(fr):	Module Perl File::Tail
Summary(it):	Modulo di Perl File::Tail
Summary(ja):	File::Tail Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	File::Tail ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul File::Tail
Summary(pl):	Modu³ Perla File::Tail
Summary(pt):	Módulo de Perl File::Tail
Summary(pt_BR):	Módulo Perl File::Tail
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl File::Tail
Summary(sv):	File::Tail Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl File::Tail
Summary(zh_CN):	File::Tail Perl Ä£¿é
Name:		perl-File-Tail
Version:	0.98
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Time-HiRes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Tail - Perl tail.

%description -l pl
File::Tail - 'tail' dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install logwatch select_demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/File/Tail.pm
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/File
#%dir %{perl_sitelib}/auto/File/Tail
#%{perl_sitelib}/auto/File/Tail/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
