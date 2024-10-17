%global packname  spdep
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.5.56
Release:          1
Summary:          Spatial dependence: weighting schemes, statistics and models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/spdep_0.5-56.tar.gz
Requires:         R-methods R-sp R-boot R-Matrix R-MASS R-nlme R-maptools R-deldir R-coda 
Requires:         R-snow R-rlecuyer R-spam R-RANN R-RColorBrewer R-lattice 
Requires:         R-LearnBayes
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-sp R-boot R-Matrix R-MASS R-nlme R-maptools R-deldir R-coda
BuildRequires:    R-snow R-rlecuyer R-spam R-RANN R-RColorBrewer R-lattice 
BuildRequires:    R-LearnBayes
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
A collection of functions to create spatial weights matrix objects from
polygon contiguities, from point patterns by distance and tesselations,
for summarising these objects, and for permitting their use in spatial
data analysis, including regional aggregation by minimum spanning tree; a
collection of tests for spatial autocorrelation, including global Moran's
I, APLE, Geary's C, Hubert/Mantel general cross product statistic,
Empirical Bayes estimates and Assuncao/Reis Index, Getis/Ord G and
multicoloured join count statistics, local Moran's I and Getis/Ord G,
saddlepoint approximations  and exact tests for global and local Moran's
I; and functions for estimating spatial simultaneous autoregressive (SAR)
lag and error models, impact measures for lag models, weighted and
unweighted SAR and CAR spatial regression models, semi-parametric and
Moran eigenvector spatial filtering, GM SAR error models, and generalized
spatial two stage least squares models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5_43-1
+ Revision: 777131
- Import R-spdep
- Import R-spdep


