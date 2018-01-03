{
  "targets": [{
    "target_name": "myModule",
    "include_dirs" : [
      "src/cpp",
      "<!(node -e \"require('nan')\")"
    ],
    "sources": [
      "src/cpp/index.cc",
      "src/cpp/Vector.cc"
    ]
  }]
}
