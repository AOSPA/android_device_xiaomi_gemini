# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017 The LineageOS Project
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

import hashlib
import common
import re
import sha

def FullOTA_Assertions(info):
  AddModemAssertion(info, info.input_zip)
  return

def IncrementalOTA_Assertions(info):
  AddModemAssertion(info, info.target_zip)
  return

def AddModemAssertion(info, input_zip):
  android_info = info.input_zip.read("OTA/android-info.txt")
  m = re.search(r'require\s+version-modem\s*=\s*(\S+)', android_info)
  if m:
    versions = m.group(1).split('|')
    if len(versions) and '*' not in versions:
      cmd = 'assert(gemini.verify_modem(' + ','.join(['"%s"' % modem for modem in versions]) + ') == "1");'
      info.script.AppendExtra(cmd)
  return

def InstallImage(img_name, img_file, partition, info):
  common.ZipWriteStr(info.output_zip, "firmware/" + img_name, img_file)
  info.script.AppendExtra(('package_extract_file("' + "firmware/" + img_name + '", "/dev/block/bootdevice/by-name/' + partition + '");'))

image_partitions = {
   'cmnlib64.mbn'      : 'cmnlib64',
   'cmnlib.mbn'        : 'cmnlib',
   'hyp.mbn'           : 'hyp',
   'pmic.elf'          : 'pmic',
   'tz.mbn'            : 'tz',
   'emmc_appsboot.mbn' : 'aboot',
   'lksecapp.mbn'      : 'lksecapp',
   'devcfg.mbn'        : 'devcfg',
   'keymaster.mbn'     : 'keymaster',
   'xbl.elf'           : 'xbl',
   'rpm.mbn'           : 'rpm',
   'splash.img'        : 'splash',
   'NON-HLOS.bin'      : 'modem',
   'logo.img'          : 'logo',
   'adspso.bin'        : 'dsp',
   'BTFM.bin'          : 'bluetooth'
}

def FullOTA_InstallEnd(info):
  info.script.Print("Writing recommended firmware...")
  for k, v in image_partitions.iteritems():
    try:
      img_file = info.input_zip.read("firmware/" + k)
      InstallImage(k, img_file, v, info)
    except KeyError:
      print "warning: no " + k + " image in input target_files; not flashing " + k


def IncrementalOTA_InstallEnd(info):
  for k, v in image_partitions.iteritems():
    try:
      source_file = info.source_zip.read("firmware/" + k)
      target_file = info.target_zip.read("firmware/" + k)
      if source_file != target_file:
        InstallImage(k, target_file, v, info)
      else:
        print k + " image unchanged; skipping"
    except KeyError:
      print "warning: " + k + " image missing from target; aborting: " + k
