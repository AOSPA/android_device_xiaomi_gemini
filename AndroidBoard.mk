# Copyright (C) 2017 Paranoid Android
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# Set the firmware path in the environment
target_firmware_path := $(ANDROID_BUILD_TOP)/vendor/xiaomi/gemini/firmware_images/

# cmnlib64
$(call add-firmware-file,$(target_firmware_path)/cmnlib64.mbn)
# cmnlib
$(call add-firmware-file,$(target_firmware_path)/cmnlib.mbn)
# hyp
$(call add-firmware-file,$(target_firmware_path)/hyp.mbn)
# pmic
$(call add-firmware-file,$(target_firmware_path)/pmic.elf)
# tc
$(call add-firmware-file,$(target_firmware_path)/tz.mbn)
# aboot
$(call add-firmware-file,$(target_firmware_path)/emmc_appsboot.mbn)
# lksecapp
$(call add-firmware-file,$(target_firmware_path)/lksecapp.mbn)
# devcfg
$(call add-firmware-file,$(target_firmware_path)/devcfg.mbn)
# keymaster
$(call add-firmware-file,$(target_firmware_path)/keymaster.mbn)
# xbl
$(call add-firmware-file,$(target_firmware_path)/xbl.elf)
# rpm
$(call add-firmware-file,$(target_firmware_path)/rpm.mbn)
# splash
$(call add-firmware-file,$(target_firmware_path)/splash.img)
# modem
$(call add-firmware-file,$(target_firmware_path)/NON-HLOS.bin)
# logo
$(call add-firmware-file,$(target_firmware_path)/logo.img)
# dsp
$(call add-firmware-file,$(target_firmware_path)/adspso.bin)
# bluetooth
$(call add-firmware-file,$(target_firmware_path)/BTFM.bin)

# Unset local variable
target_firmware_path :=
