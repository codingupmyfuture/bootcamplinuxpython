from decoradores_clases.estaticos import Demo


# Demo.saludar("lvl3")
demo = Demo()
demo.saludar("LVL3")

Demo.saludar_estaticamente("sin instancia")
demo.saludar_estaticamente("con instancia")