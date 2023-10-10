# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       waypipe

# >> macros
# << macros
%define __meson_auto_features disabled
%define spectacle_bug hack_fix
%if 0%{?_chum}
BuildRequires: lz4-devel
%endif

Summary:    Network transparency with Wayland
Version:    0.8.6
Release:    0
Group:      Applications
License:    ASL 2.0
URL:        https://gitlab.freedesktop.org/mstoeckl/waypipe/
Source0:    %{name}-%{version}.tar.bz2
Source100:  waypipe.yaml
Source101:  waypipe-rpmlintrc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  ffmpeg-devel >= 3.1

%description
%{summary}.

%if "%{?vendor}" == "chum"
Title: Waypipe
Type: console-application
DeveloperName: M. Stoeckl
PackagedBy: nephros
Categories:
 - Utility
Custom:
  Repo: %{url}
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre

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
-Dwith_zstd=enabled \
-Dwith_video=enabled \
-Dwith_dmabuf=disabled \
-Dwith_vaapi=disabled \
-Dman-pages=disabled \
-Dwith_neon_opts=%{?arm64:true}%{!?arm64:false} \
-Dwith_lz4=%{?_chum:enabled}%{!?_chum:disabled} \
-Dwith_systemtap=false
#%%meson -Dwith_dmabuf=disabled -Dwith_vaapi=disabled -Dman-pages=disabled -Dwith_systemtap=false
pushd %{_vpath_builddir}
#%%meson_build
%ninja_build
#popd
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
#%%ninja_install -C build
%meson_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
# >> files
# << files
