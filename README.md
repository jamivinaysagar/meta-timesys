What is meta-timesys
====================

This Yocto layer provides scripts for image manifest generation used for security monitoring and notification, customer support, recipe source mirroring, recipe modifications, demos, etc.

Some of the features are aimed at Timesys customers with active subscriptions.  Using these features requires an API Keyfile, which you can learn about setting up from the LinuxLink document here:

https://linuxlink.timesys.com/docs/wiki/engineering/LinuxLink_Key_File


Quick Start
===========

The fastest way to try meta-timesys and its security features is to try dropping it into your existing BSP (clone alongside other layers, add to bblayers.conf). These are instructions to try it from scratch with a pretty minimal Yocto environment.

Although a build is not required to create an image manifest or use the CVE script, BitBake does need to run (to make the manifest), so it is easiest if you adhere to the Yocto system requirements as found here:

http://www.yoctoproject.org/docs/2.4/ref-manual/ref-manual.html#intro-requirements

### Clone poky and meta-timesys

```sh
git clone git://git.yoctoproject.org/poky.git -b rocko
git clone https://github.com/TimesysGit/meta-timesys.git -b rocko
```

### Activate yocto build environment (needed for manifest creation)

```
source poky/oe-init-build-env
```

### Add meta-timesys to _conf/bblayers.conf_.

Follow format of the file, just add meta-timesys after the default poky/meta, etc.

### Create an image manifest

```sh
../meta-timesys/scripts/manifest.sh core-image-minimal manifest.json
```

### Use the manifest to check for CVEs:

```sh
../meta-timesys/scripts/checkcves.py manifest.json
```

Maintainers
===========

Steve Bedford \<steve.bedford@timesys.com\>

Ian Campbell \<ian.campbell@timesys.com\>
