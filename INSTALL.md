# Setting up Kivy

Instead of downloading a package or setting up a PPA on the Ubuntu PCs I use, it
felt like a more cross-platform solution to use the Python package manager `pip`
to install `Kivy`.

## pip, the cross-platform package manager

First, I verified that `kivy` was available using this command:

    pip search kivy

Then I went ahead to install the package:

    sudo -H pip install kivy

This failed because Cython was not present, so I installed that first:

    sudo -H pip install cython

Then I tried to install kivy again. This time it failed to find "GL/gl.h", some
openGL library on my computer, and so I had to install the dependencies myself.

## Not so cross-platform after all...

This is the Ubuntu way of doing it, first by finding out which package contains
the library:

    sudo apt-get install apt-file
    sudo apt-file update
    apt-file search "GL/gl.h" # this gives mesa-common-dev among other options
    sudo apt-get install mesa-common-dev

In my case the package was called `mesa-common-dev` so I just installed it. The
procedure will differ for other systems, and may not be necessary if openGL has
already been installed. (At this point you might prefer dropping this and going
back to downloading the Kivy installer from the website. that is fine.)

However, if you choose to continue here, do note that the installer expects the
file `libGL.so` to exist in a particular location, so a *symlink* might help:

    sudo ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1.2.0 \
    /usr/lib/x86_64-linux-gnu/libGL.so

This allows the install script to find `libGL.so` in the main library location.

Now the install succeeds and pip reports:

    Successfully installed kivy Kivy-Garden

## Unforeseen Dependencies

So it seems `pygame` is required to draw windows on screen, but is not available
in pip right now. So please check that this package is installed first. If it is
not and you are running Ubuntu, this is solved with:

    sudo apt-get install python-pygame
