Name:       waypipe

%define __meson_auto_features disabled

%if 0%{?_chum}
BuildRequires: lz4-devel
%endif

%if 0%{?sailfishos_version} >= 40400
BuildRequires: pkgconfig(libzstd)
%define zstd_build enabled
%else
%define zstd_build disabled
%endif

Summary:    Network transparency with Wayland
# Also  update DescriptionMD below:
Version:    0.11.3
Release:    0
License:    GPLv3
URL:        https://gitlab.freedesktop.org/mstoeckl/waypipe/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  sailfish-version > 3.4.0
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja

%description
%{summary}.


%package c
Summary:    Network transparency with Wayland
License:    MIT
Group:      Applications
Provides:   waypipe-bin
Obsoletes:  waypipe <= 0.9.2
Obsoletes:  waypipe >= 0.8.6

%description c
waypipe is a proxy for Wayland clients.

It forwards Wayland messages and serializes changes to shared
memory buffers over a single socket. This makes application
forwarding similar to ssh -X feasible.

%if 0%{?_chum}
Title: Waypipe
Type: console-application
DeveloperName: M. Stoeckl
PackagedBy: nephros
Categories:
 - Networking
 - Utility
Custom:
  Repo: %{url}
  PackagingRepo: https://github.com/sailfishos-chum/waypipe
  DescriptionMD: https://gitlab.freedesktop.org/mstoeckl/waypipe/-/raw/v0.11.3/README.md
PackageIcon: https://gitlab.freedesktop.org/uploads/-/system/project/avatar/3237/waypipe.png
Links:
  Homepage: https://mstoeckl.com/notes/gsoc/blog.html
  Help: https://forum.sailfishos.org/t/fun-with-remote-wayland-waypipe/16997
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

%build
%__meson setup %{_vpath_builddir} \
    --buildtype=plain \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --includedir=%{_includedir} \
    --datadir=%{_datadir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --localedir=%{_datadir}/locale \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --wrap-mode=%{__meson_wrap_mode} \
    --auto-features=%{__meson_auto_features} \
    -Dbuild_c=true \
    -Dbuild_rs=false \
    -Dtests=false \
    -Dwith_video=enabled \
    -Dwith_dmabuf=disabled \
    -Dwith_vaapi=disabled \
    -Dman-pages=disabled \
    -Dwith_zstd=%{zstd_build} \
    -Dwith_neon_opts=%{?arm64:true}%{!?arm64:false} \
    -Dwith_lz4=%{?_chum:enabled}%{!?_chum:disabled} \
    -Dwith_systemtap=false \
    -Dwith_secctx=enabled \
    %{nil}

pushd %{_vpath_builddir}
%ninja_build

%install
%meson_install

%files c
%license LICENSE.MIT
%{_bindir}/waypipe-c
