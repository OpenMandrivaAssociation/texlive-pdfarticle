Name:		texlive-pdfarticle
Version:	51127
Release:	1
Summary:	Class for pdf publications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfarticle
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfarticle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfarticle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pdfArticle is simple document class dedicated for creating pdf
documents with LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/pdfarticle
%doc %{_texmfdistdir}/doc/lualatex/pdfarticle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
