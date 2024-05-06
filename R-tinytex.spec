#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-tinytex
Version  : 0.51
Release  : 88
URL      : https://cran.r-project.org/src/contrib/tinytex_0.51.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tinytex_0.51.tar.gz
Summary  : Helper Functions to Install and Maintain TeX Live, and Compile
Group    : Development/Tools
License  : MIT
Requires: R-xfun
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
# TinyTeX
<!-- badges: start -->
[![R-CMD-check](https://github.com/rstudio/tinytex/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/rstudio/tinytex/actions/workflows/R-CMD-check.yaml)
[![Codecov test coverage](https://codecov.io/gh/rstudio/tinytex/branch/main/graph/badge.svg)](https://app.codecov.io/gh/rstudio/tinytex?branch=main)
[![CRAN release](https://www.r-pkg.org/badges/version/tinytex)](https://cran.r-project.org/package=tinytex)
<!-- badges: end -->

%prep
%setup -q -n tinytex
pushd ..
cp -a tinytex buildavx2
popd
pushd ..
cp -a tinytex buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715034024

%install
export SOURCE_DATE_EPOCH=1715034024
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tinytex/CITATION
/usr/lib64/R/library/tinytex/DESCRIPTION
/usr/lib64/R/library/tinytex/INDEX
/usr/lib64/R/library/tinytex/LICENSE
/usr/lib64/R/library/tinytex/Meta/Rd.rds
/usr/lib64/R/library/tinytex/Meta/features.rds
/usr/lib64/R/library/tinytex/Meta/hsearch.rds
/usr/lib64/R/library/tinytex/Meta/links.rds
/usr/lib64/R/library/tinytex/Meta/nsInfo.rds
/usr/lib64/R/library/tinytex/Meta/package.rds
/usr/lib64/R/library/tinytex/NAMESPACE
/usr/lib64/R/library/tinytex/NEWS.Rd
/usr/lib64/R/library/tinytex/R/tinytex
/usr/lib64/R/library/tinytex/R/tinytex.rdb
/usr/lib64/R/library/tinytex/R/tinytex.rdx
/usr/lib64/R/library/tinytex/help/AnIndex
/usr/lib64/R/library/tinytex/help/aliases.rds
/usr/lib64/R/library/tinytex/help/paths.rds
/usr/lib64/R/library/tinytex/help/tinytex.rdb
/usr/lib64/R/library/tinytex/help/tinytex.rdx
/usr/lib64/R/library/tinytex/html/00Index.html
/usr/lib64/R/library/tinytex/html/R.css
/usr/lib64/R/library/tinytex/tests/test-cran.R
/usr/lib64/R/library/tinytex/tests/test-cran/test-latex.R
/usr/lib64/R/library/tinytex/tests/test-travis.R
/usr/lib64/R/library/tinytex/tests/test-travis/test-install.R
/usr/lib64/R/library/tinytex/tests/test-travis/test-tlmgr.R
