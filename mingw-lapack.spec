%?mingw_package_header

%global commit d8574a9
%global snapshot .git20170208.%{commit}

Name:           mingw-lapack
Version:        3.7.0
Release:        2%{snapshot}%{?dist}
Summary:        MinGW port of Linear Algebra PACKage

License:        BSD
URL:            http://www.netlib.org/lapack/
# git clone https://github.com/Reference-LAPACK/lapack
# cd lapack
# git archive --prefix=lapack/ master | bzip2 >../lapack.tar.bz2
Source0:        lapack.tar.bz2
Patch0:         lapack-3.7.0-skip-cmake-build-type.patch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
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
%setup -qn lapack
%patch0 -p1

%build
%mingw_cmake -DLAPACKE=ON -DBUILD_TESTING=OFF
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

# Win32
%files -n mingw32-lapack
%{mingw32_bindir}/libblas.dll
%{mingw32_bindir}/liblapack.dll
%{mingw32_libdir}/libblas.dll.a
%{mingw32_libdir}/liblapack.dll.a
%{mingw32_libdir}/pkgconfig/lapack.pc
%{mingw32_libdir}/pkgconfig/blas.pc
%{mingw32_libdir}/cmake/lapack-%{version}/

# Win64
%files -n mingw64-lapack
%{mingw64_bindir}/libblas.dll
%{mingw64_bindir}/liblapack.dll
%{mingw64_libdir}/libblas.dll.a
%{mingw64_libdir}/liblapack.dll.a
%{mingw64_libdir}/pkgconfig/lapack.pc
%{mingw64_libdir}/pkgconfig/blas.pc
%{mingw64_libdir}/cmake/lapack-%{version}/

%changelog
* Wed Feb 08 2017 Jajauma's Packages <jajauma@yandex.ru> - 3.7.0-2.git20170208.d8574a9
- Rebase to git snapshot
- Enable LAPACKE (build fixed in git snapshot)
- Disable testing

* Tue Feb 07 2017 Jajauma's Packages <jajauma@yandex.ru> - 3.7.0-1
- Initial release
