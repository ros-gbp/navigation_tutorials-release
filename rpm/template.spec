Name:           ros-indigo-roomba-stage
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS roomba_stage package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roomba_stage
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-fake-localization
Requires:       ros-indigo-map-server
Requires:       ros-indigo-move-base
Requires:       ros-indigo-stage-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-fake-localization
BuildRequires:  ros-indigo-map-server
BuildRequires:  ros-indigo-move-base
BuildRequires:  ros-indigo-stage-ros

%description
The roomba_stage package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Oct 19 2015 William Woodall <william@osrfoundation.org> - 0.2.1-0
- Autogenerated by Bloom

* Fri Feb 06 2015 William Woodall <william@osrfoundation.org> - 0.2.0-0
- Autogenerated by Bloom

