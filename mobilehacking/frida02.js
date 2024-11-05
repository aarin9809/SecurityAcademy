//frida -U -l frida01.js -f uk.rossmarks.fridalab
//Challenge Level 1
//Challenge Level 2
Java.perform(function() {
    Java.choose("uk.rossmarks.fridalab.MainActivity",{
        "onMatch" : function(chall_02){
            chall_02.chall02(); // uk.rossmarks.fridalab.MainActivity.chall02()
            console.log("[*] Challenge Level 02 Hooking...")
            console.log("[*] Call chall02...")
            console.log(chall_02)
        },
        "onComplete" : function(){
            console.log("[#] Challenge Level 02 Hooking >>>>> Success\n")
        }
    });
})