pkgname=firefox-dpms
pkgver=1
pkgrel=1
pkgdesc="Disable DPMS settings when playing video in Firefox"
arch=('any')
url="https://github.com/dglava/firefox-dpms"
license=('GPL3')
depends=('python-pulse-control')
makedepends=('git')
source=('git+https://github.com/dglava/firefox-dpms.git')
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/${pkgname%-git}"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$srcdir/${pkgname%-git}"
  python setup.py install --root=$pkgdir
}
