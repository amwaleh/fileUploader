## File Uploader

This a simple project.Uses DRF to upload images


### Installation

- Download this repo
- pip install requirements in your virtualenv
- Run server by running `python manage.py runserver`


## Routes
To view the routes run the project and go to

 ```
 localhost:8000/help

 ```

### Searching
Searching for a file can be done by adding the `title` or `id` parameter to the `GET` method url

```
    localhost:8000/file/?title=alice

    or

     localhost:8000/file/?id=23
```

### Test
`python manage.py test`