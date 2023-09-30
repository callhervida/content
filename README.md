# content
This project let you blog posts, update or delete them and retrieve a list of or a single post.
# Content Docs

Please read this document to understand how to intract with provided endpoints.

## Table of Contents

* [Blog](#blog)
	* [Create a New Post](#create-a-new-post)
	* [Retrieve a List of Posts](#Retrieve-a-list-of-posts)
	* [Retrieve a Single Post](#Retrieve-a-single-post)
	* [Edit a Post](#edit-a-post)
  	* [Delete a Post](#delete-a-post)


## Blog
### Create a New Post

To create a new post, should use this API. 

#### Request Endpoint

	http://127.0.0.1:8000/blog/new-post/
	

#### Body

Send these parameters to the request endpoint via `POST` method.

    {
		    "title" : "test",
		    "content" : "This is the first post."
    }

#### Body Schema

This schema define the each parameter's type and value.

    {
        "title" : {
    			"type" : "string",
    			"description" : "Title of the Blog Post"
      	},
        
        "content" : {
      			"type" : "string"
      			"description" : "Content of the Blog Post"
      	},
    }


### Retrieve a List of Posts

To retrieve a list of posts, should use this API. 

#### Request Endpoint

	http://127.0.0.1:8000/blog/list/
	

#### Params

Send these parameters to the request endpoint via `GET` method.


#### Params Schema

There's no parameter's type and value.



### Retrieve a Single Post

To retrieve a single post, should use this API. 

#### Request Endpoint

	http://127.0.0.1:8000/blog/return/
	

#### Params

Send these parameters to the request endpoint via `GET` method.

    {
        "post_id": 1
    }

#### Params Schema

This schema define the each parameter's type and value.

    {
        "post_id" : {
    			"type" : "integer",
    			"description" : "Id of the Blog Post you want"
      	}
    }
  		

### Edit a post

To edit a post, should use this API. 

#### Request Endpoint

	http://127.0.0.1:8000/blog/edit/
	

#### Params

Send those parameters yo want to edit to the request endpoint via `POST` method.

    {
        "post_id": 1,
        "title": "edited",
        "content": "changed"
    }

#### Params Schema

This schema define the each parameter's type and value.

    {
        "post_id" : {
    			"type" : "integer",
    			"description" : "ID of the Blog Post you want. ID is required"
      	},
        "title" : {
    			"type" : "string",
    			"description" : "Title of the Blog Post"
      	},
        
        "content" : {
      			"type" : "string"
      			"description" : "Content of the Blog Post"
      	},
    }


### Delete a Post

To delete a post, should use this API. 

#### Request Endpoint

	http://127.0.0.1:8000/blog/delete/
	

#### Params

Send these parameters to the request endpoint via `GET` method.

    {
        "post_id": 1
    }

#### Params Schema

This schema define the each parameter's type and value.

    {
        "post_id" : {
    			"type" : "integer",
    			"description" : "Id of the Blog Post you want"
      	}
    }
