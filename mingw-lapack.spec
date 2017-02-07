%?mingw_package_header

Name:           mingw-lapack
Version:        3.7.0
Release:        1%{?dist}
Summary:        MinGW port of Linear Algebra PACKage

License:        BSD
URL:            http://www.netlib.org/lapack/
Source0:        http://www.netlib.org/lapack/lapack-%{version}.tgz
Patch0:         lapack-dont-force-release-build-type.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw64-gcc-gfortran
BuildRequires:  cmake
BuildRequires:  python >= 2.7

BuildArch:      noarch

%description
MinGW Windows port of Linear Algebra PACKage.

# Win32
%package -n mingw32-lapack
Summary:        32-bit version of Linear Algebra PACKage for Windows

%description -n mingw32-lapack
%mingw32_description

# Win64
%package -n mingw64-lapack
Summary:        64-bit version of Linear Algebra PACKage for Windows

%description -n mingw64-lapack
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn lapack-%{version}
%patch0 -p1

%build
%mingw_cmake -DBUILD_TESTING=OFF
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

# Win32
%files -n mingw32-lapack
%{mingw32_bindir}/libblas.dll
%{mingw32_bindir}/liblapack.dll
# %{mingw32_bindir}/libtmglib.dll
%{mingw32_libdir}/libblas.dll.a
%{mingw32_libdir}/liblapack.dll.a
# %{mingw32_libdir}/libtmglib.dll.a
%{mingw32_libdir}/pkgconfig/lapack.pc
%{mingw32_libdir}/pkgconfig/blas.pc
%{mingw32_libdir}/cmake/lapack-%{version}/

# Win64
%files -n mingw64-lapack
%{mingw64_bindir}/libblas.dll
%{mingw64_bindir}/liblapack.dll
# %{mingw64_bindir}/libtmglib.dll
%{mingw64_libdir}/libblas.dll.a
%{mingw64_libdir}/liblapack.dll.a
# %{mingw64_libdir}/libtmglib.dll.a
%{mingw64_libdir}/pkgconfig/lapack.pc
%{mingw64_libdir}/pkgconfig/blas.pc
%{mingw64_libdir}/cmake/lapack-%{version}/

%changelog
* Tue Feb 07 2017 Jajauma's Packages <jajauma@yandex.ru> - 3.7.0-1
- Initial release
