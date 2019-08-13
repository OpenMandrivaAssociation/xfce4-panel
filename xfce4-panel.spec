%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define major 4
%define api 1.0
%define gtk3api 2.0

%define libname	%mklibname xfce4panel- %{api} %{major}
%define gtk3libname %mklibname xfce4panel %{gtk3api} %{major}
%define develname %mklibname xfce4panel -d

%define _disable_rebuild_configure 1

Summary:	A Xfce panel
Name:		xfce4-panel
Version:	4.14.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(exo-1) >= 0.10.3
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(garcon-1) >= 0.4.0
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
Obsoletes:	%{mklibname xfce4panel 1}
Obsoletes:	%{mklibname xfce4panel 2}
Obsoletes:	%{mklibname xfce4panel 3}
Obsoletes:	%{mklibname xfce4panel 4} < 4.10.1

%description -n %{libname}
Panel library for the Xfce desktop environment.

%package -n %{gtk3libname}
Summary:	Panel library (GTK3 version) for the Xfce desktop environment
Group:		Graphical desktop/Xfce

%description -n %{gtk3libname}
Panel library (GTK3 version) for the Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	%{libname} = %{version}
Requires:	%{gtk3libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname xfce4panel 1 -d} < 4.6.3-2

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 xdt-autogen

PLATFORM_LDFLAGS="-lm"

%configure \
	--disable-gtk-doc \
	--enable-gio-unix \
	--enable-gtk3 \
	--disable-static

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

# (tpg) this file is in mandriva-xfce-config package
rm -rf %{buildroot}%{_sysconfdir}/xdg/xfce4/panel/*

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS
%dir %{_libdir}/xfce4/panel
%dir %{_libdir}/xfce4/panel/plugins
%dir %{_datadir}/xfce4/panel
%dir %{_datadir}/xfce4/panel/plugins
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/migrate
%{_libdir}/xfce4/panel/wrapper-*
%{_datadir}/gtk-doc/html/libxfce4panel-*

%files -n %{libname}
%{_libdir}/lib*%{api}.so.%{major}*

%files -n %{gtk3libname}
%{_libdir}/libxfce4panel-%{gtk3api}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libxfce4panel-*.so
%{_libdir}/pkgconfig/libxfce4panel-*.pc
%{_includedir}/xfce4/libxfce4panel-*/
