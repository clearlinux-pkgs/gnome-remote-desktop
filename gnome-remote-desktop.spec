#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: 5424026
#
Name     : gnome-remote-desktop
Version  : 47.2
Release  : 26
URL      : https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/archive/47.2/gnome-remote-desktop-47.2.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/archive/47.2/gnome-remote-desktop-47.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-remote-desktop-bin = %{version}-%{release}
Requires: gnome-remote-desktop-config = %{version}-%{release}
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
BuildRequires : fdk-aac-dev
BuildRequires : fuse-dev
BuildRequires : libgudev-dev
BuildRequires : libnotify-dev
BuildRequires : mutter
BuildRequires : mutter-dev
BuildRequires : opus-dev
BuildRequires : pkgconfig(ffnvcodec)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libei-1.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libvncclient)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(tss2-esys)
BuildRequires : polkit-dev
BuildRequires : wireplumber-dev
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
Requires: gnome-remote-desktop-config = %{version}-%{release}
Requires: gnome-remote-desktop-license = %{version}-%{release}
Requires: gnome-remote-desktop-services = %{version}-%{release}

%description bin
bin components for the gnome-remote-desktop package.


%package config
Summary: config components for the gnome-remote-desktop package.
Group: Default

%description config
config components for the gnome-remote-desktop package.


%package data
Summary: data components for the gnome-remote-desktop package.
Group: Data

%description data
data components for the gnome-remote-desktop package.


%package libexec
Summary: libexec components for the gnome-remote-desktop package.
Group: Default
Requires: gnome-remote-desktop-config = %{version}-%{release}
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
%setup -q -n gnome-remote-desktop-47.2
cd %{_builddir}/gnome-remote-desktop-47.2
pushd ..
cp -a gnome-remote-desktop-47.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732553989
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvnc=true  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvnc=true  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-remote-desktop
cp %{_builddir}/gnome-remote-desktop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-remote-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-remote-desktop
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/grdctl
/usr/bin/grdctl

%files config
%defattr(-,root,root,-)
/usr/lib/sysusers.d/gnome-remote-desktop-sysusers.conf
/usr/lib/tmpfiles.d/gnome-remote-desktop-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.RemoteDesktop.Handover.desktop
/usr/share/dbus-1/system-services/org.gnome.RemoteDesktop.Configuration.service
/usr/share/dbus-1/system.d/org.gnome.RemoteDesktop.conf
/usr/share/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
/usr/share/gnome-remote-desktop/grd-cuda-avc-utils_30.ptx
/usr/share/gnome-remote-desktop/grd-cuda-damage-utils_30.ptx
/usr/share/gnome-remote-desktop/grd.conf
/usr/share/polkit-1/actions/org.gnome.remotedesktop.configure-system-daemon.policy
/usr/share/polkit-1/actions/org.gnome.remotedesktop.enable-system-daemon.policy
/usr/share/polkit-1/rules.d/20-gnome-remote-desktop.rules

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-remote-desktop-configuration-daemon
/V3/usr/libexec/gnome-remote-desktop-daemon
/V3/usr/libexec/gnome-remote-desktop-enable-service
/usr/libexec/gnome-remote-desktop-configuration-daemon
/usr/libexec/gnome-remote-desktop-daemon
/usr/libexec/gnome-remote-desktop-enable-service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-remote-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/grdctl.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/gnome-remote-desktop-configuration.service
/usr/lib/systemd/system/gnome-remote-desktop.service
/usr/lib/systemd/user/gnome-remote-desktop-handover.service
/usr/lib/systemd/user/gnome-remote-desktop-headless.service
/usr/lib/systemd/user/gnome-remote-desktop.service

%files locales -f gnome-remote-desktop.lang
%defattr(-,root,root,-)

