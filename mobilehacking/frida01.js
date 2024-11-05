//frida -U -l frida01.js -f uk.rossmarks.fridalab
//Challenge Level 1
Java.perform(function(){
    var chall1 = Java.use("uk.rossmarks.fridalab.challenge_01")
    chall1.chall01.value = 1; //challenge_01 클래스의 chall01 메소드의 값을 변경
})