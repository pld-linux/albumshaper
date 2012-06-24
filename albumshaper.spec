%define		_alpha	a2
Summary:	Photo album creation and modification application
Summary(pl):	Program do tworzenia i modyfikacji album�w fotograficznych
Name:		albumshaper
Version:	1.0
Release:	0.%{_alpha}.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}%{_alpha}_source.tar.bz2
# Source0-md5:	704199e8f3df8e3504a72574e6f0f11a
Patch0:		%{name}-qmake.patch
URL:		http://albumshaper.sourceforge.net/
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AlbumShaper is a drag-n-drop hierarchal photo album creation and
modification application. Based on the Qt libraries AlbumShaper is a
cross-platform solution for maintaining your collection of digital
images from various sources.

%description -l pl
AlbumShaper jest hierarchicznym programem klasy "przenie� i upu��"
s�u��cym do tworzenia i modyfikacji album�w fotograficznych. Oparty o
bibliotek� Qt AlbumShaper jest rozwi�zaniem wieloplatformowym s�u��cym
do zarz�dzania zbiorami cyfrowych zdj�� pochodz�cych z r�nych �r�de�.

%prep
%setup -q -n %{name}_%{version}%{_alpha}_source
%patch0 -p1

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
