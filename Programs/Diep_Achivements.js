const saved_achievements = { "A::d583013681f15fcc_1": "1", "A::eb9792219de8f755_1": "1", "A::cdf66074bb5ce7fa_1": "1", "A::e1f4f3e6a5c9bacb_1": "1", "A::8221180ec6d53232_1": "10000", "A::b8b3e7fd58ff6706_1": "1", "A::5613de303c7e06f0_1": "1", "A::b95a9621ccccad3c_1": "1", "A::f3618c60205d7ded_1": "1", "A::723c26b6a37fccbb_1": "100", "A::9953423e884422b6_1": "100", "A::6520a970c68efb85_1": "1", "A::a402fdb3f5cebf99_1": "1", "A::a81a738312c7705d_1": "1", "A::3fd17b5d35c36670_1": "1", "A::22d84fdc78b1f1ae_1": "1", "A::5892e09831854ad2_1": "1", "A::f73016825baab042_1": "100", "A::bdf3e0a1c4ebcaee_1": "1", "A::8abd923027114f9e_1": "1000", "A::2780b5743fe93789_1": "1", "A::33e4cb47afd5602f_1": "10", "A::d932ec7312510a14_1": "10", "A::256245339c3742d2_1": "10000", "A::1ba4250a398116e7_1": "1", "A::bb9188cddc9d5b1f_1": "100", "A::4d545ac615beec40_1": "1", "A::6502bcb56dfbc0e3_1": "1", "A::76646f423e5d6bc4_1": "1", "A::fc3b3faf73bae216_1": "1", "A::4eebb78f4ee19cba_1": "1", "A::1c00693fbf538316_1": "1", "A::eef89695be793c7f_1": "100", "A::71c663fb258f5243_1": "1", "A::d3e4829583362b48_1": "3000", "A::6d671cfa6dceb09_1": "500", "A::8eeec8c270ef92be_1": "1", "A::54084a4936c7e37_1": "1", "A::e6111736c85494e9_1": "1", "A::22fd2ee6d05881d6_1": "1", "A::9898db9ff6d3c1b3_1": "1", "A::5dbb422e510cec75_1": "1", "A::87e48332e9161b3d_1": "1", "A::ecea90c4be06d999_1": "1", "A::9f0edada2bd7cd6_1": "1", "A::8b8fe153a4965c63_1": "1", "A::300ddd6f1fb3d69d_1": "500" }

// Import saved data - if clear is true, then achievements are reset
function load(clear = false) {
    Object.keys(saved_achievements).forEach((k) => (localStorage[k] = clear ? "0" : saved_achievements[k]));
}

// Export diep.io data - prints out the current achievements to be set to `saved`
function fetch() {
    let obj = {};
    Object.keys(localStorage)
        .filter((k) => k.startsWith("A::"))
        .forEach((k) => (obj[k] = localStorage.getItem(k)));
    console.log(JSON.stringify(obj));
}

load();
