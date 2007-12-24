#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP_auth
Summary:	Simple Mail Transfer Protocol Client with AUTHentication
Summary(pl.UTF-8):	Klient SMTP (Simple Mail Transfer Protocol) z uwierzytelnianiem (SMTP AUTH)
Name:		perl-Net-SMTP_auth
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23a911893c92c7c26ab9a78882691d9c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Authen-SASL >= 2.03
BuildRequires:	perl-Digest-HMAC >= 1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a client interface to the SMTP and ESMTP
protocol AUTH service extension, enabling a perl5 application to talk
to and authenticate against SMTP servers.

The Net::SMTP_auth class is a subclass of Net::SMTP, which itself is a
subclass of Net::Cmd and IO::Socket::INET.

%description -l pl.UTF-8
Ten moduł implementuje interfejs kliencki do rozszerzenia AUTH
protokołów SMTP i ESMTP, umożliwiając perlowym aplikacjom rozmawianie
i uwierzytelnianie względem serwerów SMTP.

Klasa Net::SMTP_auth jest podklasą Net::SMTP, która z kolei jest
podklasą Net::Cmd i IO::Socket::INET.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/SMTP_auth.pm
%{_mandir}/man3/*
