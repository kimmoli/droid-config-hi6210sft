# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device hi6210sft
%define vendor huawei

%define vendor_pretty Huawei
%define device_pretty P8Lite

%define dcd_path ./

# Community HW adaptations need this
%define community_adaptation 1

# Adjust this for your device
%define pixel_ratio 1.2

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
