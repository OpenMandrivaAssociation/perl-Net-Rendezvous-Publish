%define realname   Net-Rendezvous-Publish

Name:		perl-%{realname}
Version:    0.04
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Module to publish Rendezvous services 
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl(Class::Accessor::Lvalue) 
BuildRequires:  perl(Module::Pluggable)
BuildArch:      noarch
# (misc) so far,only howl backend is packaged
# maybe splitting the null backend would be cleaner ?
Requires:    perl-Net-Rendezvous-Publish-Backend

%description
Net::Rendezvous::Publish allows you to publish Zeroconf ( or Rendezvous, or
Bonjour ) services, using a mDNS responder

%prep
%setup -q -n %{realname}-%{version}

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

