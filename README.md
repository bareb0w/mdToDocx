# Run

1. Clone the repo:

```bash
git clone https://github.com/bareb0w/mdToDocx
```

2. Build the container

```bash
docker build -t fastapi-pandoc .
```

3. Run the container

```bash
docker run --network=host fastapi-pandoc
```
