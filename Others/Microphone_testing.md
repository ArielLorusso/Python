# INSTALL
```sh
sudo apt-get install pactl
```
# USE

```sh
pactl load-module module-loopback latency_msec=1
pactl unload-module module-loopback
```

# RESET AUDIO
```sh
pulseaudio -k && pulseaudio --start
```
# LIST SINKS
```sh
pactl list short sinks
```
0	alsa_output.pci-0000_29_00.1.hdmi-stereo	                    module-alsa-card.c	s16le 2ch 44100Hz	    IDLE
1	alsa_output.usb-Digidesign_Mbox_2_Digidesign-00.analog-stereo	module-alsa-card.c	s24be 2ch 48000Hz	    RUNNING
2	alsa_output.platform-snd_aloop.0.analog-stereo	                module-alsa-card.c	s16le 2ch 44100Hz	    IDLE

# MAP new SINK
```sh
pactl load-module module-remap-sink master=<SINK_NAME> channels=2 channel_map=mono,mono
pactl load-module module-remap-sink master=alsa_output.usb-Digidesign_Mbox_2_Digidesign-00.analog-stereo channels=2 channel_map=mono,mono
```

0	alsa_output.pci-0000_29_00.1.hdmi-stereo	                    module-alsa-card.c	s16le 2ch 44100Hz	    IDLE
1	alsa_output.usb-Digidesign_Mbox_2_Digidesign-00.analog-stereo	module-alsa-card.c	s24be 2ch 48000Hz       RUNNING
2	alsa_output.platform-snd_aloop.0.analog-stereo	                module-alsa-card.c	s16le 2ch 44100Hz       IDLE
3	alsa_output.usb-Digidesign_Mbox_2_Digidesign-00.analog-stereo.remapped	module-remap-sink.c	s24be 2ch 48000Hz	IDLE   <--- NEW MONO SINK

# SET default MONO SINK
```sh
 pactl set-default-sink 3
```

# SHOW 
```sh
pactl list modules | grep alsa
```
Argument: device_id="0" name="pci-0000_29_00.1"     card_name="alsa_card.pci-0000_29_00.1"      namereg_fail=false tsched=yes fixed_latency_range=no ignore_dB=no deferred_volume=yes use_ucm=yes avoid_resampling=no card_properties="module-udev-detect.discovered=1"
Argument: device_id="1" name="pci-0000_2b_00.3"     card_name="alsa_card.pci-0000_2b_00.3"      namereg_fail=false tsched=yes fixed_latency_range=no ignore_dB=no deferred_volume=yes use_ucm=yes avoid_resampling=no card_properties="module-udev-detect.discovered=1"
Argument: device_id="2" name="usb-Digidesign_Mbox_2_Digidesign-00" card_name="alsa_card.usb-Digidesign_Mbox_2_Digidesign-00" namereg_fail=false tsched=yes fixed_latency_range=no ignore_dB=no deferred_volume=yes use_ucm=yes avoid_resampling=no card_properties="module-udev-detect.discovered=1"
Argument: device_id="3" name="platform-snd_aloop.0" card_name="alsa_card.platform-snd_aloop.0"  namereg_fail=false tsched=yes fixed_latency_range=no ignore_dB=no deferred_volume=yes use_ucm=yes avoid_resampling=no card_properties="module-udev-detect.discovered=1"
Argument: master=alsa_output.usb-Digidesign_Mbox_2_Digidesign-00.analog-stereo channels=2 channel_map=mono,mono

# DELETE sink
```sh
pactl unload-module <module_index>
```