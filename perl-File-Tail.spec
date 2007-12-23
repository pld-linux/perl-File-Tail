#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Tail
Summary:	File::Tail Perl module - reading from continuously updated files
Summary(pl.UTF-8):	Moduł Perla File::Tail - czytanie z ciągle uaktualnianych plików
Name:		perl-File-Tail
Version:	0.99.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef0fb7bcb4181ba593f4a09940f61d1c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Tail is a Perl tail. The primary purpose of File::Tail is
reading and analysing log files while they are being written, which is
especialy useful if you are monitoring the logging process with a tool
like Tobias Oetiker's MRTG.

%description -l pl.UTF-8
File::Tail to 'tail' dla Perla. Głównym przeznaczeniem modułu jest
czytanie i analizowanie plików logów podczas gdy są zapisywane, co
jest szczególnie przydatne przy monitorowaniu procesu logowania przy
użyciu narzędzi takich jak MRTG Tobiasa Oetikera.

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
