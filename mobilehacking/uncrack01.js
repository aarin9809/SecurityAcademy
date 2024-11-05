//frida -U -l uncrack01.js -f owasp.mstg.uncrackable1
Java.perform(function(){
    var root_ = Java.use("sg.vantagepoint.a.c")
    console.log("[-] Rooting Bypass ...")
    //1. 메서드 값 재정의 코드 추가
    // root_.a.overload().implementation = function() {
    root_.a.implementation = function() {
        return false;
    }
    //2
    //3
})