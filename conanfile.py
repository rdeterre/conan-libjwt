from conans import ConanFile, CMake

class LibjwtConan(ConanFile):
    name = 'libjwt'
    version= 'master'
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    url = "https://github.com/benmcollins/libjwt"
    license = "LGPLv2.1"

    def source(self):
        self.run("git clone --branch master https://github.com/benmcollins/libjwt")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "{}/libjwt" {}'.format(self.conanfile_directory, cmake.command_line))
        self.run('cmake --build . --target jwt {}'.format(cmake.build_config))

    def package(self):
        self.copy("jwt.h", dst='include/libjwt', src='libjwt/include')
        self.copy("*.so", dst="lib", src="libjwt/lib")

    def package_info(self):
        self.cpp_info.libs = ["jwt"]
        self.cpp_info.includedirs = ['include']
