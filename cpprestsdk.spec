Summary:	C++ Rest SDK
Summary(pl.UTF-8):	Pakiet programistyczny C++ Rest
Name:		cpprestsdk
Version:	2.10.19
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://github.com/microsoft/cpprestsdk/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a7f8a8b55cd2f799cb9d712f172b1af1
Patch0:		%{name}-truncation.patch
# https://github.com/microsoft/vcpkg/blob/master/ports/cpprestsdk/fix-asio-error.patch
Patch1:		%{name}-boost-asio.patch
Patch2:		%{name}-boost.patch
URL:		https://github.com/microsoft/cpprestsdk
BuildRequires:	boost-devel >= 1.66
BuildRequires:	cmake >= 3.9
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	websocketpp-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API
design. This project aims to help C++ developers connect to and
interact with services.

Note: cpprestsdk is in maintenance mode and is not recommended its use
in new projects. Maintainers will continue to fix critical bugs and
address security issues.

%description -l pl.UTF-8
C++ REST SDK to projekt Microsoftu do komunikacji chmurowej
klient-serwer w kodzie natywnym z użyciem nowoczesnego,
asynchronicznego projektu API C++. Celem jest pomoc programistom C++ w
łączeniu się i interakcji z usługami.

Uwaga: cpprestsdk jest w trybie utrzymania i nie jest zalecany do
użycia w nowych projektach. Błędy krytyczne i problemy z
bezpieczeństwem będą nadal rozwiązywane.

%package devel
Summary:	Header files for cpprest library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cpprest
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel >= 1.66
Requires:	libstdc++-devel >= 6:5

%description devel
Header files for cpprest library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cpprest.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS.txt README.md SECURITY.md ThirdPartyNotices.txt changelog.md license.txt
%{_libdir}/libcpprest.so.2.10

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcpprest.so
%{_includedir}/cpprest
%{_includedir}/pplx
%{_libdir}/cmake/cpprestsdk
