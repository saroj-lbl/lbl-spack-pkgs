from spack.package import *

class LlamaCpp(CMakePackage):
    """LLama.cpp package
    """

    homepage = "https://github.com/ggml-org/llama.cpp"
    url = "https://github.comggml-org/llama.cpp/archive/refs/tags/b6276.tar.gz"
    git = "https://github.com/ggml-org/llama.cpp.git"

    license("MIT")

    version("latest", branch="master")
    version("b6276", tag="b6276")

    # variants
    variant("cuda", default=False)

    # dependencies
    depends_on("cmake@3.14:", type="build")
    depends_on("git", type="build")

    def cmake_args(self):
        args = []

        args.extend([
            self.define_from_variant("GGML_CUDA", "cuda")
        ])

        # cuda architecture
        if "+cuda" in self.spec:
            args.extend([
                self.define_from_variant("")
            ])

            if "CMAKE_CUDA_ARCHITECTURES" not in self.spec.variants:
                args.append("-DCMAKE_CUDA_ARCHITECTURES=70;75;86;90")
