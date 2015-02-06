%define oname clonk

Name:		openclonk
Version:	5.3.3
Release:	3
Summary:	Free multiplayer action game about mining, settling and fast-paced melees
Group:		Games/Arcade
License:	BSD
URL:		http://openclonk.org/
Source:		http://hg.openclonk.org/openclonk/archive/%{name}-release-%{version}-src.tar.gz
Patch0:		openclonk-release-5.3.3-tinyxml.patch
Patch1:		openclonk-release-5.3.3-path.patch
BuildRequires:	cmake
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	tinyxml-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(zlib)

%description
OpenClonk is a free multiplayer action game where you control clonks,
small but witty and nimble humanoid beings. The game is mainly about
mining, settling and fast-paced melees. OpenClonk is also not just a
game but also a versatile 2D game engine that offers countless
possibilites to make own mods.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
rm -rf thirdparty/tinyxml

%build
# Segfaults with default optimization
# See http://bugs.openclonk.org/view.php?id=873
%global optflags %{optflags} -O0

%cmake \
	-DUSE_GTK2:BOOL=ON \
	-DUSE_GTK3:BOOL=OFF \
	-DUSE_GL:BOOL=ON
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/c4group
%{_gamesbindir}/%{oname}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_iconsdir}/hicolor/*/apps/%{oname}.png

