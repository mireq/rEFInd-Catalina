## Clover rEFInd theme

![OS select](https://raw.github.com/wiki/mireq/rEFInd-Catalina/screenshot_001.png)

### Usage

 1. Locate your refind EFI directory. This is commonly `/boot/EFI/refind`
    though it will depend on where you mount your ESP and where rEFInd is
    installed. `fdisk -l` and `mount` may help.

 2. Create a folder called `themes` inside it, if it doesn't already exist

 3. Copy `refind/Catalina` directory into `themes` directory.

 4. To enable the theme add `include themes/Catalina/theme.conf` at the end of
    `refind.conf`.

Here's an example menuentry configuration (from the screenshot)

```nginx
menuentry "Arch Linux" {
	icon /EFI/refind/themes/Catalina/icons/os_arch.png
	loader vmlinuz-linux
	initrd initramfs-linux.img
	options "rw root=UUID=dfb2919d-ff78-48db-a8a7-23f7542c343a loglevel=3"
}

menuentry "Windows" {
	icon /EFI/refind/themes/Catalina/icons/os_win.png
	loader /EFI/Microsoft/Boot/bootmgfw.efi
}

menuentry "OSX" {
	icon /EFI/refind/themes/Catalina/icons/os_mac.png
	loader /EFI/Apple/Boot/bootmgfw.efi
}
```

### Background sizes

If you find the background looks blurry it may be due to the included wallpaper
being an incorrect resolution for your monitor. You can download the [original
high quality wallpaper][wallpaper], resize it as appropriate, and replace the
`background.png`.

You can of course also choose your own background!

### Attribution

The OS icons and background are from [clover Catalina theme][clover-catalina].

[clover-catalina]: https://sourceforge.net/p/cloverefiboot/themes/ci/master/tree/themes/Catalina/
