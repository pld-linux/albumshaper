%define		_alpha	a2
Summary:	Photo album creation and modification application
Summary(pl.UTF-8):	Program do tworzenia i modyfikacji albumów fotograficznych
Name:		albumshaper
Version:	1.0
Release:	0.%{_alpha}.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/albumshaper/%{name}_%{version}%{_alpha}_source.tar.bz2
# Source0-md5:	704199e8f3df8e3504a72574e6f0f11a
Patch0:		%{name}-qmake.patch
URL:		http://albumshaper.sourceforge.net/
BuildRequires:	qt-devel >= 1:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AlbumShaper is a drag-n-drop hierarchal photo album creation and
modification application. Based on the Qt libraries AlbumShaper is a
cross-platform solution for maintaining your collection of digital
images from various sources.

%description -l pl.UTF-8
AlbumShaper jest hierarchicznym programem klasy "przenieś i upuść"
służącym do tworzenia i modyfikacji albumów fotograficznych. Oparty o
bibliotekę Qt AlbumShaper jest rozwiązaniem wieloplatformowym służącym
do zarządzania zbiorami cyfrowych zdjęć pochodzących z różnych źródeł.

%prep
%setup -q -n %{name}_%{version}%{_alpha}_source
%patch -P0 -p1

%build
export QTDIR=%{_prefix}
qmake
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -pipe -Wall -W -DQT_NO_DEBUG"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,share/albumshaper/images}

install bin/images/*.png $RPM_BUILD_ROOT%{_datadir}/albumshaper/images
install bin/AlbumShaper.bin $RPM_BUILD_ROOT%{_bindir}/albumshaper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{authors,bugs,changelog,credits} docs/html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
