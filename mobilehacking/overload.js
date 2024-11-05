//frida -U -l {script}.js -f {package_name}
Java.perform(function() {
    var lab_03 = Java.use("com.stl.stllab.MainActivity")
    console.log('test')
    lab_03.stl_test_level_03.overload('java.lang.String').implementation = function() {
        this.stl_test_level_03("test")
    }
});                 192.168.0.16:9999 - FridaLab.apk / 교육용_PDF