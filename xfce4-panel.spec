%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define major 4
%define api 2.0

%define libname	%mklibname xfce4panel- %{api} %{major}
%define develname %mklibname xfce4panel -d

%define gmajor	2.0
%define girname	%mklibname xfce4panel-gir %{gmajor}

%define _disable_rebuild_configure 1

Summary:	A Xfce panel
Name:		xfce4-panel
Version:	4.18.6
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://www.xfce.org
Source0:	https://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	intltool
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.12
BuildRequires:	pkgconfig(libxfconf-0) >=  4.13.3
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(exo-2) >= 0.10.3
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(garcon-1) >= 0.4.0
BuildRequires:	pkgconfig(garcon-gtk3-1)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	%{_lib}harfbuzz-gir-devel

Requires:	desktop-common-data
Obsoletes:	xfce-panel

%description
The Xfce 4 Panel supports multiple panels, with many options
for their position, appearance, transparency and behavior.
There are many items available by default to full fit a panel,
like application launchers with detachable menus, a graphical pager,
a tasklist, a clock, a system tray, a show/hide desktop switcher,
and even more. It offers an easy way to add items using a dialog,
and to move items accross different panels.

%package -n %{libname}
Summary:	Panel library for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	%{girname} = %{EVRD}
Obsoletes:	%{mklibname xfce4panel 1}
Obsoletes:	%{mklibname xfce4panel 2}
Obsoletes:	%{mklibname xfce4panel 3}
Obsoletes:	%{mklibname xfce4panel 4} < 4.10.1
Obsoletes:      %{_lib}xfce4panel-1.0_4 < 4.16.0-3
Obsoletes:      %{_lib}xfce4panel2.0_4 < 4.16.0-3

%description -n %{libname}
Panel library for the Xfce desktop environment.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.


%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname xfce4panel 1 -d} < 4.6.3-2

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=1

PLATFORM_LDFLAGS="-lm"

%configure \
	--disable-gtk-doc \
	--enable-gio-unix \
	--disable-static

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build LIBS="-lm"

%install
%make_install

# (tpg) this file is in mandriva-xfce-config package
#rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/*

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS
%dir %{_libdir}/xfce4/panel
%dir %{_libdir}/xfce4/panel/plugins
%dir %{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel/plugins
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_sysconfdir}/xdg/xfce4/panel/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper-*
%{_datadir}/gtk-doc/html/libxfce4panel-*

%files -n %{libname}
%{_libdir}/libxfce4panel-%{api}.so.%{major}{,.*}

%files -n %{girname}
%{_libdir}/girepository-1.0/Libxfce4panel-%{gmajor}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libxfce4panel-*.so
%{_libdir}/pkgconfig/libxfce4panel-*.pc
%{_includedir}/xfce4/libxfce4panel-*/
%{_datadir}/gir-1.0/Libxfce4panel-%{gmajor}.gir
%{_datadir}/vala/vapi/libxfce4panel-%{api}.{deps,vapi}
