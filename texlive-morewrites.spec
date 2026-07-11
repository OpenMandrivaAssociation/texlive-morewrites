%global tl_name morewrites
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Always room for a new write stream
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/morewrites
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/morewrites.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package aims to solve the error "No room for a new \write", which
occurs when the user, or when the user's packages have 'allocated too
many streams' using \newwrite (TeX has a fixed maximum number - 16 -
such streams built-in to its code). The package hooks into TeX primitive
commands associated with writing to files; it should be loaded near the
beginning of the sequence of loading packages for a document. The
package uses the l3kernel bundle.

