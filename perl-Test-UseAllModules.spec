#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	UseAllModules
Summary:	Test::UseAllModules - do use_ok() for all the MANIFESTed modules
Summary(pl.UTF-8):	Test::UseAllModules - wykonaj use_ok() dla wszystkich modułów MANIFEST
Name:		perl-Test-UseAllModules
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3e9fb933c71f677ee584bca27191fa2
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Test-UseAllModules/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I'm sick of writing 00_load.t (or something like that) that'll do use_ok() for every module I write. I'm sicker of updating 00_load.t when I add another file to the distro. This module reads MANIFEST to find modules to be tested and does use_ok() for each of them. Now all you have to do is update MANIFEST. You don't have to modify the test any more (hopefully).

%description -l pl.UTF-8
Test::UseAllModules - wykonaj use_ok() dla wszystkich modułów MANIFEST

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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
