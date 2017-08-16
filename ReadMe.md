## File Uploader

This a simple project.Uses DRF to upload images


### Installation

- Download this repo
- pip install requirements in your virtualenv
- Run server by running `python manage.py runserver`


## Routes
To view the routes run the project and go to

#### For information on available routes
 ```python

 http://localhost:8000/help

```

#### View all files

 ```
 http://localhost:8000/file

 ```
#### View specific file
 ```

 http://localhost:8000/file/:id

 ```

#### Download a File
 ```

 http://localhost:8000/download/:id

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