Name:		texlive-morewrites
Version:	20190228
Release:	1
Summary:	Always room for a new write stream
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/morewrites
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package aims to solve the error "No room for a new \write",
which occurs when the user, or when the user's packages have
'allocated too many streams using \newwrite (TeX has a fixed
maximum number - 16 - such streams built-in to its code). The
package hooks into TeX primitive commands associated with
writing to files; it should be loaded near the beginning of the
sequence of loading packages for a document. The package uses
the l3kernel bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/morewrites
%doc %{_texmfdistdir}/doc/latex/morewrites
#- source
%doc %{_texmfdistdir}/source/latex/morewrites

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
