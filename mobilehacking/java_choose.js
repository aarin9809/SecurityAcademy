Java.perform(function() {
    Java.choose("com.stl.stllab.MainActivity", {
        onMatch: function(instance) {
            instance.stl_test_level_02()
        },
        onComplete: function() {
            console.log("Success")
        }
    })
})