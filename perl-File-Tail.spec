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
Summary(es):	M�dulo de Perl File::Tail
Summary(fr):	Module Perl File::Tail
Summary(it):	Modulo di Perl File::Tail
Summary(ja):	File::Tail Perl �⥸�塼��
Summary(ko):	File::Tail �� ����
Summary(no):	Perlmodul File::Tail
Summary(pl):	Modu� Perla File::Tail
Summary(pt):	M�dulo de Perl File::Tail
Summary(pt_BR):	M�dulo Perl File::Tail
Summary(ru):	������ ��� Perl File::Tail
Summary(sv):	File::Tail Perlmodul
Summary(uk):	������ ��� Perl File::Tail
Summary(zh_CN):	File::Tail Perl ģ��
Name:		perl-File-Tail
Version:	0.98
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d16d67052577a5cdcde03d5cd2dc5569
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/File/Tail.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/File
#%dir %{perl_vendorlib}/auto/File/Tail
#%%{perl_vendorlib}/auto/File/Tail/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
