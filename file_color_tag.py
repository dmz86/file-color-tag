# File Color Tag Extension for Nautilus
# https://github.com/dmz86/file-color-tag
# Copyright (c) 2025 Marco Domiziani
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gi
import os
import gettext
import base64
import subprocess
gi.require_version("Gtk", "3.0")
gi.require_version("Nautilus", "4.0")
# noinspection PyUnresolvedReferences

from gi.repository import Nautilus, GObject, Gio
# i18n
gettext.textdomain("folder_i18n")
_ = gettext.gettext

class FileStatusEmblemsExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(self, files):
        self.create_icons()
        if not files:
            return []
        return self._create_menu(files)

    def create_icons(self):
        icon_dir = os.path.expanduser('~/.icons/hicolor/48x48/emblems/')
        if not os.path.exists(icon_dir):
            os.makedirs(icon_dir, exist_ok=True)

            # emblem-colors-blue.png
            with open(os.path.join(icon_dir, 'emblem-colors-blue.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFAElEQVRYw+2X328UVRTHv2fuzLbb36Wl9Kc/EqUNVvwBiTGRB2J4IMbElGA04YUEMVJe+A981Qc0MUCImKjggw8uT0rkSQNvVsQGEAqJaNrdlm132912dnbm3nN8mGm73e4UCSTGhJuczOzde+753HPPOfcO8Lj9x40eZPD+Ly4P2mSPwLJGAPSKkQ4AIEVzJJgymlMQSn17+JWJRwqw//NLOwD7ZDKhhvv721X/5pa6pqSDhjoFAHDLBsVSgKmZQnkyPW88X49rxmjq/VevPBTA4dNjziwFpxK29e7QYF+ye3MzLWpBQRsEItAiAACbCA4RWmyFJpuQzhZl4la65AfBuVzGH/3pw936gQHeOHmp3Ra60NnVOjw4NNA4FwimPQ2LANsCLAKsaCwDYAE0AyLAlnobHQ7h5o2/SnNzxXEN2fv9kV35fw2w4/SY0xO4l7v7ul7qebrbmSgEKLPAtsLVKgtQtKosAIwAhgEtAs1AvSJsbXaQ/jMTZKayV5ZmzWu1PGHXAtjiLZ1q62gd7hzY4oxlA/gQONHKlSVQHHqgEoClAoKBYiBY8AK8MNDtlJa87cYsnALw3n09sOf4xZ31ieTP23Y813CjYLBoBLAAolBUhfsp0hZZ3QYTbYNIuDdNirCtxcL1X6+5QaB3/Xjs9TWBaa1bPqsTXQN9yalFRtFjiBFAA2IANoDWgK8BTwOlSLyoT+twjBhEOoKix5haFHT3DyQN04lqc2sAdn90YVApDDe1tlG6aMKJTDjRqgASAYmueq8aiwgmXTRobGsj25Ltez6++Gy8Bwzta2rtUHMuQ69MuGoAGhAdGdBVEvWhEioSrYGcK2hq7VSB4ZFYAA3rrYbmtrq8y6srqAEi1UZq9S1DR17JuwYNza11hmkkNgs40ANKJVAqCYQBWBKGKQNEBKGKsK0OX6l4CiAiq+8MlFigkgmw4f5YAGNMO5GNIOCV6EYU/UISbzwWYjlHAd8IqMGGMXpTLIBmA60j1y+XOKohGzWpARCxa81g5vhCJIyc5/k9FjswItHqa7ueqkBENt4Kiwilkg/DmIvfAqHJkuv12OTA11Wup0rjtGJnLYSs88KyJ2wbKLkeDGMyNgtEB6lCPusliNZGc0Wkh5khNQUmJhsMkCBCIZ/1EATfxQKUjU7N5zLsQGDVSC/o+6ch9Po+ywAOBAv5aQ4Mn48FuHn8nYmgbMYXctNcb1VVtXUVLwakogwvS1IB+dkM+4G5ev2Tt+9seBb4ujx6L3PLs9lAcaURia+CVdUwfIZ6igFlDGanJzwtwWi1PVXdkfvlfGbTzpGnPDc/1NLckQg0h0UpymcIRUdfRaBxpQjAAmGGJQYNyuBeetz1y+7Z258dOLPhYbTcejt7jhSX8teyM3/4dVQGGQ+sPciKlEMJIln+Hf3P2gMZDwmUkZ25WS66ud/7uvqOPtCV7IkPvmkn1j/UJxqf39S1tZFFQXOoQlRbTURAkOjOYJC7d9v1/MVxKvPeu18enK+lo+IAFsZS3sKbL37VmGt4slDIDBGJSjgJImGANUQ0hEOBaBBrWDAgBHAXZzg7M1HSpnz27967++c/PeY+1LW89+DplwHnBAjb6+uarWSytV6pBJRyojMkgDY+PK9Q8koLAuAqjBxNf33ot0f6YbL5wJlnHJv3EawRAfUJTGc4iZoFYRKsU4FRqey5Q3cef/P9b9o/bjfKOv4y68QAAAAASUVORK5CYII='''))

            # emblem-colors-brown.png
            with open(os.path.join(icon_dir, 'emblem-colors-brown.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFHElEQVRYw+1XW29UVRT+1j7nzHRmenFKy7TYRhrRIdBWBeIlqInxRdAYU0KikVc1Wp78IQZjEE18QMEHSKwP3t4MaAgYb0CEeCHQaLGl7XRunXPmXPZaPpwz05mxUyCQGBN2cjLntuf71lrft/Y+wJ3xHw+6mZeP741nDZIJpdSEkGwQlnUAQIpyELrKEkwpGFMTx9zfbyuB43ut7SDjXSvZObpuKGukN4zE46m7YCVSAADfqcCtFJD/+7Kbm/lN+3blPJOefPGY/9MtEXj/VVjdufghM5l8aWjr44n04AgFpWvwinMQtwz2HQCAshKgeBdiPQMwuzPIz16Wq7+ccnzHPjqQcyefOoHgpgl8/CzSHI99ld5w7+jwA0+m/KW/4Fz7A8QapAgEgCicLiIQAMICUSYSmU2I9Q7jytmTTmnu8nlV9Xa9/AXyq+EY7SInN/Z1/8jYtsHs9o7ipe/gLM1AmEOgGqAIWAQsAHP0qzWqxXm4pQWszz5isZbMcin39IMD+vCJaXArlrkaAXM+fqhz/fBo38Yt1sLFbyGBC0UEVgIFAoXh19MnYRogAjAEwoBfzsO98A367n/Msiul8SH58xDgvnLdEry329oRS6ROZnfuThav/AjtlKEUQRGBKASnBnA0kJCIRD0zLDASXege2Y5fT31ua8954rXPmoWpWgmwwsH+kS2J8vw0qstFaBZoLQg0R0fjeeux8kxrgWZBdbmIyvw0MiOjCQYOtuI1ETjwTDxLZmI02Zuh0tx0CM6MgLl+rhsBo2croBy+wxLNCc+Lc9NI9mYIZmL87efi97UlwKL3pHoHjMrSLALfi8CkATT64xq4ljb3uHmu78HOzyGVzhii9UR7AqAXEl3puF1YjCKuZUCaIv13KVrKEs3R9cwJKoVFJLp64wHTRFsXaC3DyojBtssQzWCqiU8iAUqoXCIA0uyCSISRIeqCZJFQlHYZnd0ZaJah9gQEaSjA9zwAAkUCrikfK7+oEWkhAAEEkRPQ6AgArgsQQWv0tiXgC+D7PrRmADXwlegbu99qNmzqitJsS5CC7/nwZY1GJFqWXMcZZGWCo+bTGD3QUIa2BMKrxiywCJRpoWrbEJHcGiVQM7a9PAgyoLWAm6JvAaeWIkgzicYSiADKMmDby9BazQB6dQIBZKqYL431dHd0BHYZqpbypizUsKmx+mErbiGAmgYAWFYcpVK56kM+aWtDl42pQrnMUDEwI7Rf1NWabMirdMPGe8wr3ZMFzABUDIVCid3A+HTNteDNR83T/f29D8eJleeUWjSwIsJ2o8mKURliyR44GpzL5c+8dTrYufZaAJq8tpivasMCk1HvdNdfB1reiboikwGtTCzkClUOaPK6+4EzMzy7Y5A2Vj1/cyrVGfM9t77WhxHV9gASCWzlunZoBjQDDAUz0Y2FfMl2/eDIO98HH9zQfqAvpd+YXfbGmSsP9aRSscC1IVpH5UAkylVsKKj3AFIGzFgS84WK69jeuYFuvf+mtmSvjyHtW8aXccMY60zFUuAAHATNTlilDwAEMgxAmSjZnh0E+rzPetfhsyjc8JYMAH6YR/X5rHy46OAeuxpsZlGGMgxiIWgBWEKXaAEYBC0EhgEmBcdlLtieE7AcGe7Rew+cgX1L2/J949Y2A3wQwLhBUKZFHapBwRwdQSBOwBAIzkKp/R+d83++rR8m+7ZiE5tqDwlNEHC3FvQBgEFYFGAGIlPEPHX0Ai7d+eb734x/ABJG+UzrdIdDAAAAAElFTkSuQmCC'''))

            # emblem-colors-green.png
            with open(os.path.join(icon_dir, 'emblem-colors-green.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFD0lEQVRYw+2Xz29UVRTHv+fe9+ZnW+wPsK0QrEpbpTRBSAGFjYkLEhemxIV/gJL+2Lh0YcJSdybaFhM3BrfWlZiYmPiDAAIBhIVpNSHqQJHaX9N23q97z3HxZobX6QxCIDEm3OTm3vfm3Xc+7/s9J/cO8Lj9x40e5OGRyf19Sulhx3GGIdJtjGkHAMdxFgC6GRkzTVamJ8YvzD5SgJHJA/scR01mU7mB/l19umdHT7o5twW5bB4AUPLWUSyt4MafN4KZX2esH3rXbMhjE+PnLz8UwNuf7HNT5E5l3OybLw0NZXdu76EIKwhRBCMASwgAUJSCQhoptMDFFvxeuCFnf7rg+ZH/ecdceuzEie/MAwOMTB5uVTr6euf2nQOHDhzMh7SAdTsHIkCRgiJKLBewCFgYIoS87kRa2nHm3FmvcKtwzVrn6NTomaX7Boi/3DnT19u7d2B3v7toZmHhQ5EuB1cgKFB5tQggYLBUuoVGFu1uL65f/yWamZ293DGXPVxPCaceQErcqc6uzoG+/mfcgn8FgIFSGoo4BoAC0UZ2EQEnIAJeRslcRt/zu93i6urgbdyeAvDWvypw/KOh/bl85vtXXj2SWzAzsPCgVCy5ojiwIgWAEgZUbOAYRDi2hBkaWXToPnz7zQ+l0I+O1CamqgVwXZrof6EnuxLdRCkqwlgLYwyMtYisQWQNQhshsiFCjhByeW6j6u/JNaWoiGVzC30Dz2YpxRO18VRtnTuOO9C2rY0Wg5uw1sYvsxZRYm6Mia+N2Tiv86y1FotBAe3bWslRqcHjJw/saqwAq2Nbu9v0SngHoQmrL6sEiCrd2rvzOvcqUBWQ0IQohvPY2t2uFdNwwyRULl5vaWtKr4aLMGzBRFDMUCr2nij2vTImy0DKiVgdyzkQl6egKAtoaW1N64IdBvBBXQBh7NCuwmq0BhZTTT5ijsdyRxmitgqQDJ4YmRlM69jitkNEbW9chiKtogWBH4BIoETKWU+bFKjXNimQUELEB9ICZmm7BwAQRbH3RLLpy5MQdQESwWshAEJkw0rN1gcQhUUv8LpEAANbDa6SgWv9v/v58bsTKiRt0HBQ8jyAZKEhAAEFrxR0cVrBcJwD1aSrgcCGnQCbk7HSATAzSKXgBz6IpNDYAsb0+pK/J93pZoy1IOZNwakmOGogpB6ECNLKRWnJ98Xgi8YKCE37y+F76W0pGBYADJVQAAn/G1ZBRYmK/BVc1igtBUzkfnnPvWBkcuhc6kk1xPmSCnhtg/+NSrBuKSbyIK2aodYzHPzF50+OXnz5nruhYjUWzvOPKuPmjFUQ2PIZoOJ/JQU2b0Yi8YUA5QQECBqudmDmxVeCsdp4uvbGxdOFuf1Hu59GQP2cVanAhLCWYRmwLLBWqqMpd2sT15y4zwRXNUHdcUti5dTU6KVP7+s80DmfH53bujaIBb2XmjOpkL1YCVC1+upUYeJwIiBopFQGtKAD9vFz13zT+AMfyUSC05Fj9hTza3lDIVhs3eBJiBhSQYuLJ9ZbStrqa9kgOvrhO1eX663RjQAuffWH/9pQ72dezu7MBOl+I6IDGGKhu5JzbAdbwDJBREGYkA1y3Oa1eMR0qnu+6Y333z1feqhj+djHB180ZCeEeHCVPLWu/EwEA0OxIo5ouOIgz1mvGRmB0FWlMH5y5NKVR/rHZHTi0HMi9hgrOyyCp5SoDgBg4r8BFBzoaUBPT46d++3xf77/TfsHCOWGX0xzfN4AAAAASUVORK5CYII='''))

            # emblem-colors-grey.png
            with open(os.path.join(icon_dir, 'emblem-colors-grey.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAB7FBMVEUAAABAQECAgIBmZmZAQEA8PDx4eHg5OTlOTk5nZ2dRUVGAgIBpaWl8fHxKSko+Pj49PT1NTU1wcHB6enp9fX1sbGxTU1M6Ojo8PDxnZ2dTU1N9fX1+fn5mZmZBQUFKSkp6enpJSUlAQEBycnJxcXF7e3s+Pj5PT09ISEhAQEBEREROTk5sbGx8fHw8PDxGRkZYWFh0dHR3d3c8PDxkZGRsbGx1dXV7e3tXV1dlZWWAgIB/f388PDxZWVliYmJ/f39aWlphYWFOTk5XV1eLi4s/Pz9CQkJNTU1UVFRWVlZubm5vb291dXV/f3+AgICCgoKEhIRMTEyFhYWKiopLS0tcXFxeXl5paWk7OztYWFhcXFxfX19+fn6AgICYmJhYWFiPj49YWFhZWVltbW2RkZGhoaFYWFhdXV1hYWFmZmZnZ2dpaWlqampra2tsbGxtbW1ubm5vb29wcHBxcXFycnJzc3N0dHR1dXV2dnZ3d3d4eHh5eXl6enp7e3t8fHx9fX1+fn5/f3+AgICBgYGCgoKDg4OEhISFhYWGhoaHh4eIiIiJiYmKioqLi4uMjIyNjY2Ojo6QkJCRkZGTk5OUlJSVlZWWlpabm5ugoKCmpqanp6eoqKiqqqqrq6usrKyvr6+wsLCysrK0tLS6urqcIBGCAAAAZnRSTlMABAQFEBERJCQlJiYnJzAxMjIyMjM0dXZ3d3h4eXqYmJmam5ucnMXFxsfHx8fHyMjIyMjJycnJycrKysvk5OXl5uf09PT19fX19fX19fX19fX29vb39/f3+Pj4+Pj4+Pn6/f39/v5KPzS4AAABvklEQVQ4y72TzW/TQBDF37gmH6VR2lDAtKFURBwq5YBIr3DhCCf+Y8SdA0UEgShqG4WmpMVJm9iud+dx2HViVb3CHsYjvZ9nd+btAv98SSlvNJ+Ej3GSH8Wz24DNTtR8dSeAmveTw+H5TWDl6d7Dl6mlQSgrtQ+nB8fqhNB9Kt3Wu/ScAsCC81610vp87f508UX37TQhCACEZqab6hmXQKfzOs4BgiRB0GTPxtmfBXD/+Zur60J3hLV7F+MEQAAAu5FJqEpVkj5JTLQFD6w92I+ppJKq6hPG+zt138VGK7cQUFg0T5Aw99YTV6HdS5QsdnB7kDrvbfsKtSAlRYiiBAESWW3VA1uBocDpAhZELpEHaBVOX8oAofTAMA2MQOhkf0gwTE49kCZCimtCinETMr/0k9TVKHOdYREI1voHM1chngq01IQ7gshk6ivk1bWmIZxTRUTl5NOo8GI4gFBV3ZBIVaVg8GvhZqqznVwXbpJUVD72z5b3YdK427C25KaEx/3D0o3CRXq5CavOTSX45dt3LQM6FtZDkEoQnP/8+kNvXvv1R+1mSwTk76uj0eS2h1Pd2K63MZiO4gz/c/0FnUZJ63HiTBIAAAAASUVORK5CYII='''))

            # emblem-colors-orange.png
            with open(os.path.join(icon_dir, 'emblem-colors-orange.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEvklEQVRYw+2Xz29UVRTHv+fe9zoznba29DdthYVQG4ZGoQYXsmiMiexMWUHcuGFh2UJcaNKl/wA0kY0RXFp36sZolChExLaKgVIjwnRa+rud6fx4791zXLyZ9s2PBzSQGBNucnLfe7n3ns8595xz7wOet/+40W4G//LhUD/ZMqIsPQLwXvGkFQDIohWCmjOumTDwJo6NTc08U4BfPzpylCy6qCP1iaaDB3W878WI3dAEHa0HAJh8Fl5mE5kH/xQ2Z+4aU9iaZvFGh8ambz4VwI0zR23VzeMUiZ3qPPZ6LP7ifhJ3DcZdBTgHEcdfhOoAFYO294DsFmzdvyeL16/lXCd/JYOm0eGx771dA/z4weGWWJ36umHf/kTXseNx8Zbg5ZMAGCAqzixNF0AAiADQsKI9IKsdCz/9kMsk70/nHHPi+Me/rz0xwI0zR210eFebBw692nY4YbuZOxCTBYhARAGAQCsCiAggAtJx2I39WJ6adtfv3LqZ1nveqOUJVQtA2gvj9T29idZDL9vO6hTESQPMADOkJKZCit+3xzmbcFYm0ZoYsOPdfYNxd3W8lq4qgOvnE0PKjp7qGhqqd9duQ7wCxAiExV/cBKSksOKbsPhzvALctdvofG0opqy60z+fGzjyWADRfKF9MBEzuYUyy2G4COJbXKaYA14wUgYnThqcW0DHK4diSusLjwS4er6/X+tIIt7VSSaT2l60ylI2VVsANlWeKcF6mRTinV2kLXvw2rmBA6EA2tDJxt69mvOrgPEAlqLlOxaWubuGBOPDhxHAeOD8Khp6u7UQj4RvgZJ34h2tEc6tBYJKAh4wAQUmEJAmAGh2xrNsj+HcOuLtrRESlAFY5QEgfXbEhrhZfwEiSDHlqDL3a6VhoCb46VisDSIQycKONoFZekMB2HgtZFkwuUJR107OCwIAYeVLAkUJ5QDMeeiYhrDZ8wgAAVwHMAKBbAMQFWEQ6MOayHYvAQBAQVzXz5LQLSCsevlstxIFEQ8gH0JQG6D0KFIbYLsXfwu97BagsBIKoCBJJ53pjtRriOfsWF7l+tK21HB/5VaUPGFruJk0AEmGZoHn8kRmfilPsMvyWALpBVOj+plgsaqeB2YQbKQXlvNc4C9CAZRrJjbml1lIA4yaysrSrkxMdZ0ovTMgpLExv8SGzJehAMcvzc2IcabTc4sMFakoQKYCxlRIUKkp8wLpKDaTD5mNOzl8MTn7yLPA8Xh08e6DvLACQe1YHnL6hZ2OpXkEBTaEpdlknl2MPvYwevOT1E1j+PPUn/e2hCJ+INU4fMJioOxZAKEI5m79nWXPXB6+NDf5ZPeB7tT7W2vpPx7+lXKEbD+TguXXhEgwPgQQ2FicTRVyG5kp3jt/dndXstMvtHj10a+iDdHDPQc644rErw1PcI8l0mAhpGYeZnPZ3DRc58Twp+vru76UfjcGix+0jxPodEdfc7SprUFR4PoFKuV9sGQDG8sZXkmu59nwZdq3fHZ4DN5TXcu/fa/tiCi6QILBxuaoamyuj9p1Fqw67dcPx8AteEivZ3PpjbwAmGQPZ9/6bOm3Z/pj8s277S/Zik/CwggJegyjDQC0wjKAJDMmPKMm3r6yNPv8n+9/0/4Fogz35KaCXREAAAAASUVORK5CYII='''))

            # emblem-colors-red.png
            with open(os.path.join(icon_dir, 'emblem-colors-red.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFOElEQVRYw+1XTW9UVRh+3nPvfHdKp9BK0UYlQj9oK6VGF+AHxoW4MmWlezeUlSvjisSF/gHoxh1urStFjVEMJBJDCq0SoDGCSWmJbYeZdj7u3HPO+7q4dzp3hg5SJTEmnOTknJmcc57nfd6Pcy7wuP3Hjbaz+MbhgQGCM6lizqQI9sCYnQAA110D4Y7UeIatnRn6+cbCIyVw/aXBCYm7Z1Q6M5I9OOKkh/Yn3NwOuNksAMBsbMDkiyhfv1krzV2zXC7Pw9ip4UvXZ/8VgcsTE7FEvDZN6eQ7O4++msoM7iOpFoHqOmBqEOsHhzhxwE0AqU5QagfKNxdk7fsLVa5UPltL9EwdPX/ebJvA/JHRnNV8LrN378iu149mZGMNNr8MUgC5CuQQoMLtLBArEMMQJjjdu0HZbqx890O1evvWvIqpY2MXf7n30AQuT0zEoLyL2QMj4zufH4vpPxYA44FiTgiuAEeBwt0iACxDLAcktAViKcSe3o+1uTm9ce3X2Y10z5GtlHC3ImBRm07t6R/JDQ7GqvNXAGugYg7IcANcUYO+AMLSIKEZvF6AKcwiN3AgVssXx5KLi9MA3vtbBS6Oj7ygkskfn33rzbT/+wKkWgEpCnsgPTkqkD9CIHADB65ghrBAWECpNOJ79+PWl19XTKX88ivzzYGpWgkYwenuoeGUv7wEU1wHG250bcG+hfU0uNLcrafBvg3WRPaY4jr8u8voHh5OseOebsVrInBubGyA46mRTG8v+XeWwkNsU7c6ALHh3IZzDuet69kw/MU7yPT2EseSY98eHNrXlgAxjmd6ex1/ZQXW12AbtZ43Cdm6GpFuN8lG1zLYMqyv4a+uoqOn12HrTrYlwEJvp7u6EjqfbxxmIsDaBodHLLcRVVhzRIXmvTqfRyrXlTCsJttmgWbpd90YTKkCGAYpARGFEU9B2hEFsUct8SsCqY8SjiyQ+liqwMl2wzCeakvAt8gRCNbzQZAg8imIdqLGvA4eTYLNgiAIQKNzFoipIUEEbbm7LQErBFvzwcYGBCiodhS1nkLo1gQOzG9YH4IjVAEIztZC7QuRAeVr5WofoCBGN6yvu6AufXv8ZldwQwW4MXilClhorS0Btlislip9KSKwsaHFLf6PIjfV4sg0GgeBFFCxOKqlKtjSYlsCVaaZ1UJptD+TSFpdDmPgfumJtr7D6n6/zxUsUB1xrBXKXpXV5+3rgOaZlaLHrBwwS5hu3BjD9NosQC29ka7ctJdZwMrBn4UKG4svHngXnOkf/6m/u/PFnDIKpRIUSZP0m9ZvGQShChFXsBAom8WaIV7Mly6dWLxy+IG3Yc2qqdv58oXUE11pKA0yBooEBAnvH2lgt+ShABAQgtgjsBDEdQGVxO17Bc+KTLXiOa1/fLOxvPxGpu+Zks+D2Y6OuPYtDBMMFKwQjChoKBhRMOFvIw60KBhW0KKgxYFmB4ZcSDqLW/cqFU/z2feXZj99qPfAxnL2hN5dGiN4472pjrjUqoDlUAmEdm7lAQpvZgreDPEU7ha92rpXm6ve7Ty5rSfZxztGczaR/CoZc0b7kpmMYgMYswlOLS6QOglSgOOAlYMlr1LxtZ3Xvj52qnC1sO1H6Sm85qKnPE3Au7l4MtnpxBXAm/lN9YCL1AtAoWg8Lmjfg8hZWe04eQr/4FEabR/umjikxDkNwliKXJVy4kkXBCfMCCsCA4ZndbUiRiBylZSc/Gjl8pVH+mHyQc+h55Rxj4NokiBPMskuAFBCqwIsimBGXDPzycrsb4+/+f437S+QarTdBIq56gAAAABJRU5ErkJggg=='''))

            # emblem-colors-violet.png
            with open(os.path.join(icon_dir, 'emblem-colors-violet.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAFG0lEQVRYw+1X3WtcVRD/nXP37maT5mOTNGmaNA2xbSqkkX7ZBxEUfamFIilCxYKgqLTpi/+Bb1aRWh/6BRaqbV8E0wdRHwSpCIK02BpUbEybNm3TJtvsbj52936cmfHh3k2y6W6T0IIIPTDc4Z6P32/mzMydCzwZ//FQy1n81e5TXQp2r7LRK6xWC1MDAChtTSgldwxRP7Tu33v+zcHHSuDcrtNbbY1jkUq7u+mpJiuxti4Wq44hWhkBAHg5A3fKRXok7Y5fS5Lv+APC3Lf3m7d+eyQCJ7eetGuaI8cj8cjrHds64w3tCeVPezDTLtgjsE8AAG1b0FELkeoY7OooUiNpGb44nPdc/+zq7K2+Fy98YJZN4NyuYwk21vf1axq71+3YUOWnHTjJLACB0oBS83YLIAIIA4BGxcpK2IkKDP16NZ+6lRrQEbPzjW8PpEvhWOUsVzH82LKudUvHps6K6aEM3Ak3AJAQkAEQIAQwB08hgI3AS3vwJz00P91qk6HmTHLqpc3t209fuHGBF2JFShGI1HnHa5ubulvWt9npPycgJrSaAaUVlC7hu5CUsEAYoEkf6T8m0LKhzc5OZ3vkDh8H8M6iV3DihcPbKmLxn555eXtl9vo02CEopQKZ5/pSVzD/KkQEIgJdYaGqsxqXf7iY8/PO8+/9/H5RYOoHzCfraGtXRzw/loc344GIQcxgZjAxyAjYCMgHOBTyA9eTETAFa4kZRAxvxkN+PI/2rrVx1uroQrgiAkee+6hL2aq7dmVCZceyIBYwB4cSMYgkOJzmAObrwZwEOjGYBcSC7L0saprqlbZUz2c7Pl5f3gO+7EmsbLDyKQfk0ZwlLMWAIUixSDGhcA8zgzyCk3KQaKq3lJLeh13BqysStTE34wYHLAQpZf2S5gROxsWKukSMhHrLZgGRWWNHo3BSLsASBp9AhVEX6AgjsCgGQ0WCLJWCLkFQisDL+YhW2yBf2soTMJTQ2gJ5QcLPRv8siQJ2GQIhIARF4CICkKDCioOMX1+WgGED4xGIgnqhVIEEoApWKzUL+SCBALDwnCMAQAnIMzBM5QsRM6fyOadFtATFRwXuVgi8EDhBzVaQIgIy64O5ehAqIoCKKORm8hCRibIEhOR2bjrbYqsYiHjW/QEJLI9AISZCL1i2hfxUFsJ8u2wWeOz3T4yPOcrWpaOZlpAFZdYrWyOVTDqu8b4uS8AY6r8/fpdFIywixYfwgvw3ocx/x1RiHwtEA8nkKBum82UJfHj98KDr+gP3x0dZRa3ZHOZlWDpHhGdriY5ZSN4dZdc1Vw5d+3Tood8C8ty+m8NXHdYGorA46CJkRAGkDEZGrjrkO32L9gO/TF+8+2zl9o6Z7OTG2obGKJnQhSVyu5SwhN8AYbASqArgxvW/cm4+d+aTO8c+X1I/UDPaeCDDYz23RgY3r2rtjBqHAA5qQKEElWgHCjkQ1AINWLbG6M1/3Ml0+ve6saaDy2rJ9tfuT0Ri5rt4ZfWmVe0bqpRoCDHKUZACBSVQWkMU497IYM7JZQe05+48kjmdWXJLBgCX3EvOK9ndX2Qi42tT46MbobUViccVKwaBYYRAoRgQWAmCOUEmNcajw3/nPT93pjHZ9toh50jukdryd2v3bdGwjkLrntiKGl1Vk6iw7CgsOxYEru+CfA+5qUzemZkUiFwB+OCJzJeXH+uPyds1+9ZphT0aVi8UWoW4EQCUpe+LqNsA9ZNI/6mps0NP/vn+N+NfZlFaSSzgIZsAAAAASUVORK5CYII='''))

            # emblem-colors-white.png
            with open(os.path.join(icon_dir, 'emblem-colors-white.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAD7ElEQVRYhe2WzU8bVxDAZ95+GFdFrI0AQUGWQYpC86FIAYkLB465teTQRggBNwj/BH8EOOWe9hZyQi0S4kR9clrFHBCOQFgEYWPFNuJrvbvzpofEZL3s+qOt1B4y0tPuvjdv5vd2PvQAvsh/LNiKcjKZvCuE+F5V1afM3Cel7AQAEEJ8AIBjZn6FiK9HR0f3/lWA7e3tEV3XV4QQ97u6uhTDMEKapoGmaQAAYNs22LYN5XK5UigUiIh2mHlxbGzszT8CSKVSmuM4PwkhfozFYmHDMBARgZn9jX1aK5fLnM1mr4noZ9M0n09MTDgtAySTySgz/xaJRO7H4/EwAAAzAyLeOHNLFcqtc3BwcH12dpYmoifj4+OlpgFSqZRmmubvPT09j/r7+zUp5Y1hr2OvMPONrhACjo6O7Hw+/0c4HB4fGRmxvfrCz8jFxcVqe3v7vd7eXs22bagCMHPNu3d49Wzbhr6+Pq2jo+Ph5eXlCz9ftwA2NzdHFUX5YXBw8CsiauioERgRQTweDyPis62trccNARBxZWBgICylbHha92ikF4vFwsy8UhdgY2PjLiJ+G4lE0H36qoN6jurpEhF8qqAH6+vrdwIBiOhpZ2en2mycW12LRqOKEGIyEEBRlO8Mwwj5xd6bYH6jUY4YhhFCxBoA1f3hOM6Arus1peSu62bF3ROqT0QEXdeBiPoDAYjIUBQFpJR1DQcBeTukG4CZQVVVIKJoIID713kNuZ0GteIgGPe7lLJmcw0AMxcrlUqvNwx+EK06R0QwTROklMVAAAA4vrq66lVV7/RnY820Yr9vZgbTNAEA3rvXa6rAsqy1QqFgVjf4ZXRQBfg1JG9IT09PTdu2X9UFyOVy0q/sGjWgRmXLzHByciIdx3kdCDA9Pb3nOM5OLpeTiOhb+8049u5DRMjlcpKI3k5NTb0LBAAAqFQqi5lMxnScj3eIeiGoN1edB/h4Y8pkMqZlWYtef7cAZmdn31iW9Us6nb50HAeICIgo0EHQXHWf4ziws7NzZdv2y5mZmT+9/nzT3TTN58Vi8eHe3t6joaEhHQBqLiONGpE78fb39yvFYjF9eHh46/QAda5kiUQiEgqFfu3o6Lg3PDz8tRCff1YznZCIYHd39+r8/DyNiE/m5ubKLQEAAKyurmpCiBdCiGexWCzc3d2NQojATlhN3Hw+L7PZrMnML4+PjxeXlpZav5S6JZFIPFYUZUUI8SASiYhoNNrW1tYGuq4DAIBlWXB9fQ2lUskslUpSSvlWSrm4sLBwK+Z/C6Aqy8vLdxBxUlXVSQD4hog6AQAURfmAiO8ty1pTVXVtfn7+XQNTX+T/I38B2stYAcRrhGoAAAAASUVORK5CYII='''))

            # emblem-colors-yellow.png
            with open(os.path.join(icon_dir, 'emblem-colors-yellow.png'), 'wb') as f:
                f.write(base64.b64decode(
                    '''iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEyUlEQVRYw+2XzW9UVRjGf++589WZaSulfEswRmAD5XMj4sIlGyUlkWBijFvLwuifYUzcIH8AGldWExNdEgJRF6RCJSEBsZEAUlragZm2M/fe874u7p32ztBBUBJdcJKTe+fee8553ud93uecgeftP27yNB/PXGanuNwoUh5F/GbT1loAccX7mLuNLoyb6vi6vVx7pgBmJjmAlT8nGNhVXvNmkKseLga5DUgwBID5OXx0l6hxvtWsfefR+qTZ4ti6PUz8KwB2kfxMvnQaGThR3fhhX6H6mgghZi1AwXw6SwA4RIoYBcLGBWvc/WzJfP2L9bXmmLxB/NQA/phkTSEq/FDsP7yrf/PHFSHE9CEgSLpgZ1PMPGCIG8AoUL/zyVJY/3mylW8e2TbC/BMDuHiR/BZKF/qGju6rrj+RV38PLE4XDkBcOrQ93JJuCvgEiORxwToa976Klua+ndhYbx5ejQm3GoBNVjydqxzYVRkezftoCrQBFmEWYRZiGoJ1dtMweWcRWARax0dTVIZH87nKgZE7ldLpJ2Lg5gUOBsWhc8PbPy2j95PJ0shFXIrZgXQNNUt0gWIpE6RM4NYyc/2jxTief/2lVzuF+SgDrnCqf8PxPvQBpvWViKwdYSJC01YStYbJvbWW3yespIxpHfQBA+uP90Hp1GNT8PsFdiKVXYX+3aLxdLpwtDLxI9S30p55pmEGSDJe42kKAyPiKI3cOMf23gzE7lhxcH+Ar4G1lnO+nOduFla97/4+SkBqjeLg/gDcaG8AUjjaV9leNJ3vFFgHC9mou+41CyTqnMPXKFV2FJFCB4Bc9odX3eryVUwbyyUFAWI+FZ3DEDDpIcJ2VzDDaItRQesEuSoa64s9AWgcr3Euj+kSgiQ1j8do131yFSRZp9s5uwC0qwLzmBkueAHVeKgnAFNAmwlluJQBh+AyUUvCwiMVnGEgZcOWAWj6vIn6zlGdDKibi6PaJpczxEIwB5LSTtb9JDURyUROFwDNuKNiEhCHc6DufvJuNQaQW2FzdlNfpZwILjUdaQPoyL10ZcG6tKAJsBSAUCRqzqImt3qLMPbjC3O/7S5V9pRoAzCHSSZyS69C515gXWnoYEIxKdGYv9FU77/uWYYa6fjD2Sk1s47SM3vU+9G0JLW1ikF1e0aEmVGfmdJQ9ZueAPaOcs37ePLh7HVFcpn6fpwJ9TAjDVc8QnLUZ65p7P2lA2/xW88UAMQ+Hrv3x6/nq4PDZXHtQ4eAuTT98phjRKp+Y0WEEmCxZ/rmlSZhPPa32/HBY0z42H95+/rEAhaAxctMrGy5j2EgG7nFYAG3r08saqRn9r3NpSc6D9TX6geLD+av3J26GkKAWbyyULoLrthwawVchxXHGI7pqauthdr85YfD/uRTHcnOf8maQhB8X65Wdm/d8XJFAksiQnoMzRSlBJgXbl37fXFxYWEyv+iP7Huf2lMfSs+eJVf+051GeGfDtg2lwfWDLrHhbLlldCGCYdSmazpz815TjTNLm/TkG//kUJptP51hPyKnRGRkYKjs+oeqpUIpR74QABCFnrAZ0ZhrLD2YWzIzu2TeTh56j1+e6R+TH8/wiinHXE5GTdmiyjCAc8yKcEvVxkUYP/RuZ6k9b//r9hfj66gsrD26EAAAAABJRU5ErkJggg=='''))

            subprocess.run(['gtk-update-icon-cache', icon_dir])
            print('✔️ Icons installed and icon cache updated.')


    def get_background_items(self, current_folder):
        return []

    def _create_menu(self, files):
        top_menu = Nautilus.MenuItem(
            name="FileStatusEmblemsExtension::Top",
            label="Set color TAG ...",
            tip=" Add a color TAG to the file"
        )

        submenu = Nautilus.Menu()
        top_menu.set_submenu(submenu)

        states = {
            _("Red"): "emblem-colors-red",
            _("Orange"): "emblem-colors-orange",
            _("Yellow"): "emblem-colors-yellow",
            _("Green"): "emblem-colors-green",
            _("Blue"): "emblem-colors-blue",
            _("Violet"): "emblem-colors-violet",
            _("Brown"): "emblem-colors-brown",
            _("Grey"): "emblem-colors-grey",
            _("White"): "emblem-colors-white"
        }
        emoji_colors = {
            "emblem-colors-red": "🔴",
            "emblem-colors-orange": "🟠",
            "emblem-colors-yellow": "🟡",
            "emblem-colors-green": "🟢",
            "emblem-colors-blue": "🔵",
            "emblem-colors-violet": "🟣",
            "emblem-colors-brown": "🟤",
            "emblem-colors-grey": "⚫",
            "emblem-colors-white": "⚪"
        }

        for label, emblem in states.items():
            all_have_emblem = True
            for f in files:
                location = f.get_location()
                if not location:
                    continue
                path = location.get_path()
                gio_file = Gio.File.new_for_path(path)
                try:
                    info = gio_file.query_info("metadata::emblems", Gio.FileQueryInfoFlags.NONE, None)
                    emblems = info.get_attribute_stringv("metadata::emblems") or []
                    if emblem not in emblems:
                        all_have_emblem = False
                        break
                except Exception:
                    all_have_emblem = False
                    break

            emoji = emoji_colors.get(emblem, "")
            display_label = f"✔️ {emoji} {label}" if all_have_emblem else f"{emoji} {label}"

            item = Nautilus.MenuItem(
                name=f"FileStatusEmblemsExtension::{label}",
                label=display_label,
                tip=f"{_('Add color')} {label.lower()}"
            )
            item.connect("activate", self.set_emblem, files, emblem)
            submenu.append_item(item)
        remove_item = Nautilus.MenuItem(
            name="FileStatusEmblemsExtension::Remove",
            label=_("Remove Color TAG"),
            tip=_("Removes the current color TAG")
        )
        remove_item.connect("activate", self.remove_emblem, files)
        submenu.append_item(remove_item)

        return [top_menu]

    def set_emblem(self, menu, files, emblem_name):
        for f in files:
            path = f.get_location().get_path()
            gio_file = Gio.File.new_for_path(path)
            try:
                info = gio_file.query_info("metadata::emblems", Gio.FileQueryInfoFlags.NONE, None)
                current_emblems = info.get_attribute_stringv("metadata::emblems") or []

                if emblem_name in current_emblems:
                    current_emblems.remove(emblem_name)
                else:
                    current_emblems.append(emblem_name)

                info.set_attribute_stringv("metadata::emblems", current_emblems)
                gio_file.set_attributes_from_info(info, Gio.FileQueryInfoFlags.NONE, None)
                self._reload_icon(path)

            except Exception as e:
                print(f"Error modifying emblem '{emblem_name}' on {path}: {e}")

    def _reload_icon(self, path):
            os.utime(path, None)

    def remove_emblem(self, menu, files):
        for f in files:
            path = f.get_location().get_path()
            gio_file = Gio.File.new_for_path(path)
            try:
                info = gio_file.query_info("metadata::emblems", Gio.FileQueryInfoFlags.NONE, None)
                info.set_attribute_stringv("metadata::emblems", [])
                gio_file.set_attributes_from_info(info, Gio.FileQueryInfoFlags.NONE, None)
                self._reload_icon(path)
            except Exception as e:
                print(f"Error removing emblem from {path}: {e}")
