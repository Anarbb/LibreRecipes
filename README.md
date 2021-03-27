# OsRecipes
> A bloat free recipe website made in Flask

This is an OpenSource crowd-sourced cooking recipes website, this is a personal project
but feel free to fork it and edit any code to your needs just keep it open source as the ``LICENSE`` implies.


## Development setup

```sh
pip install -r requirments.txt
```
```sh
python3.9 main.py
```
Put the recipes.sqlite3 in the ``project`` folder and then change 
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///[db-name].sqlite3"
```
in the ``__init__.py`` file line ``6``

Images: <https://anonfiles.com/UfzeydXet9/recipes-imgs_zip>

## Planned Features

* Adding categories filter

## Release History

* 0.0.1
    * initial release

## Meta

Anas Arbaoui – [@Anarbbb](https://twitter.com/Anarbbb) – anarbaoui@gmail.com

Distributed under the GPL-3.0 license. See ``LICENSE`` for more information.

[https://github.com/Anarbb/](https://github.com/Anarbb/)

## Contributing

1. Fork it (<https://github.com/Anarbb/LibreRecipes/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Copyright

Copyright (c) 2021 Anas Arbaoui

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

