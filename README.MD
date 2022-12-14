<h1>Native Obfuscator GUI</h1>
<p>This uses radioegor146's native obfuscator (https://github.com/radioegor146), but everything is automated by this little thing</p>

<p>Native obfuscation converts Java class files to native code which is compiled and relinked to the original program through the Java Native Interface. No trace of the original Java bytecode remains, and no deobfuscation tool that works on class files can recover the original code.</p>

<h2>Setup</h2>
<p>First, you need to install JDK 8. You can download it below</p>

<p>Next, you need to install CMake, you can download that below.
You need to make sure that you allow it to install on all or just this current user (the only reason not to put it on all users is if you're using a public or famiily computer)</p>

<p>You also need to install a C++/C compiler tool, such as Visual Studio, you can download that below.

<p>Finally, run the setup.bat file and then run the python file</p>

For a more detailed guide, follow https://github.com/radioegor146/native-obfuscator 

<h2>Downloads</h2>
JDK 8: https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html#license-lightbox

CMake: https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-windows-x86_64.msi

Visual Studio: https://visualstudio.microsoft.com/

<h2>Disclaimer</h2>
I'm aware the gui is very bad, it's made with tkinter and took me less than an hour so you can be quiet
