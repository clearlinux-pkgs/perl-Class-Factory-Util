#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Class-Factory-Util
Version  : 1.7
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Class-Factory-Util-1.7.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Class-Factory-Util-1.7.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libclass-factory-util-perl/libclass-factory-util-perl_1.7-3.debian.tar.xz
Summary  : Provide utility methods for factory classes
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Class-Factory-Util-license = %{version}-%{release}
Requires: perl-Class-Factory-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Class::Factory::Util - Provide utility methods for factory classes
SYNOPSIS
package My::Class;

%package dev
Summary: dev components for the perl-Class-Factory-Util package.
Group: Development
Provides: perl-Class-Factory-Util-devel = %{version}-%{release}
Requires: perl-Class-Factory-Util = %{version}-%{release}

%description dev
dev components for the perl-Class-Factory-Util package.


%package license
Summary: license components for the perl-Class-Factory-Util package.
Group: Default

%description license
license components for the perl-Class-Factory-Util package.


%package perl
Summary: perl components for the perl-Class-Factory-Util package.
Group: Default
Requires: perl-Class-Factory-Util = %{version}-%{release}

%description perl
perl components for the perl-Class-Factory-Util package.


%prep
%setup -q -n Class-Factory-Util-1.7
cd %{_builddir}
tar xf %{_sourcedir}/libclass-factory-util-perl_1.7-3.debian.tar.xz
cd %{_builddir}/Class-Factory-Util-1.7
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Class-Factory-Util-1.7/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Factory-Util
cp %{_builddir}/Class-Factory-Util-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Factory-Util/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Class-Factory-Util/5f07578ffdd10f877b0f3dd14d1681540d7b2368 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Factory::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Factory-Util/5f07578ffdd10f877b0f3dd14d1681540d7b2368
/usr/share/package-licenses/perl-Class-Factory-Util/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
