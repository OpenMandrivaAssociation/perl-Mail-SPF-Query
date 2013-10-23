%define upstream_name    Mail-SPF-Query
%define upstream_version 1.999.1

Name:   	perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	Perl implementation of querying Sender Policy Framework and Sender ID
License:	BSD
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Mail::SPF) perl(Sys::Hostname::Long) perl(Net::CIDR::Lite) perl-devel
BuildArch:	noarch

%description
Mail::SPF::Query is an object-oriented Perl implementation of the Sender Policy
Framework (SPF) e-mail sender authentication system <http://www.openspf.org>.

It supports both the TXT and SPF RR types as well as both SPFv1 (v=spf1) and
Sender ID (spf2.0) records, and it is fully compliant to RFCs 4408 and 4406.
(It does not however implement the patented PRA address selection algorithm
described in RFC 4407.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL installdirs=vendor
%make

#check
#make test

%install
make install DESTDIR=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/spfquery
%_bindir/spfd
%_mandir/man1/spfd.1*
%_mandir/man1/spfquery.1*
%_mandir/man3/Mail::SPF::Query.3pm*
%perl_vendorlib/Mail/SPF/Query.pm


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.999.1-1
+ Revision: 803777
- import perl-Mail-SPF-Query

