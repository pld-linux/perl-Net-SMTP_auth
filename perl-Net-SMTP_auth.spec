#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP_auth
Summary:	Simple Mail Transfer Protocol Client with AUTHentication
Summary(pl):	Klient SMTP (Simple Mail Transfer Protocol) z Autentykacj±
Name:		perl-Net-SMTP_auth
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	926e9885a45a190d9c991f138d448914
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
to and authenticate against SMTP servers. This documentation assumes
that you are familiar with the concepts of the SMTP protocol described
in RFC821 and with the AUTH service extension described in RFC2554.

A new Net::SMTP_auth object must be created with the new method. Once
this has been done, all SMTP commands are accessed through this
object.

The Net::SMTP_auth class is a subclass of Net::SMTP, which itself is a
subclass of Net::Cmd and IO::Socket::INET.

#%description -l pl
#TODO

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
