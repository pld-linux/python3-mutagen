#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
#
%define		module	mutagen
Summary:	Audio metadata reader/writer for Python 2
Summary(pl.UTF-8):	Moduł Pythona 2 do odczytu i zapisu metadanych dźwiękowych
Name:		python3-%{module}
Version:	1.48.1
Release:	1
License:	GPL v2+
Group:		Development/Languages/Python
#Source0Download: https://github.com/quodlibet/mutagen/releases
Source0:	https://github.com/quodlibet/mutagen/releases/download/release-%{version}/mutagen-%{version}.tar.gz
# Source0-md5:	90d74b6da76fdf31933766e0e0d83cc5
URL:		https://github.com/quodlibet/mutagen
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 1.3
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutagen is an audio metadata tag reader and writer implemented in pure
Python. It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2,
and FLAC, and writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

%description -l pl.UTF-8
Mutagen to moduł do odczytu i zapisu znaczników metadanych dźwiękowych
zaimplementowany w czystym Pythonie. Obsługuje odczyt ID3v1.1,
ID3v2.2, ID3v2.3, ID3v2.4, APEv2 i FLAC oraz zapis ID3v1.1, ID3v2.4,
APEv2 i FLAC.

%package tools
Summary:	Simple tools for reading and writing audio metadata
Summary(pl.UTF-8):	Proste narzędzia do odczytu i zapisu metadanych dźwiękowych
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-mutagen-tools < 1.48.1

%description tools
Simple tools for reading and writting audio metadata.

%description tools -l pl.UTF-8
Proste narzędzia do odczytu i zapisu metadanych dźwiękowych.

%package apidocs
Summary:	API documentation for Python mutagen module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mutagen
Group:		Documentation

%description apidocs
API documentation for Python mutagen module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mutagen.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rst
%{py3_sitescriptdir}/mutagen
%{py3_sitescriptdir}/mutagen-%{version}-py*.egg-info

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mid3cp
%attr(755,root,root) %{_bindir}/mid3iconv
%attr(755,root,root) %{_bindir}/mid3v2
%attr(755,root,root) %{_bindir}/moggsplit
%attr(755,root,root) %{_bindir}/mutagen-inspect
%attr(755,root,root) %{_bindir}/mutagen-pony
%{_mandir}/man1/mid3cp.1*
%{_mandir}/man1/mid3iconv.1*
%{_mandir}/man1/mid3v2.1*
%{_mandir}/man1/moggsplit.1*
%{_mandir}/man1/mutagen-inspect.1*
%{_mandir}/man1/mutagen-pony.1*

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,api,man,user,*.html,*.js}
%endif
