#findpackages in setup.py will just go and see in how many folder you have this __init__.py . So it will directly consider this source as a package itself.
#So once it builds right you can probably import this anywhere wherever you want. Like how we import seaborn how we import pandas similarly.
#now or in my entire project development will basically be happening inside this particular folder. In inside this folder.
#And whenever we create any new folders also there also we'll be using this file so that that internal folder also behaves like a package once we build it.