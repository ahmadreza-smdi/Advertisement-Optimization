# Advertisement optimization
Suggest best website to put the ads on, considering the context of advertise

## Deep into the Project
Given the content of a website, the overall interests of those who follow it can be assessed.
Given these interests, people can be grouped into different groups and the promotion of the product or service they want to offer to those interested in the product or service. Generally, targeted advertising is targeted at a specific audience, which may be a specific demographic, group, or individual.
In fact, targeted advertising only means that the ads are selected in relation to the content of the website, assuming that they will communicate well with the site's audience. For example, advertising the sales of a sports team's clothing will definitely have a greater impact on the audience of a sports website than advertising the sale of the same product on an economic website. As a result, targeted ads for specific target audiences limit the websites targeted to upload ads to websites with ad-related content and place the focus and targeting of ads on those websites, which will reduce costs and achieve more impact. .
In order to find a way to optimize and target ads, one must identify the context of the ad. Therefore, you need to create a model to categorize ads by topic. There are several methods for categorizing texts including Mathematical Hope Algorithm - Maximization by Bhawna Nigam1 et al., Simple Bayes classifier by Wang et al., Support vector machine by Mayor et al. The project will try to do this using artificial neural networks. It also requires gathering context-specific texts to teach the categorization model, which is to crawl websites with specific contexts.

## Running the project

First of all you need to install pip3
```
sudo apt-get -y install python3-pip

```
After that, you need to install django with pip -- each version of django is different. In this project we work with djnago v2.0 .
By executing the below code you will install latest verion of django
```
pip3 install django
```
We have all the requirements listed in requirments.txt so you can use that to install all of them.
```
pip3 install -r /path/to/requirements.txt

```
Also the requirements are listed as
```
asgiref==3.2.3
astroid==2.3.3
attrs==19.3.0
backcall==0.1.0
bleach==3.1.0
cycler==0.10.0
Cython==0.29.14
decorator==4.4.1
defusedxml==0.6.0
Django==3.0.2
entrypoints==0.3
enum34==1.1.6
fasttext==0.9.1
hazm==0.7.0
hdbscan==0.8.24
importlib-metadata==1.5.0
ipykernel==5.1.4
ipython==7.12.0
ipython-genutils==0.2.0
isort==4.3.21
jedi==0.16.0
Jinja2==2.11.1
joblib==0.14.1
jsonschema==3.2.0
jupyter-client==5.3.4
jupyter-core==4.6.1
kiwisolver==1.1.0
lazy-object-proxy==1.4.3
libwapiti==0.2.1
MarkupSafe==1.1.1
matplotlib==3.1.3
mccabe==0.6.1
mistune==0.8.4
nbconvert==5.6.1
nbformat==5.0.4
nltk==3.3
notebook==6.0.3
numpy==1.18.1
pandas==1.0.1
pandocfilters==1.4.2
parso==0.6.1
pexpect==4.8.0
pickleshare==0.7.5
prometheus-client==0.7.1
prompt-toolkit==3.0.3
ptyprocess==0.6.0
pybind11==2.4.3
Pygments==2.5.2
pylint==2.4.4
pyparsing==2.4.6
pyrsistent==0.15.7
python-dateutil==2.8.1
pytz==2019.3
pyzmq==18.1.1
scikit-learn==0.22.1
scipy==1.4.1
Send2Trash==1.5.0
six==1.14.0
sqlparse==0.3.0
terminado==0.8.3
testpath==0.4.4
tornado==6.0.3
traitlets==4.3.3
typed-ast==1.4.1
wcwidth==0.1.8
webencodings==0.5.1
wrapt==1.11.2
zipp==2.2.0
```
for the project to run you should install fast text
```
git clone https://github.com/facebookresearch/fastText.git
```
```
cd fastText
```
```
pip3 install
```
after the installation of required stuff you need to download fast text pretrained word vector for PERSIAN language.
you can download from below link.
```
https://fasttext.cc/docs/en/pretrained-vectors.html
```

put the .bin file in root of the project so the project could run


NOTE 1: Dont forget to build your data base.


NOTE 2:Running the project would need at least 8 GB of ram and after the project's run it need 3 GB continuously to maintain the running
so it will take like 20 min to run the project

NOTE 3: this website only works with PERSIAN language

## Built With

* [Python](https://www.python.org/) - Programming language
* [Django](https://www.djangoproject.com/) - Web freamwork
* [Html](https://developer.mozilla.org/en/docs/Web/HTML) - Hypertext Markup Language
* [css](https://developer.mozilla.org/en-US/docs/Web/CSS) - Cascading Style Sheets
* [Java script](https://www.javascript.com) - programming language
* [boot strap](https://getbootstrap.com) - Front-end framework
* [jquery](https://jquery.com) - JavaScript library

* [Hazm library](https://github.com/alifars/hazm) - Python NLP library
* [Fast text library](https://fasttext.cc/) - Python text classification library




## Authors

* **Ahmadreza Samadi** - *Developer* - [Ahmadreza samadi](https://github.com/ahmadreza-smdi)
* **Mohammadreza tohidi** - *Programmer* - [Mohammadreza Tohidi](https://github.com/tohidireza)


*Thanks for your attention.*
