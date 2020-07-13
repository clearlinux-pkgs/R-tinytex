#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tinytex
Version  : 0.24
Release  : 38
URL      : https://cran.r-project.org/src/contrib/tinytex_0.24.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tinytex_0.24.tar.gz
Summary  : Helper Functions to Install and Maintain 'TeX Live', and Compile
Group    : Development/Tools
License  : MIT
Requires: R-xfun
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
# TinyTeX
[![Build Status](https://travis-ci.com/yihui/tinytex.svg)](https://travis-ci.com/yihui/tinytex)
[![AppVeyor build status](https://ci.appveyor.com/api/projects/status/github/yihui/tinytex?svg=true&branch=master)](https://ci.appveyor.com/project/yihui/tinytex)
[![Coverage status](https://codecov.io/gh/yihui/tinytex/branch/master/graph/badge.svg)](https://codecov.io/github/yihui/tinytex?branch=master)
[![Downloads from the RStudio CRAN mirror](https://cranlogs.r-pkg.org/badges/tinytex)](https://cran.r-project.org/package=tinytex)

%prep
%setup -q -c -n tinytex
cd %{_builddir}/tinytex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592855095

%install
export SOURCE_DATE_EPOCH=1592855095
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tinytex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tinytex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tinytex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tinytex || :


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
/usr/lib64/R/library/tinytex/tests/test-travis/test-tlmgr.R
