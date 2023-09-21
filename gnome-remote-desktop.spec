#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-remote-desktop
Version  : 44.2
Release  : 8
URL      : https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/archive/44.2/gnome-remote-desktop-44.2.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/archive/44.2/gnome-remote-desktop-44.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-remote-desktop-bin = %{version}-%{release}
Requires: gnome-remote-desktop-data = %{version}-%{release}
Requires: gnome-remote-desktop-libexec = %{version}-%{release}
Requires: gnome-remote-desktop-license = %{version}-%{release}
Requires: gnome-remote-desktop-locales = %{version}-%{release}
Requires: gnome-remote-desktop-man = %{version}-%{release}
Requires: gnome-remote-desktop-services = %{version}-%{release}
BuildRequires : FreeRDP-dev
BuildRequires : asciidoc
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : fuse-dev
BuildRequires : libgudev-dev
BuildRequires : libnotify-dev
BuildRequires : pkgconfig(ffnvcodec)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libvncclient)
BuildRequires : pkgconfig(tss2-esys)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GNOME Remote Desktop
Remote desktop daemon for GNOME using pipewire.

%package bin
Summary: bin components for the gnome-remote-desktop package.
Group: Binaries
Requires: gnome-remote-desktop-data = %{version}-%{release}
Requires: gnome-remote-desktop-libexec = %{version}-%{release}
Requires: gnome-remote-desktop-license = %{version}-%{release}
Requires: gnome-remote-desktop-services = %{version}-%{release}

%description bin
bin components for the gnome-remote-desktop package.


%package data
Summary: data components for the gnome-remote-desktop package.
Group: Data

%description data
data components for the gnome-remote-desktop package.


%package libexec
Summary: libexec components for the gnome-remote-desktop package.
Group: Default
Requires: gnome-remote-desktop-license = %{version}-%{release}

%description libexec
libexec components for the gnome-remote-desktop package.


%package license
Summary: license components for the gnome-remote-desktop package.
Group: Default

%description license
license components for the gnome-remote-desktop package.


%package locales
Summary: locales components for the gnome-remote-desktop package.
Group: Default

%description locales
locales components for the gnome-remote-desktop package.


%package man
Summary: man components for the gnome-remote-desktop package.
Group: Default

%description man
man components for the gnome-remote-desktop package.


%package services
Summary: services components for the gnome-remote-desktop package.
Group: Systemd services
Requires: systemd

%description services
services components for the gnome-remote-desktop package.


%prep
%setup -q -n gnome-remote-desktop-44.2
cd %{_builddir}/gnome-remote-desktop-44.2
pushd ..
cp -a gnome-remote-desktop-44.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685511302
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfdk_aac=false \
-Dvnc=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfdk_aac=false \
-Dvnc=true  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-remote-desktop
cp %{_builddir}/gnome-remote-desktop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-remote-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-remote-desktop
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/grdctl
/usr/bin/grdctl

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
/usr/share/gnome-remote-desktop/grd-cuda-avc-utils_30.ptx
/usr/share/gnome-remote-desktop/grd-cuda-damage-utils_30.ptx

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-remote-desktop-daemon
/usr/libexec/gnome-remote-desktop-daemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-remote-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/grdctl.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-remote-desktop.service

%files locales -f gnome-remote-desktop.lang
%defattr(-,root,root,-)

