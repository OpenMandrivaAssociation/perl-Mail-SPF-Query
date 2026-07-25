%define modname	Mail-SPF-Query
%define modver	1.999.1

Summary:	Perl implementation of querying Sender Policy Framework and Sender ID
Name:		perl-%{modname}
Version:	%{modver}
Release:	19
License:	BSD
Group:		Development/Perl
Url:		https://metacpan.org/dist/Mail-SPF-Query
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMEHNLE/mail-spf-query/Mail-SPF-Query-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Mail::SPF)
BuildRequires:	perl(Sys::Hostname::Long)
BuildRequires:	perl(Net::CIDR::Lite)
BuildRequires:	perl-devel

%description
Mail::SPF::Query is an object-oriented Perl implementation of the Sender Policy
Framework (SPF) e-mail sender authentication system <http://www.openspf.org>.

It supports both the TXT and SPF RR types as well as both SPFv1 (v=spf1) and
Sender ID (spf2.0) records, and it is fully compliant to RFCs 4408 and 4406.
(It does not however implement the patented PRA address selection algorithm
described in RFC 4407.)

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL installdirs=vendor
%make

%check
#make test

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/spfquery
%{_bindir}/spfd
%{perl_vendorlib}/Mail/SPF/Query.pm
%{_mandir}/man1/spfd.1*
%{_mandir}/man1/spfquery.1*
%{_mandir}/man3/Mail::SPF::Query.3pm*

