# Daring

Inspired by John Gruber's [Daring Fireball](http://daringfireball.net) link blog, Daring is a similar theme for users of Ghost. It favours text over images and doesn't handle cover images or post images in Ghost.

![Screenshot of Daring](https://s3-eu-west-1.amazonaws.com/s3.matthewlang.net/assets/daring-screenshot.png)

Daring is based on the excellent [Poole](http://getpoole.com) by [Mark Otto](https://github.com/mdo).

Updated for Ghost 2.0.


## Contents

- [Usage](#usage)
- [People using Daring](#people-using-daring)
- [Author](#author)
- [License](#license)


## Usage

Daring is built on top of [Poole](https://github.com/poole/poole), which provides a great starting point for Jekyll but also works well when used with Ghost.

To download, visit the [releases](https://github.com/matthewl/Daring/releases) page.

Daring contains pre-built themes for the following colours:

- Red
- Orange
- Green
- Purple
- Brown
- Blue
- Orange Dark

Each of these pre-built themes can be found in the `themes` folder.

Simply, upload the compressed theme that you want to use to Ghost and activate it.


## Developing

An [Invoke](http://www.pyinvoke.org/) file is included (`tasks.py`) to simplify development.
If you make a change to the code, just run `invoke build` to rebuild the .zip files in `themes/`
(after installing invoke with `pip install invoke`).

Pull requests, especially to add more themes, are quite welcome.


## Authors

**Matthew Lang**
- <https://www.matthewlang.net>
- <https://github.com/matthewl>
- <https://twitter.com/matthewlang>

**Brandon Istenes**
- <https://brandonistenes.com>
- <https://github.com/brandones>


## License

Open sourced under the [MIT license](LICENSE.md).
