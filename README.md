# Pokeapi

Available on [www.pokeapi-juan.com](https://pokeapi-juan.herokuapp.com/)

_A Pokemon is a mystical creature that belongs to a fictional world, designed
and managed by the Japanese companies Nintendo, Game Freak and
Creatures. The Pokemon world is available on manga, anime adaptions, games,
retail stores and many more places.
The depth of this virtual world allows to have mountains of data only to describe
completely a Pokemon and its relations around the universe._

_This project takes the data from the PokeApi (https://pokeapi.co/docs/v2)._

<p align="center">
  <img src="https://raw.githubusercontent.com/juanmarcoscabezas/poke-api/main/doc-images/pokeapi.png" alt="Sublime's custom image" style="max-width: 500px"/>
</p>


## Starting 🚀

_To get a copy of this project run the following command._

`
git clone https://github.com/juanmarcoscabezas/poke-api
`

Look at **Deployment** to know how to deploy the project.

## Requirements 📋

_Required packages to run the application and how to install them_

```
pip install Django==3.0.8
pip install django-heroku==0.3.1
pip install gunicorn==20.0.4
pip install psycopg2==2.8.5
pip install whitenoise==5.1.0
pip install requests==2.22.0
```

## Built-in Command 🤖

_Add a new evolution chain._

`
python3 manage.py evolution_chain $ID
`

_Example._

`
python3 manage.py evolution_chain 1
`

_To run the previous command in the application deployed in heroku.
Select the "more" button and then click on "run console". this will display a new window and allow you to enter the command._


## Start the server 🔧

_Apply the migrations._

`
python manage.py migrate
`

_Start the development server_

`
python manage.py runserver
`

## Deployment 📦

_This is ready to be deployed in heroku._

_You must enter your heroku account, create a new application and link the heroku application to the project's github._

## Built with 🛠️

_Used tools_

* [Django](https://www.djangoproject.com/) - Web framework
* [pip](https://pypi.org/project/pip/) - Package installer for Python
* [Bootstrap](https://getbootstrap.com/) - CSS framework

## Authors ✒️

* **Juan Marcos Cabezas** - *Software Engineer* - [juanmarcoscabezas](https://github.com/juanmarcoscabezas)


You can also look at the list of all [contributors](https://github.com/juanmarcoscabezas/poke-api/blob/main/AUTHORS) who have participated in this project.

## License 📄

This project is under the License (MIT License) - look at the file [LICENSE](LICENSE) for details.


---
⌨️ With ❤️ by [Juan Marcos](https://github.com/juanmarcoscabezas) 😊
