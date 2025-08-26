from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *

class Llamacpp(CMakePackage, CudaPackage):
    """LLama.cpp package
    """

    homepage = "https://github.com/ggml-org/llama.cpp"
    url = "https://github.com/ggml-org/llama.cpp/archive/refs/tags/b6276.tar.gz"
    git = "https://github.com/ggml-org/llama.cpp.git"

    license("MIT")

    version("latest", branch="master")
    version("b6276", tag="b6276")
    
    # dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    depends_on("git", type="build")

    
    def cmake_args(self):
        cmake_args = []

        cmake_args.extend([
            self.define_from_variant("GGML_CUDA", "cuda")
        ])

        # cuda architecture
        if self.spec.satisfies("+cuda"):
            cmake_args.append("-DCUDAToolkit_ROOT:STRING=" + self.spec["cuda"].prefix)
            if "CMAKE_CUDA_ARCHITECTURES" not in self.spec.variants:
                cmake_args.append("-DCMAKE_CUDA_ARCHITECTURES=70;75;86;90")

        return cmake_args

    def setup_build_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
            env.set("CUDA_ROOT", self.spec["cuda"].prefix)
            env.prepend_path("PATH", join_path(self.spec["cuda"].prefix, "bin"))
            env.prepend_path("LD_LIBRARY_PATH", join_path(self.spec["cuda"].prefix, "lib64"))

    def setup_run_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.prepend_path("LD_LIBRARY_PATH", join_path(self.spec["cuda"].prefix, "lib64"))
