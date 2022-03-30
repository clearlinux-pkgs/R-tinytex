#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tinytex
Version  : 0.38
Release  : 65
URL      : https://cran.r-project.org/src/contrib/tinytex_0.38.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tinytex_0.38.tar.gz
Summary  : Helper Functions to Install and Maintain TeX Live, and Compile
Group    : Development/Tools
License  : MIT
Requires: R-xfun
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
# TinyTeX
<!-- badges: start -->
[![R-CMD-check](https://github.com/yihui/tinytex/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/yihui/tinytex/actions/workflows/R-CMD-check.yaml)
[![AppVeyor build status](https://ci.appveyor.com/api/projects/status/github/yihui/tinytex?svg=true&branch=main)](https://ci.appveyor.com/project/yihui/tinytex)
[![Codecov test coverage](https://codecov.io/gh/yihui/tinytex/branch/main/graph/badge.svg)](https://app.codecov.io/gh/yihui/tinytex?branch=main)
[![CRAN release](https://www.r-pkg.org/badges/version/tinytex)](https://cran.r-project.org/package=tinytex)
<!-- badges: end -->

%prep
%setup -q -c -n tinytex
cd %{_builddir}/tinytex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648666191

%install
export SOURCE_DATE_EPOCH=1648666191
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tinytex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
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
/usr/lib64/R/library/tinytex/tests/test-travis/test-install.R
/usr/lib64/R/library/tinytex/tests/test-travis/test-tlmgr.R
