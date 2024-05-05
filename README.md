# FunAPI

FunAPI is a RESTful API built with FastAPI that provides random compliments, fortunes, fun facts, pizza ideas, life truths, and thoughts.

## Features

- **Compliments:** Brighten up your day with random compliments.
- **Fortunes:** Ponder upon random fortunes for insight and inspiration.
- **Fun Facts:** Discover random useless yet entertaining facts.
- **Pizza Ideas:** Explore unique pizza combinations for your next culinary adventure.
- **Life Truths:** Reflect on deep insights into life's mysteries and truths.
- **Thoughts:** Receive random thoughts to inspire, entertain, or provoke contemplation.

## Usage

### Base URL

The base URL for accessing the API is: `https://my-fun-api.onrender.com`

### Endpoints

#### Get Random Compliment

```http
GET /compliment
```

Returns a random compliment.

#### Get Random Fortune

```http
GET /fortune
```

Returns a random fortune.

#### Get Random Fun Fact

```http
GET /funfact
```

Returns a random fun fact.

#### Get Random Pizza Idea

```http
GET /pizzaidea
```

Returns a random pizza idea.

#### Get Random Life Truth

```http
GET /lifetruth
```

Returns a random life truth.

#### Get Random Thought

```http
GET /thought
```

Returns a random thought.

## Example

To get a random compliment, you can send a GET request to:

```http
https://my-fun-api.onrender.com/compliment
```

Example Response:

```json
{
  "success": True,
  "data": {
    "compliment": "You have a great sense of humor!"
  }
}
```

## Documentation

For detailed documentation, please visit FunAPI Documentation

[Scalar](https://my-fun-api.onrender.com/)
[Swagger UI](https://my-fun-api.onrender.com/docs)
[Redoc](https://my-fun-api.onrender.com/redoc)

## Installation

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=github.com/LakhindarPal/my-fun-api)

### Locally

1. Clone the repository:

```bash
git clone https://github.com/LakhindarPal/my-fun-api.git
```

2. Install dependencies:

```bash
cd funapi
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
