from MVC.Model import Model
from MVC.View import View
from MVC.Controller import Controller
from pyscript import document

def main() -> None:
    m = Model()
    # v = View()
    # v.showGraph()
    output_div = document.querySelector("#output")
    output_div.innerText = m.findPath("1", "6")
    # output_div.innerHTML = v.getGraph()

main()