Java.perform(function(){
    var root_ = Java.use("sg.vantagepoint.a.c")
    var secret_logic = Java.use("sg.vantagepoint.uncrackable1.a")
    console.log("[-] Verify Logic Bypass ...")
    root_.a.overload().implementation = function() {
        return false;
    }
    //Secret Key 인증 로직 우회
    secret_logic.a.implementation = function() {
        console.log("[+] Verify Logic Bypass Success")
        return true;
    }
})