{
  "targets": [{
    "target_name": "permissions",
    "cflags!": [ '-fno-exceptions' ],
    "cflags_cc!": [ '-fno-exceptions' ],
    "sources": [
      'src/permissions.mm'
    ],
    'include_dirs': [
      "<!@(node -p \"require('node-addon-api').include\")"
    ],
    'variables': {
        'openssl_fips': '',
    },
    'libraries': [],
    'link_settings': {
      'libraries': [
        "-framework AppKit",
        "-framework AVFoundation",
        "-framework CoreBluetooth",
        "-framework CoreFoundation",
        "-framework CoreLocation",
        "-framework CoreGraphics",
        "-framework Contacts",
        "-framework EventKit",
        "-framework IOKit",
        "-framework Photos",
        "-framework Speech",
        "-framework StoreKit"
      ]
    },
    'dependencies': [
      "<!(node -p \"require('node-addon-api').gyp\")"
    ],
    "xcode_settings": {
      'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
      'CLANG_CXX_LIBRARY': 'libc++',
      "MACOSX_DEPLOYMENT_TARGET": "10.13",
      "OTHER_CFLAGS": [
        "-arch x86_64",
        "-arch arm64"
      ],
      "OTHER_LDFLAGS": [
        "-arch x86_64",
        "-arch arm64"
      ]
    }
  }]
}
