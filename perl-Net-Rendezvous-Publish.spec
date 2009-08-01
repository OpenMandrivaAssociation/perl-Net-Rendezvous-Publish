%define upstream_name    Net-Rendezvous-Publish
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module to publish Rendezvous services 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Class::Accessor::Lvalue) 
BuildRequires:  perl(Module::Pluggable)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
# (misc) so far,only howl backend is packaged
# maybe splitting the null backend would be cleaner ?
Requires:    perl-Net-Rendezvous-Publish-Backend

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*
