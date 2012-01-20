from distutils.core import setup
import pygments_rust


setup(
    name = "pygments_rust",
    version = pygments_rust.__version__,
    author = "startling",
    author_email = "tdixon51793@gmail.com",
    description = "Rust syntax highlighting with pygments!",
    packages = ["pygments_rust"],
    install_requires = ['pygments'],
    entry_points = """
    [pygments.lexers]
    rust = pygments_rust:RustLexer
    """
)
