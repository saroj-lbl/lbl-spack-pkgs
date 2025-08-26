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
    depends_on("cmake@3.14:", type="build")
    depends_on("git", type="build")
    
    def cmake_args(self):
        cmake_args = []

        cmake_args.extend([
            self.define_from_variant("GGML_CUDA", "cuda")
        ])

        # cuda architecture
        if self.spec.satisfies("+cuda"):
            if "CMAKE_CUDA_ARCHITECTURES" not in self.spec.variants:
                cmake_args.append("-DCMAKE_CUDA_ARCHITECTURES=70;75;86;90")

        return cmake_args
