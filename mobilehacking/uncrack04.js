Java.perform(function(){
    var root_ = Java.use("sg.vantagepoint.a.c")
    console.log("[-] Verify Logic Bypass ...")
    root_.a.overload().implementation = function() {
        return false;
    }

    console.log("[-] 3초 후, 문자열 출력 코드실행")
    //String 출력, 출력 결과 내에 정답 문자열 확인
    setTimeout(function() {
        console.log("[+] 문자열 출력")
        var str_1 = Java.use("java.lang.String")
        str_1.equals.implementation = function(arg1) {
            console.log(this+':::'+arg1)
            return false
        }
    }, 3000)
})