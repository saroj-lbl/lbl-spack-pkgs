from spack.package import *

class Ollama(Package):
    """Ollama binary package
    """

    homepage = "https://ollama.com"
    url = "https://github.com/ollama/ollama/releases/download/v0.9.0/ollama-linux-amd64.tgz"
    version("0.12.10",
            url="https://github.com/ollama/ollama/releases/download/v0.12.10/ollama-linux-amd64.tgz",
            sha256="8f4bf70a9856a34ba71355745c2189a472e2691a020ebd2e242a58e4d2094722",
            expand=False,)
    version("0.12.6", 
            url="https://github.com/ollama/ollama/releases/download/v0.12.6/ollama-linux-amd64.tgz",
            sha256="de82adce2ab79235115d511ff22fcb099ac53b67127870f12b80198c033ec0a1",
            expand=False,)
    version("0.9.0",
            url=url,
            sha256="ae9cebd61552d6cf3c527cb88e3a4865a25f22950aa8bb5328887ffd96cfd22a",
            expand=False,)

    def install(self, spec, prefix):
        tar = which("tar")
        tar("-xzf", self.stage.archive_file, "-C", prefix)