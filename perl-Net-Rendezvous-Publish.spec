%define upstream_name    Net-Rendezvous-Publish
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Module to publish Rendezvous services 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Lvalue)
BuildRequires:	perl(Module::Pluggable)
BuildArch:	noarch
Requires:	perl-Net-Rendezvous-Publish-Backend

%description
Net::Rendezvous::Publish allows you to publish Zeroconf ( or Rendezvous, or
Bonjour ) services, using a mDNS responder

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 406174
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.04-5mdv2009.0
+ Revision: 241789
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-3mdv2008.0
+ Revision: 25202
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Wed Feb 01 2006 Michael Scherer <misc@mandriva.org> 0.04-1mdk
- New release 0.04

* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.03-3mdk
- Do not ship empty dir

* Fri Sep 23 2005 Michael Scherer <misc@mandriva.org> 0.03-2mdk
- requires a backend module ( such as howl backend, or avahi, once someone write it )

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 0.03-1mdk
- First mandriva package

