py_binary(
    name = "bin",
    srcs = ["bin.py"],
    deps = [
        ":lib",
	":fib",
    ],
)

py_library(
    name = "fib",
    srcs = ["fib.py"],
)

py_library(
    name = "lib",
    srcs = ["lib.py"],
)

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = [
        ":lib",
	":fib",
    ],
)

py_test(
    name = "fail",
    srcs = ["fail.py"],
    deps = [":lib"],
)
