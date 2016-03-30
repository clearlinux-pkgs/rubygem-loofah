#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-loofah
Version  : 2.0.3
Release  : 6
URL      : https://rubygems.org/downloads/loofah-2.0.3.gem
Source0  : https://rubygems.org/downloads/loofah-2.0.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-hoe-bundler
BuildRequires : rubygem-hoe-debugging
BuildRequires : rubygem-hoe-gemspec
BuildRequires : rubygem-hoe-git
BuildRequires : rubygem-json
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rr

%description
= Loofah {<img src="https://travis-ci.org/flavorjones/loofah.png?branch=master" alt="Build Status" />}[https://travis-ci.org/flavorjones/loofah]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n loofah-2.0.3
gem spec %{SOURCE0} -l --ruby > rubygem-loofah.gemspec

%build
gem build rubygem-loofah.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
loofah-2.0.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/loofah-2.0.2 && rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/loofah-2.0.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/MIT-LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/benchmark/benchmark.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/benchmark/fragment.html
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/benchmark/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/benchmark/www.slashdot.com.html
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/elements.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/html/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/html/document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/html5/scrub.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/html5/whitelist.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/instance_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/metahelpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/scrubber.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/scrubbers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/xml/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/lib/loofah/xml/document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/assets/testdata_sanitizer_tests1.dat
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/html5/test_sanitizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/integration/test_ad_hoc.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/integration/test_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/integration/test_html.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/integration/test_scrubbers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/integration/test_xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/unit/test_api.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/unit/test_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/unit/test_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/unit/test_scrubber.rb
/usr/lib64/ruby/gems/2.3.0/gems/loofah-2.0.3/test/unit/test_scrubbers.rb
/usr/lib64/ruby/gems/2.3.0/specifications/loofah-2.0.3.gemspec
