//frida -U -l uncrack01.js -f owasp.mstg.uncrackable1
Java.perform(function(){
    var System_ = Java.use("java.lang.System")
    console.log("[-] Rooting Bypass ...")

    //root 탐지 우회, System.exit() 함수 후킹
    System_.exit.implementation = function() {
        console.log("[+] System exit")
    }

})