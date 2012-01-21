This is [Pygments][] syntax highlighting for [Rust][].

Rust's syntax isn't set in stone, so this will probably break sometime. Also I'm not sure that I got everything -- if you find anything that I missed, leave a note in the [issues][] or fork and pull request.

[Pygments]: http://pygments.org/
[Rust]: https://github.com/mozilla/rust
[issues]: https://github.com/startling/pygments-rust/issues

## Installation

```bash
pip install git+git://github.com/startling/pygments-rust.git
```

This uses Pygment's `entry_points`, so you don't have to do anything special.

## Credits

I liberally stole from both [Rust's vim syntax highlighting][] and the [language reference][].

[Rust's vim syntax highlighting]: https://github.com/mozilla/rust/blob/master/src/etc/vim/syntax/rust.vim
[language reference]: http://doc.rust-lang.org/doc/rust.html
