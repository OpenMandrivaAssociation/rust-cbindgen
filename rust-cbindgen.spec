# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check

%global crate cbindgen

Name:           rust-cbindgen
Version:        0.28.0
Release:        1
Summary:        Tool for generating C bindings to Rust code
Group:          Development/Rust

License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:         https://github.com/mozilla/cbindgen/archive/refs/tags/v%{version}/%{crate}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(clap/default) 
#>= 4.3.0 with crate(clap/default) < 5.0.0~)
BuildRequires:  (crate(heck/default) >= 0.4.0 with crate(heck/default) < 0.5.0~)
BuildRequires:  (crate(indexmap/default) >= 2.1.0 with crate(indexmap/default) < 3.0.0~)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
BuildRequires:  (crate(proc-macro2/default) >= 1.0.60 with crate(proc-macro2/default) < 2.0.0~)
BuildRequires:  (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0~)
BuildRequires:  (crate(serde) >= 1.0.103 with crate(serde) < 2.0.0~)
BuildRequires:  (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0~)
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0~)
BuildRequires:  (crate(syn) >= 2.0.85 with crate(syn) < 3.0.0~)
BuildRequires:  (crate(syn/clone-impls) >= 2.0.85 with crate(syn/clone-impls) < 3.0.0~)
BuildRequires:  (crate(syn/extra-traits) >= 2.0.85 with crate(syn/extra-traits) < 3.0.0~)
BuildRequires:  (crate(syn/fold) >= 2.0.85 with crate(syn/fold) < 3.0.0~)
BuildRequires:  (crate(syn/full) >= 2.0.85 with crate(syn/full) < 3.0.0~)
BuildRequires:  (crate(syn/parsing) >= 2.0.85 with crate(syn/parsing) < 3.0.0~)
BuildRequires:  (crate(syn/printing) >= 2.0.85 with crate(syn/printing) < 3.0.0~)
BuildRequires:  (crate(tempfile/default) >= 3.0.0 with crate(tempfile/default) < 4.0.0~)
BuildRequires:  (crate(toml/default) >= 0.8.8 with crate(toml/default) < 0.9.0~)
BuildRequires:  rust >= 1.74
%if %{with check}
BuildRequires:  (crate(pretty_assertions/default) >= 1.4.0 with crate(pretty_assertions/default) < 2.0.0~)
BuildRequires:  (crate(serial_test) >= 2.0.0 with crate(serial_test) < 3.0.0~)
%endif

%global _description %{expand:
A tool for generating C bindings to Rust code.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
Group:          # FIXME
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc contributing.md
%doc docs.md
%doc internals.md
%{_bindir}/cbindgen

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(cbindgen) = 0.28.0
Requires:       (crate(heck/default) >= 0.4.0 with crate(heck/default) < 0.5.0~)
Requires:       (crate(indexmap/default) >= 2.1.0 with crate(indexmap/default) < 3.0.0~)
Requires:       (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
Requires:       (crate(proc-macro2/default) >= 1.0.60 with crate(proc-macro2/default) < 2.0.0~)
Requires:       (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0~)
Requires:       (crate(serde) >= 1.0.103 with crate(serde) < 2.0.0~)
Requires:       (crate(serde/derive) >= 1.0.103 with crate(serde/derive) < 2.0.0~)
Requires:       (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0~)
Requires:       (crate(syn) >= 2.0.85 with crate(syn) < 3.0.0~)
Requires:       (crate(syn/clone-impls) >= 2.0.85 with crate(syn/clone-impls) < 3.0.0~)
Requires:       (crate(syn/extra-traits) >= 2.0.85 with crate(syn/extra-traits) < 3.0.0~)
Requires:       (crate(syn/fold) >= 2.0.85 with crate(syn/fold) < 3.0.0~)
Requires:       (crate(syn/full) >= 2.0.85 with crate(syn/full) < 3.0.0~)
Requires:       (crate(syn/parsing) >= 2.0.85 with crate(syn/parsing) < 3.0.0~)
Requires:       (crate(syn/printing) >= 2.0.85 with crate(syn/printing) < 3.0.0~)
Requires:       (crate(tempfile/default) >= 3.0.0 with crate(tempfile/default) < 4.0.0~)
Requires:       (crate(toml/default) >= 0.8.8 with crate(toml/default) < 0.9.0~)
Requires:       cargo
Requires:       rust >= 1.74

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/contributing.md
%doc %{crate_instdir}/docs.md
%doc %{crate_instdir}/internals.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(cbindgen/default) = 0.28.0
Requires:       cargo
Requires:       crate(cbindgen) = 0.28.0
Requires:       crate(cbindgen/clap) = 0.28.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(cbindgen/clap) = 0.28.0
Requires:       (crate(clap/default) >= 4.3.0 with crate(clap/default) < 5.0.0~)
Requires:       cargo
Requires:       crate(cbindgen) = 0.28.0

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_ir-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(cbindgen/unstable_ir) = 0.28.0
Requires:       cargo
Requires:       crate(cbindgen) = 0.28.0

%description -n %{name}+unstable_ir-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_ir" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_ir-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
